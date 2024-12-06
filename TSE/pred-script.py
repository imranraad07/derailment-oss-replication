import pandas as pd
import time
import ollama 
import os


from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import csv

prompt_template_least_to_most = (
"""
Here is step-by-step guideline to write an GitHub conversation trajectory summary:

Step 1: Identify the main elements of the conversation.

Step 2: Find any triggers of tension in the conversation. The common triggers are: 
	Failed use of tool/code or error messages: trouble with code/tool.
	Communication breakdown: being misinterpreted by people or being unable to follow.
	Rejection: receiving a quick rejection or a rejection without sufficient explanation.
	Violation of community conventions: disagreement with the workflow imposed by the community.
	Past interactions: comments are posted that refer to past interactions of the author with the project.
	Politics/ideology: arising over politics or ideology differences (specific beliefs).
	Technical disagreement: having differing views on some technical component of the project.
	Unprovoked: uncivil behavior or hostility occurs without an apparent reason or trigger.


Step 3: If there are triggers, identify the social orientation. Social orientation from circumplex theory is a social theory that characterizes interactions between speakers. The social orientation tagset includes: Assured-Dominant, Gregarious-Extraverted, Warm-Agreeable, Unassuming-Ingenuous, Unassured-Submissive, Aloof-Introverted, Cold, Arrogant-Calculating, which are defined below in more detail.
	Assured-Dominant: Demands to be the center of interest, demands attention, does most of the talking, speaks loudly, is firm, is self-confident, is forceful, is ambitious, is assertive, is persistent, is domineering, not self-conscious
	Gregarious-Extraverted: Feels comfortable around people, starts conversations, talks to a lot of different people, loves large groups, is friendly, is enthusiastic, is warm, is extraverted, is good-natured, is cheerful / happy, is pleasant, is outgoing, is approachable, is not shy, is \"lively\"
	Warm-Agreeable: is interested in people, reassures others, inquires about others’ well-being, gets along well with others, is kind, is polite and courteous, is sympathetic, is respectful, is tender-hearted, is cooperative, is appreciative, is accommodating, is gentle, is charitable
	Unassuming-Ingenuous: Tolerates a lot from others, takes things as they come, tells the truth, thinks of others first, does not brag or boast, seldom stretches the truth, does not scheme or plot, is modest, is trustworthy, is unassuming, is honest, not self-centered, is sincere, not demanding, is straightforward
	Unassured-Submissive: Speaks softly, lets others finish what they are saying, dislikes being the center of attention, doubts themselves, not especially thorough, doesn’t like to work too hard / will give up easily, is impractical, is timid, is inconsistent, is weak, is disorganized, is not authoritative, is a bit lazy, is not forceful
	Aloof-Introverted: Is quiet, especially around strangers, is a very private person, doesn’t talk a lot / has little to say, doesn’t smile much, doesn’t reveal much about themselves, is not demonstrative (verbally or non-verbally), is distant, is shy, is impersonal, is introverted, is disinterested in others, is bashful, is not very social, is focused inward
	Cold: Believes people should fend for themselves, doesn’t fall for sob-stories, is not interested in other people’s problems, not warm toward others, is cruel, is ruthless, is cold-hearted, is hard-hearted, is unsympathetic, is uncharitable
	Arrogant-Calculating: Flaunts what they have, boasts and brags, will plot and scheme to get ahead, willing to exploit others for own benefit, is big-headed, is tricky, is boisterous, is conniving / calculating, is conceited, is crafty / cunning, is cocky, is manipulative of others


Step 4: Describe the sentiments and tones expressed by each participant. Use indicators such as:
	Bitter frustration: when someone expresses strong frustration.
	Impatience: participants might demonstrate impatience when they express a feeling that it is taking too long to solve a problem, understand a solution, or answer a question.
	Irony: contributors used expressions that usually signify the opposite in a mocking or blaming tone.
	Insulting: insulting remarks directed at another person.
	Mocking: when a discussion participant is making fun of someone else, usually because that person has made a mistake.
	Threat: contributors put a condition impacting the result of another discussion participant or that person’s career.
	Vulgarity: using profanity or language that is not considered proper.
	Entitlement: expecting special privileges, attention, or resources without regard for the norms of collaboration and respect.
	Identity attack/Name-Calling: race, religion, nationality, gender, sexual orientation, or any other kind of attacks and mean/offensive words directed at someone or a group of people.


Step 5: To find tones, note the conversation strategies used in the conversation. Pay attention to language that signals tone shifts, such as:
    Rhetorical Questions: Questions posed not to elicit an answer, but to make a point or lead the conversation in a particular direction, often used to challenge the other party’s reasoning.
    Supporting with Evidence: Providing concrete data, facts, or references to back up one's claims or opinions to strengthen an argument.
    Justifying with Personal Experience: Using personal anecdotes or experiences as a way to validate an argument, making the point more relatable or authentic.
    Hedging: Softening the impact of a statement by showing uncertainty or caution (e.g., “I might be wrong, but…”), which can make disagreements less confrontational.
    Drawing Comparisons: Highlighting similarities or differences between ideas or situations to make a point more understandable or persuasive.
    Questioning Logic: Directly challenging the reasoning or coherence of the other participant's argument to expose flaws or weaknesses.
    Posing Challenges or Requests for Clarification: Asking the other speaker to elaborate on or justify a statement, often pushing them to refine or defend their position.

Step 6: Combine all the information from step 1-5 to write a short summary capturing the trajectory of the GitHub conversation. 
Do not include specific technical details, claims, or arguments from the conversation. 
Keep it concise and coherent, ensuring it captures the essence of the text. 
Focus on capturing key moments where the tone shifts or where the conversation dynamics change significantly, without mentioning specific technical details.

Here is an example of a complete trajectory summary. 
Trajectory summary: "Several contributors discuss a technical approach for a GitHub project. User1 raises a question regarding a method proposed by User2, to which User2 responds with clarification and additional details. User3 then joins, providing alternative suggestions that complement both User1’s and User2’s points. User4 later contributes by summarizing the key points and proposing a potential way forward based on the collective input. The conversation maintains a neutral and constructive tone, with each user focused on finding a solution."

Task: Using the above guideline, provide the final summary of the following GitHub conversation.

Conversation Transcript: {conversation}

Write only the final summary in double quotes.
"""
)

