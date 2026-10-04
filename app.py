import streamlit as st
import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

st.title("🎨 Text to Image")

prompt = st.text_input("Enter your image description:")

if st.button("Generate Image"):
    if not prompt:
        st.warning("Please enter a description.")
    else:
        try:
            client = InferenceClient(
                token=os.getenv("HF_TOKEN")
            )

            with st.spinner("Generating image..."):
                image = client.text_to_image(prompt)

            st.image(image, caption="Generated Image")

        except Exception as e:
            st.error(f"Error: {e}")