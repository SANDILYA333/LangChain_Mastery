from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.chat_models import init_chat_model

# Load environment variables from .env
load_dotenv()

# Initialize the chat model
model = init_chat_model("google_genai:gemini-3.5-flash-lite")

prompt1 = PromptTemplate(
    template = 'Generate a detailed report on {topic}',
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = 'Generate a 5 pointer summary from the following text \n {text}',
    input_variables = ['text']
)

paser = StrOutputParser()

# Building the chain

chain = prompt1 | model | paser | prompt2 | model | paser

print(chain.invoke({'topic':"Unemployement in INdia"}))