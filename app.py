# app.py
import streamlit as st
from transformers import pipeline

# Load the Hugging Face text generation pipeline using GPT-2
generator = pipeline("text-generation", model="gpt2")

# Streamlit app interface
st.title("GPT-2 Content Generator")
prompt = st.text_input("Enter a prompt to generate content:")

if st.button("Generate"):
    if prompt:
        with st.spinner("Generating content..."):
            # Generate content
            result = generator(prompt, max_length=50, num_return_sequences=1)
            st.write("**Generated Content:**")
            st.write(result[0]["generated_text"])
    else:
        st.warning("Please enter a prompt to generate content.")
