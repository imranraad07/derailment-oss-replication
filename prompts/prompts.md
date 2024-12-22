## Prompt Hua et al. SCD

Write a short summary capturing the trajectory of an online conversation.

Do not include specific topics, claims, or arguments from the conversation. The style you should avoid: Example Sentence 1: “Speaker1, who is Asian, defended Asians and pointed out that a study found that whites, Hispanics, and blacks were accepted into universities in that order, with Asians being accepted the least. Speaker2 acknowledged that Asians have high household income, but argued that this could be a plausible explanation for the study’s findings. Speaker1 disagreed and stated that the study did not take wealth into consideration.”

This style mentions specific claims and topics, which are not needed. Instead, do include indicators of sentiments (e.g., sarcasm, passive-aggressive, polite, frustration, attack, blame), individual intentions (e.g., agreement, disagreement, persistent-agreement, persistent-disagreement, rebuttal, defense, concession, confusion, clarification, neutral, accusation) and conversational strategies (if any) such as 'rhetorical questions', 'straw man fallacy', 'identify fallacies', and 'appealing to emotions.''

The following sentences demonstrate the style you should follow: 
Example Sentence 2: "Both speakers have differing opinions and appeared defensive. Speaker1 attacks Speaker2 by diminishing the importance of his argument and Speaker2 blames Speaker1 for using profane words. Both speakers accuse each other of being overly judgemental of their personal qualities rather than arguments."

Example Sentence 3: "The two speakers refuted each other with back and forth accusations. Throughout the conversation, they kept harshly fault-finding with overly critical viewpoints, creating an intense and inefficient discussion." 

Example Sentence 4: "Speaker1 attacks Speaker2 by questioning the relevance of his premise and Speaker2 blames Speaker1 for using profane words. Both speakers accuse each other of being overly judgemental of their personal qualities rather than arguments."

Overall, the trajectory summary should capture the key moments where the tension of the conversation notably changes.

Here is an example of a complete trajectory summary. Trajectory summary: Multiple users discuss minimum wage. Four speakers express their different points of view subsequently, building off of each other’s arguments. Speaker1 disagrees with a specific point from Speaker2’s argument, triggering Speaker2 to contradict Speaker1 in response. Then, Speaker3 jumps into the conversation to support Speaker1’s argument, which leads Speaker2 to adamantly defend their argument. Speaker2 then quotes a deleted comment, giving an extensive counterargument. The overall tone remains civil.

Now, provide the trajectory summary for the following conversation. 

Conversation Transcript: {conversation}


## Prompt (Modified Hua et al.) Few-shot SCD

Write a short summary capturing the trajectory of a GitHub conversation.

Do not include specific technical topics, claims, or arguments from the conversation. The style you should avoid: Example Sentence 1: “User1, who is familiar with the codebase, suggested that changing a line in the code could solve the issue, referencing recent updates. User2 responded that the approach was not feasible due to compatibility issues, suggesting an alternative solution. User1 disagreed, explaining that their suggestion should be compatible with older versions.”

This style mentions specific technical claims and topics, which are not needed. Instead, do include indicators of sentiments (e.g., sarcasm, passive-aggressive, polite, frustration, attack, blame), individual intentions (e.g., agreement, disagreement, persistent-agreement, persistent-disagreement, rebuttal, defense, concession, confusion, clarification, neutral, accusation) and conversational strategies (if any) such as 'rhetorical questions', 'straw man fallacy', 'identify fallacies', and 'appealing to emotions.''

The following sentences demonstrate the style you should follow:

Example Sentence 2: "User1 and User2 hold opposing views, and the exchange becomes tense. User1 questions User2’s logic dismissively, while User2 accuses User1 of misunderstanding the project goals. The tension escalates as both users shift to personal criticisms rather than focusing on solutions."

Example Sentence 3: "The contributors exchange repeated rebuttals, each insisting on their approach. The conversation becomes increasingly strained as they challenge each other's understanding, with frustration apparent on both sides."

Example Sentence 4: "User1 becomes confrontational, accusing User2 of overlooking key project guidelines, while User2 defensively counters by pointing to established practices. Both users end up focusing on each other’s communication style rather than on constructive feedback."

Overall, the trajectory summary should capture the key moments where the tension of the conversation notably changes.

Here is an example of a complete trajectory summary.

Trajectory Summary: Several contributors discuss an unresolved code issue. User1 requests guidance, and User2 offers a solution that User1 finds unworkable, leading to mild frustration. User3 enters the conversation neutrally, asking if any progress has been made, and is soon joined by User4, echoing the need for resolution. User5 becomes defensive, blaming User3 and User4 for not contributing to the project’s resolution, escalating the tension. User4 responds with frustration over the lack of a solution, and the conversation ends on a tense note.

Now, provide the trajectory summary for the following GitHub conversation.

Conversation Transcript: {conversation}


## Prompt Least to Most Decomposed SCD

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

Step 7: Refine the summary by following the below points:
 - Do not include specific technical details, claims, or arguments from the conversation. 
 - Keep it concise and coherent, ensuring it captures the essence of the text. 
 - Focus on capturing key moments where the tonal shifts that becomes personal.
 - Focus where the conversation dynamics change significantly.

Here is an example of a complete trajectory summary: 
"Several contributors discuss an unresolved code issue. User1 requests guidance, and User2 offers a solution that User1 finds unworkable, leading to mild frustration. User3 enters the conversation neutrally, asking if any progress has been made, and is soon joined by User4, echoing the need for resolution. User5 becomes defensive, blaming User3 and User4 for not contributing to the project’s resolution, escalating the tension. User4 responds with frustration over the lack of a solution, and the conversation ends on a tense note."

Task: Using the above guideline, write the final trajectory summary for the following GitHub conversation.

Conversation Transcript: {conversation}

Write only the trajectory summary in double quotes.


## Predictor Prompt for Derailing to Toxic:

You will be provided with a summary of a GitHub conversation trajectory. A Conversation Trajectory Summary captures the evolution of a discussion by identifying key elements, triggers of tension, conversational strategies, interaction patterns, sentiments, and tonal shifts among participants. It provides a concise overview of significant dynamics and tone changes without detailing the technical aspects or specific arguments.

Now based on the given GitHub conversation trajectory summary, what is the probability that the conversation may derail and become toxic on a scale of 0 to 1 (Toxicity is defined by “any rude, disrespectful, or unreasonable comment that is likely to make one leave a discussion.”)?

Conversation trajectory summary: {summary}

Write exactly one word: the probability rounded to two decimal places.

Do not write reasoning.