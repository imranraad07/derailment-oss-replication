import pandas as pd
from openai import OpenAI

openai_api_key = '...'

client = OpenAI(api_key=openai_api_key)

import time

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import csv


input_csv = 'derailed_coversations.csv'
output_csv = 'gpt_4o_derailed_ltm.csv'


prompt_template = (
"""
Let's break down the task of summarizing the trajectory of a GitHub conversation into smaller steps. 
Start with understanding the basic structure and move towards a detailed trajectory summary.

Step 1: Identify the main elements of the conversation.

Step 2: Find any triggers of tension in the conversation. 
The common triggers are: 'Failed use of code/tool or error messages', 'Technical Disagreement', 'Communication Breakdown' and 'Politics/ideology'.

Step 3: If there are triggers, identify the social orientation. 
Social orientation from circumplex theory is a social theory that characterizes interactions between speakers. 
The social orientation tagset includes: Arrogant-Calculating, Assured-Dominant, and Cold.

Step 4: Describe the sentiments and tones expressed by each participant. 
Use indicators such as Bitter Frustration, Impatience, and Mocking.

Step 5: To find tones, note the linguistic features used in the conversation. 
Pay attention to terms that correlate with tonal changes, such as second person pronouns, questioning, reasoning, negation, emphasis terms, and communication words. 

Step 6: Now, combine all the information to write a short summary capturing the trajectory of the GitHub conversation.
Do not include specific topics, claims, or arguments.

Now, provide the trajectory summary for the following conversation. 
Keep it concise and coherent, ensuring it captures the essence of the text.

Conversation Transcript: {conversation}

Write only the step 6 summary.
"""
)


def get_response_least_to_most(conversation):
    max_tokens = 8192 - 1200 
    words = conversation.split()
    while len(words) > max_tokens:
        words = words[len(words) // 2:]  
    trimmed_conversation = ' '.join(words)

    prompt = prompt_template.format(conversation=trimmed_conversation)
    response = client.chat.completions.create(model="gpt-4o", temperature=0,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ])
    refined_summary = response.choices[0].message.content.strip()
    return refined_summary



prompt_template2 = (
"""
I will provide you a GitHub conversation trajectory summary. On a scale of 0 to 1, what is the possibility of this conversation derailing to toxic?

Trajectory Summary: {summary}

Now, write one word output: the decimal point of occuring toxicity in the future comments in the following conversation trajectory summary.
"""
)



def get_response(summary):
    prompt = prompt_template2.format(summary=summary)
    response = client.chat.completions.create(model="gpt-4o", temperature=0,
    messages=[
        {"role": "system", "content": "You are a helpful GitHub moderator."},
        {"role": "user", "content": prompt}
    ])
    # Return the content of the first choice
    return response.choices[0].message.content.strip()


data = pd.read_csv(input_csv)
toxic_data = data[data['toxic']==1]
toxic_data = toxic_data['issue_id'].values
data = data[data['toxic']==0]

# Make sure the CSV has columns named 'conversation_id' and 'text'
if 'issue_id' not in data.columns or 'text' not in data.columns:
    raise ValueError("Input CSV must contain 'issue_id' and 'text' columns")

data['text'] = data['text'].astype(str).fillna('')
data['text'] = data['speaker'] + ': (' + data['text'] + ')'

grouped = data.groupby('issue_id')['text'].apply(lambda x: ' '.join(x)).reset_index()

with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['issue_id', 'response', 'possibility_toxic'])
    writer.writeheader()
    counter = 0
    correct = 0
    for idx, row in grouped.iterrows():
        try:
            issue_id = row['issue_id']
            conversation = row['text']
            response = get_response_least_to_most(conversation)
            response2 = get_response(response)
            counter = counter + 1
            if float(response2) >= 0.5:
                correct = correct + 1
            writer.writerow({'issue_id': issue_id, 'response': response, 'possibility_toxic': response2})
            print(f"Processed issue_id: {issue_id}, {response2}, {correct} ,/, {counter} {correct*100/counter}")
            time.sleep(1)
        except Exception as e:
            print(f"exception occurred for issue: {issue_id}", e)

print(f"Responses have been written to {output_csv}")
