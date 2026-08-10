from langchain.chat_models import init_chat_model   
from dotenv import load_dotenv

load_dotenv()

model = init_chat_model("google_genai:gemini-3.5-flash-lite")

chat_history=[]


while True: 
    user_input = input("You:")
    chat_history.append(user_input)
    if user_input == 'exit':
        break
    result=model.invoke(chat_history)
    chat_history.append(result.text)
    print("Ai:",result.text)
  
print(chat_history)
