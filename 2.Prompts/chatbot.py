from langchain.chat_models import init_chat_model   
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = init_chat_model("google_genai:gemini-3.5-flash-lite")

chat_history=[
    SystemMessage(content='You are a helpful AI assistant')
]


while True: 
    user_input = input("You:")
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result=model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.text))
    print("Ai:",result.text)
  
print(chat_history)
