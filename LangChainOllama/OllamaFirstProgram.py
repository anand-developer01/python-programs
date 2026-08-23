from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

# 1. Create Prompt
prompt = ChatPromptTemplate.from_template(
"Explain {topic} in simple words."
)

# 2. Create LLM
model = ChatOllama(
model="llama3.2"
)

# 3. Create Output Parser
parser = StrOutputParser()

# 4. Create LCEL Chain
chain = prompt | model | parser

# 5. Execute Chain
result = chain.invoke({
"topic": "space"
})

# 6. Print Result
print(result)
