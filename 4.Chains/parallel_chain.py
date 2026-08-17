from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from langchain.chat_models import init_chat_model

load_dotenv()

model1 = init_chat_model("google_genai:gemini-3.5-flash-lite")
model2 = init_chat_model("google_genai:gemini-2.5-flash")

prompt1 = PromptTemplate(
    template = 'Generate short and simple summary from the text below:\n{text}',
    input_variables = ['text']
)

prompt2 = PromptTemplate(
    template = 'Generate 10 creative headlines for the text below:\n{text}',
    input_variables = ['text']
)

prompt3 = PromptTemplate(
    template = 'Merge the summary and headlines in a creative way:\n\nSummary:\n{summary}\n\nHeadlines:\n{headlines}',
    input_variables = ['summary', 'headlines']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel(
    summary=prompt1 | model1 | parser,
    headlines=prompt2 | model2 | parser
)

merge_chain = prompt3 | model2 | parser

chain = parallel_chain | merge_chain

print(chain.invoke({'text': 'AI is revolutionizing many industries by automating tasks, analyzing large datasets, and enabling new capabilities. From healthcare to finance, AI is transforming how we work and live. With continuous advancements, AI is expected to play an even more significant role in our future.'}))