prompt_template2 = (
"""
You are provided with a summary of GitHub conversation trajectory. 
The summary provides a concise description of how participants' interactions evolve during a conversation, focusing on changes in tones, conversational strategies, and interaction patterns, rather than just the content being discussed.

On a scale of 0 to 1, based on this conversation trajectory summary, what is the probability that this conversation will turn into toxic?

Conversation trajectory summary:

{summary}

Write exactly one word: the probability up to two decimal point.

Do not write reasoning.
"""
)


def get_response_least_to_most(conversation):
    # max_tokens = 8192 - 1200 
    words = conversation.split()
    # while len(words) > max_tokens:
    #     words = words[len(words) // 2:]  # Remove the first half
    # trimmed_conversation = ' '.join(words)

    prompt = prompt_template_least_to_most.format(conversation=conversation)
    if len(words) > 2000:
        output = ollama.chat(model="llama3.1:70b", messages=[{
            'role':'user',
            'content': prompt
        }], 
        options=dict(temperature=0.0, num_ctx=8192)
        )
    else:
        output = ollama.chat(model="llama3.1:70b", messages=[{
            'role':'user',
            'content': prompt
        }], 
        options=dict(temperature=0.0)
        )
    output = output['message']['content']
    return output

def get_response(summary):
    prompt = prompt_template2.format(summary=summary)
    output = ollama.chat(model="llama3.1:70b", messages=[{
        'role':'user',
        'content': prompt
    }])
    output = output['message']['content']
    return output


input_csv = 'unified_dataset.csv'
data = pd.read_csv(input_csv)
data['text'] = data['text'].astype(str).fillna('')
data['text'] = data['speaker'] + ': (' + data['text'] + ')'
counter = 0
accurate = 0
output_csv = 'local-combined-2.csv'
with open(output_csv, mode='a', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['issue_id', 'response', 'possibility_toxic', 'actually_toxic'])
    writer.writeheader()
    for idx, group in data.groupby('issue_id'):
        current_coversation = ''
        is_toxic = 0
        for index, row in group.iterrows():
            current_coversation = current_coversation + "\n" + row['text'] 
            issue_id = row['issue_id']
            is_toxic = row['toxic']

            if is_toxic == 1:
                break

        if issue_id <= 269261234:
            continue
        
        if is_toxic == 1:
            continue

        try:
            counter = counter +1
            response = get_response_least_to_most(current_coversation)
            response2 = get_response(response)
            writer.writerow({'issue_id': issue_id, 'response': response2, 'possibility_toxic': response, 'actually_toxic': is_toxic})
            if float(response2) >= 0.5:
                accurate = accurate + 1
            print(f"{issue_id}, {response2}, {is_toxic}, {counter}, {accurate}")
        except Exception as e:
            print(e)

print(f"Responses have been written to {output_csv}")