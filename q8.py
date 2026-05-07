prompt_a = """
I am a marketing manager at a retail company and we have just finished a three-month campaign. My team has collected customer feedback through an online survey and we now have about 500 responses stored in a spreadsheet. Each response includes the customer's age group, the product they purchased, their satisfaction rating from 1 to 5, and a short written comment. I need to present the findings to our CEO next Friday in a way that is easy to understand. Can you analyse this data for me, highlight which age groups and products have the lowest satisfaction scores, identify the most common complaints from the written comments, and summarise everything in a short paragraph I can use as an executive summary?
"""

prompt_b = """
Role: You are a data analyst helping a retail marketing team. Task: Analyse customer survey data from a 3-month campaign.
Data: 500 responses containing age group, product purchased, satisfaction rating (1-5), and written comments.

Steps:
1. Identify age groups and products with the lowest satisfaction scores.
2. Extract the most common themes from the written comments.
3. Summarise findings in an executive summary paragraph.

Audience: CEO presentation on Friday.
Constraints: Keep the summary concise and free of technical jargon.
"""


# Task 1
# Read both prompts above carefully, then answer the questions below as comments.

# Q8a: Which prompt do you think will get a better response from an AI?
# Harish's answer: Prompt B will get a better response from an AI.

# Q8b: Give TWO reasons to support your choice.
# Harish's answer:
    # Reason 1:
        # Prompt B uses an explicit, labelled structure (Role, Task, Data, Steps, Audience, Constraints), which makes it easy for the AI to separate context from instructions. Prompt A mixes everything into a single flowing paragraph, so the AI has to work harder to identify the actual sub-tasks and may weight incidental details unevenly.

    # Reason 2:
        # Prompt B specifies explicit output constraints ("concise and free of technical jargon"), giving the AI clear success criteria for the response.Prompt A never tells the AI what the output should look like in style or length, so the AI might produce a summary that is technically correct but too long, too jargon-heavy, or in the wrong tone for a CEO presentation.

# Q8c: What is ONE strength of the prompt you did NOT choose?
# Harish's answer:
    # Prompt A provides richer narrative context; it tells the AI that the data came from an online survey, that it is stored in a spreadsheet, and that the speaker is a marketing manager presenting to their own CEO. This kind of situational detail helps the AI tailor its response appropriately (e.g., factoring in self-selection bias from an online survey, or matching the tone a marketing manager would use with a CEO). Prompt B sacrifices some of this richness in exchange for clean structure.


# Task 2: Rewrite either prompt by borrowing ONE element from the other to make it stronger. Explain what you borrowed and why.
# Harish's answer:

    # I am rewriting Prompt A by borrowing the explicit "Constraints" element from Prompt B. This is Prompt A's biggest weakness -- it never tells the AI what the output should look like in terms of length and style -- and the fix is a single sentence at the end.

    # Rewritten Prompt A:

''' I am a marketing manager at a retail company and we have just finished a three-month campaign. My team has collected customer feedback through an online survey and we now have about 500 responses stored in a spreadsheet. Each response includes the customer's age group, the product they purchased, their satisfaction rating from 1 to 5, and a short written comment. I need to present the findings to our CEO next Friday in a way that is easy to understand. Can you analyse this data for me, highlight which age groups and products have the lowest satisfaction scores, identify the most common complaints from the written comments, and summarise everything in a short paragraph I can use as an executive summary? Please keep the summary concise and free of technical jargon, suitable for a CEO who is not a data specialist.
    
What I borrowed: the "Constraints" line from Prompt B ("Keep the summary concise and free of technical jargon").
    
Why I borrowed it: explicit output constraints are one of the highest-leverage techniques in prompt engineering. Without them, an AI might produce a long, jargon-heavy response that is analytically correct but unsuitable for a CEO audience. Adding one short sentence at the end of Prompt A gives the AI clear success criteria for the output, while preserving Prompt A's strength in narrative context.  

'''
