import json

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate


# -----------------------------
# 1. Load JSON notes
# -----------------------------
with open("notes.json", "r") as file:
    data = json.load(file)


# -----------------------------
# 2. Convert notes into text
# -----------------------------
notes = ""

for topic in data["topics"]:
    notes += f"""
Topic: {topic["title"]}
Notes: {topic["notes"]}
"""


# -----------------------------
# 3. Create Ollama LLM
# -----------------------------
llm = ChatOllama(
    model="llama3.2",
    temperature=0
)


# -----------------------------
# 4. Create prompt
# -----------------------------
prompt = ChatPromptTemplate.from_template("""
You are an AI tutor.

Answer the user's question using ONLY the subject notes
provided below.

If the answer is not available in the notes, say:
"I don't have that information in your notes."

Subject notes:
{notes}

User question:
{question}
""")


# -----------------------------
# 5. Create chain
# -----------------------------
chain = prompt | llm


# -----------------------------
# 6. Ask questions
# -----------------------------
while True:

    question = input("\nYou: ")

    if question.lower() in ["exit", "quit"]:
        break

    response = chain.invoke({
        "notes": notes,
        "question": question
    })

    print("\nAI:", response.content)






# ------------------------------------------------------------
# --------------------------------------------------
# Install packages
# Since you're already working with Ollama and LangChain:
# --$> pip3 install langchain langchain-ollama
# Make sure Ollama is running and you have a model:
# --$> ollama pull llama3.2
# You can check:
 # --$> ollama list
# ------------------------

# Run it
# --$> python3 ai_agent.py

# Then:
# You: What are decorators?

# AI: A decorator is a function that modifies or extends
# the behavior of another function. They are commonly used
# for logging, authentication, timing and validation.

# Try:
# You: What is Django?
# For Django, it should respond:
# I don't have that information in your notes.
