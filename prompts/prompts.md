## Prompt Hua et al. SCD

Write a short summary capturing the trajectory of an online conversation. 

Do not include specific topics, claims, or arguments from the conversation. The style you should avoid:
Example Sentence 1: “Speaker1, who is Asian, defended Asians and pointed out that a study found that whites, Hispanics, and blacks were accepted into universities in that order, with Asians being accepted the least. Speaker2 acknowledged that Asians have high household income, but argued that this could be a plausible explanation for the study’s findings. Speaker1 disagreed and stated that the study did not take wealth into consideration.” 

This style mentions specific claims and topics, which are not needed. Instead, do include indicators of sentiments (e.g., sarcasm, passive-aggressive, polite, frustration, attack, blame), individual intentions (e.g., agreement, disagreement, persistent-agreement, persistentdisagreement, rebuttal, defense, concession, confusion, clarification, neutral, accusation) and conversational strategies (if any) such as ’rhetorical questions’, ’straw man fallacy’, ’identify fallacies’, and ’appealing to emotions.’ 

The following sentences demonstrate the style you should follow:
Example Sentence 2: “Both speakers have differing opinions and appeared defensive. Speaker1 attacks Speaker2 by diminishing the importance of his argument and Speaker2 blames Speaker1 for using profane words. Both speakers accuse each other of being overly judgemental of their personal qualities rather than arguments.”
Example Sentence 3: “The two speakers refuted each other with back and forth accusations. Throughout the conversation, they kept harshly fault-finding with overly critical viewpoints, creating an intense and inefficient discussion.”
Example Sentence 4: “Speaker1 attacks Speaker2 by questioning the relevance of his premise and Speaker2 blames Speaker1 for using profane words. Both speakers accuse each other of being overly judgemental of their personal qualities rather than arguments.”

Overall, the trajectory summary should capture the key moments where the tension of the conversation notably changes. 

Here is an example of a complete trajectory summary.
Trajectory summary: Multiple users discuss minimum wage. Four speakers express their different points of view subsequently, building off of each other’s arguments. Speaker1 disagrees with a specific point from Speaker2’s argument, triggering Speaker2 to contradict Speaker1 in response. Then, Speaker3 jumps into the conversation to support Speaker1’s argument, which leads Speaker2 to adamantly defend their argument. Speaker2 then quotes a deleted comment, giving an extensive counterargument. The overall tone remains civil.

Now, provide the trajectory summary for the following conversation.
Conversation Transcript: {conversation}


## Prompt Modified Hua et al. Few-shot SCD

Write a short summary capturing the trajectory of a GitHub conversation. 

Example Sentence 1: “Speaker1, who is Asian, defended Asians and pointed out that a study found that whites, Hispanics, and blacks were accepted into universities in that order, with Asians being accepted the least. Speaker2 acknowledged that Asians have high household income, but argued that this could be a plausible explanation for the study’s findings. Speaker1 disagreed and stated that the study did not take wealth into consideration.” 

This style mentions specific claims and topics, which are not needed. Instead, do include indicators of sentiments (e.g., sarcasm, passive-aggressive, polite, frustration, attack, blame), individual intentions (e.g., agreement, disagreement, persistent-agreement, persistentdisagreement, rebuttal, defense, concession, confusion, clarification, neutral, accusation) and conversational strategies (if any) such as ’rhetorical questions’, ’straw man fallacy’, ’identify fallacies’, and ’appealing to emotions.’ 

The following sentences demonstrate the style you should follow:
Example Sentence 2: “Both speakers have differing opinions and appeared defensive. Speaker1 attacks Speaker2 by diminishing the importance of his argument and Speaker2 blames Speaker1 for using profane words. Both speakers accuse each other of being overly judgemental of their personal qualities rather than arguments.”
Example Sentence 3: “The two speakers refuted each other with back and forth accusations. Throughout the conversation, they kept harshly fault-finding with overly critical viewpoints, creating an intense and inefficient discussion.”
Example Sentence 4: “Speaker1 attacks Speaker2 by questioning the relevance of his premise and Speaker2 blames Speaker1 for using profane words. Both speakers accuse each other of being overly judgemental of their personal qualities rather than arguments.”

Overall, the trajectory summary should capture the key moments where the tension of the conversation notably changes. 

Here is an example of a complete trajectory summary.
Example Trajectory Summary: The conversation involves six users discussing an issue that was encountered in their code. User1 posts the issue asking for guidance,  causing User2 to ask for a clarifying detail. User2 provides a solution and User1 responds saying that the solution did not work. User3 then joins the conversation and asks if a solution was ever found. User4 seconds this, causing User5 to join the conversation and comment on how User3 and User4 are not project contributors and therefore have done nothing to try to fix the problem. User4 then responds expressing frustration that a solution has not been posted in the last few years.

Now, provide the trajectory summary for the following conversation.
Conversation Transcript: {conversation}


## Prompt Least to Most Decomposed SCD

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


## Prompt for Derail to Toxic scale:

I will provide you a GitHub conversation trajectory summary. On a scale of 0 to 1, what is the possibility of this conversation derailing to toxic?

Trajectory Summary: {summary}

Now, write one word output: the decimal point of occuring toxicity in the future comments in the following conversation trajectory summary.
