import openai
import streamlit as st

# Set up OpenAI API key (stored in Streamlit secrets)
openai.api_key = st.secrets["openai_api_key"]  # Store your OpenAI API key as "openai_api_key" in Streamlit Secrets

# Streamlit UI setup
st.title("AI-Powered Content Generator with OpenAI")
st.write("Enter a prompt below, and AI will generate content for you!")

# User prompt input
user_prompt = st.text_input("Enter your prompt:")

# Generate content on button click
if st.button("Generate Content"):
    if user_prompt.strip() == "":
        st.warning("Please enter a valid prompt.")
    else:
        with st.spinner("Generating content..."):
            try:
                # Generate content using OpenAI API
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": user_prompt}]
                )
                st.write("**Generated Content:**")
                st.write(response['choices'][0]['message']['content'])
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
