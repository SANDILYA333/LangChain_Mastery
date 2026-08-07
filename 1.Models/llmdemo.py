import os
from langchain.chat_models import init_chat_model
from dotenv  import load_dotenv

load_dotenv()

model = init_chat_model("google_genai:gemini-2.5-flash-lite")

result=model . invoke("What is the Capital of India")
print(result)