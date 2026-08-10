##Prompt is given as input from the user 
import os
from langchain.chat_models import init_chat_model
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt
from dotenv import load_dotenv

load_dotenv()# 


model = init_chat_model("google_genai:gemini-3.5-flash-lite")

st.header('Research tool')
# user_input=st.text_input('Enter your Prompt:')
##This method of prompting is called static prompting and is usually not preferred as 
## it gives the user a lot of unnecessary control and we dont want that to happen 

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

template = load_prompt('template.json')



if st.button('Summarize'):
    chain = template | model
    result = chain.invoke({
        'paper_input':paper_input,
        'style_input':style_input,
        'length_input':length_input
    })
    st.write(result.text)

