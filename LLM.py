from groq import Groq


client = Groq( api_key="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")

#prompt = input("Ask the LLM something:")



# =========================
# 1. ZERO-SHOT PROMPTING
# =========================

#zero_shot_prompt = """
#hat is a computer?
#Give a simple answer.
#"""

#response = client.chat.completions.create(
#    model="openai/gpt-oss-20b",
#    messages=[
#       {
#          "role": "user",
#         "content": zero_shot_prompt
#    }
#]
#)

#print("\n========== ZERO-SHOT ==========")
#print(response.choices[0].message.content)


# =========================
# 2. FEW-SHOT PROMPTING
# =========================

#few_shot_prompt = """
#Answer the questions based on the examples.

#Question: What is C++?
#Answer: C++ is a programming language.

#Question: What is Python?
#Answer: Python is a programming language.

#Question: What is HTML?
#Answer: HTML is a markup language used to create web pages.

#Now answer this question:

#Question: What is a computer?
#Answer:
#"""

#response = client.chat.completions.create(
#    model="openai/gpt-oss-20b",
#    messages=[
#        {
#            "role": "user",
#            "content": few_shot_prompt
#        }
#    ]
#)

#print("\n========== FEW-SHOT ==========")
#print(response.choices[0].message.content)


# =========================
# 3. CHAIN-OF-THOUGHT
# =========================

#cot_prompt = """
#Solve this problem step by step and give a brief explanation.

#A student has 10 books.
#He buys 5 more books.
#Then he gives 3 books to his friend.

#How many books does he have now?
#"""

#response = client.chat.completions.create(
#    model="openai/gpt-oss-20b",
#    messages=[
#        {
#            "role": "user",
#            "content": cot_prompt
#        }
#    ]
#)

#print("\n========== CHAIN-OF-THOUGHT ==========")
#print(response.choices[0].message.content

response = client.chat.completions.create(

    model="openai/gpt-oss-20b",

    messages=[

        {
            "role": "user",
            "content": "What is Machine Learning?"
        }
    ]
)

print(response.choices[0].message.content)