import pandas as pd
import time
import ollama
import os


from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import csv

prompt_template2 = (
"""
You will be provided with a summary of a GitHub conversation trajectory. This summary offers a concise overview of how participants' interactions evolve during the conversation, emphasizing shifts in tone, conversational strategies, and interaction patterns rather than the specific content discussed.

On a 0 to 1 scale, based on the given conversation trajectory summary, what is the probability that the conversation may derail and become toxic?

Toxicity is defined as 'rude, disrespectful, or unreasonable language that is likely to make someone leave a discussion.'

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
output_csv = 'hua-output.csv'
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
