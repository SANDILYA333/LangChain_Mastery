from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.chat_models import init_chat_model

# Load environment variables from .env
load_dotenv()

# Initialize the chat model
model = init_chat_model("google_genai:gemini-3.5-flash-lite")

prompt = PromptTemplate(
    template = 'Generate 5 interesting facts about {topic}',
    input_variables = ['topic']
)
parser=StrOutputParser()

chain = prompt | model | parser


print(chain.invoke({"topic": "Volleyball"}))

chain.get_graph().print_ascii()