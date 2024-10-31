# app.py
import streamlit as st
from transformers import pipeline

# Streamlit app interface
st.title("GPT-2 Content Generator")
prompt = st.text_input("Enter a prompt to generate content:")

# Load the model
@st.cache_resource(show_spinner=False)
def load_model():
    try:
        # Load the GPT-2 model
        generator = pipeline("text-generation", model="gpt2")  # Use GPT-2
        return generator
    except Exception as e:
        st.error(f"Error loading model: {e}")

generator = load_model()

if st.button("Generate"):
    if prompt:
        with st.spinner("Generating content..."):
            try:
                # Generate content
                result = generator(prompt, max_length=100, num_return_sequences=1, do_sample=True, top_k=50, top_p=0.95)
                st.write("**Generated Content:**")
                st.write(result[0]["generated_text"])
            except Exception as e:
                st.error(f"Error generating content: {e}")
    else:
        st.warning("Please enter a prompt to generate content.")
