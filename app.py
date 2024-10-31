# app.py
import streamlit as st
from transformers import pipeline

# Streamlit app interface
st.title("GPT-2 Content Generator")
prompt = st.text_input("Enter a prompt to generate content:")

# Load the model in the main function
@st.cache_resource(show_spinner=False)
def load_model():
    try:
        # Load a smaller model to avoid resource issues
        generator = pipeline("text-generation", model="distilgpt2")  # Use a smaller model for better performance
        return generator
    except Exception as e:
        st.error(f"Error loading model: {e}")

generator = load_model()

if st.button("Generate"):
    if prompt:
        with st.spinner("Generating content..."):
            try:
                # Generate content
                result = generator(prompt, max_length=50, num_return_sequences=1)
                st.write("**Generated Content:**")
                st.write(result[0]["generated_text"])
            except Exception as e:
                st.error(f"Error generating content: {e}")
    else:
        st.warning("Please enter a prompt to generate content.")
