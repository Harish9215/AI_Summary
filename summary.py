import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI  # ✅ from openai-specific package

# Load environment 
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY", "ollama")
base_url = os.getenv("OPENAI_BASE_URL", "http://localhost:11434/v1")

# local LLaMA 3 model via Ollama
llm = ChatOpenAI(
    model="llama3",
    openai_api_key=api_key,
    base_url=base_url,
    temperature=0.2
)

# Prompt template
prompt = PromptTemplate(
    input_variables=["content", "role"],
    template=(
        "Please summarize the following text in a friendly and helpful way, "
        "as if you were explaining it to a {role}:\n\n{content}\n\nSummary:"
    )
)

chain = prompt | llm

# Summary function
def summarize_text(text: str, role: str = "Student") -> str:
    response = chain.invoke({"content": text, "role": role})
    return response.content if hasattr(response, "content") else str(response)