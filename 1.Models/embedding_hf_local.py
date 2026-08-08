from langchain_huggingface import HuggingFaceEmbeddings
import sentence_transformer
embedding = HuggingFaceEmbeddings(model_name= 'deepseek-ai/DeepSeek-V4-Flash-0731')
text = "Delhi is the capital of india"

vector = embedding.embed_query(text)
print(str(vector))