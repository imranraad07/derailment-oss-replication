import pandas as pd
import time
import ollama
import os


from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import csv

prompt_template2 = (
"""
You will be provided with a summary of a GitHub conversation trajectory. 
A Conversation Trajectory Summary captures the evolution of a discussion by identifying key elements, triggers of tension, conversational strategies, interaction patterns, sentiments, and tonal shifts among participants. It provides a concise overview of significant dynamics and tone changes without detailing the technical aspects or specific arguments.

Now based on the given GitHub conversation trajectory summary, what is the probability that the conversation may derail and become toxic on a scale of 0 to 1 (Toxicity is defined by “any rude, disrespectful, or unreasonable comment that is likely to make one leave a discussion.”)?

Conversation trajectory summary: {summary}

Write exactly one word: the probability rounded to two decimal places.
Do not write reasoning.
"""
)


def get_response(summary):
    prompt = prompt_template2.format(summary=summary)
    output = ollama.chat(model="llama3.1:70b", messages=[{
        'role':'user',
        'content': prompt
    }])
    output = output['message']['content']
    return output


input_csv = 'hua.csv'
data = pd.read_csv(input_csv)
output_csv = 'hua-output-3.csv'
with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['issue_id', 'summary', 'possibility_toxic'])
    writer.writeheader()
    for index, row in data.iterrows():
        issue_id = row['issue_id']
        summary = row['summary']
        response2 = get_response(summary)
        writer.writerow({'issue_id': issue_id, 'summary': summary, 'possibility_toxic': response2})
        print(f"{issue_id}, {response2}")

print(f"Responses have been written to {output_csv}")
