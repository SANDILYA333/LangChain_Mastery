

from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import init_chat_models
from datetime import datetime
# Dynamic prompt template
template = ChatPromptTemplate.from_template("""
You are a {role} on {date}.
{action} the paper titled '{paper_title}' in {style} fashion.
""")
# Variables filled at runtime
formatted_prompt = template.format(
role="Research Assistant",
date="14 February 2025 00:01",
action="Summarize",
paper_title="Attention is All You Need",
The ”Summarize Fetch ILM” Workflow | 113
style="simple"
)
model = ChatOpenAI()
response = model.invoke(formatted_prompt.to_messages())
print(response.content) 