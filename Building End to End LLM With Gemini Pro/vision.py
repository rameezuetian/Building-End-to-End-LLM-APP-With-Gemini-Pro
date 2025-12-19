import streamlit as st
import google.generativeai as genai
import os
from PIL import Image

# Configure Gemini API
genai.configure(api_key)

# Load Gemini Pro Vision model
model = genai.GenerativeModel("gemini-pro-vision")

def gemini_vision_response(image, prompt):
    response = model.generate_content(
        [prompt, image],
        generation_config={"max_output_tokens": 1024}
    )
    return response.text

# Streamlit UI
st.set_page_config(page_title="Gemini Pro Vision with Streamlit", page_icon="🤖")
st.header("🖼️ Gemini Pro Vision with Streamlit")

# Image input options
uploaded_image = st.file_uploader(
    "Upload an image", type=["jpg", "jpeg", "png"]
)

prompt = st.text_input("Enter your prompt for the image:")

submit = st.button("Submit")

if submit:
    if uploaded_image is None:
        st.error("Please upload an image.")
    elif prompt.strip() == "":
        st.error("Please enter a prompt.")
    else:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        with st.spinner("Generating response..."):
            response_text = gemini_vision_response(image, prompt)

        st.text_area(
            "Response from Gemini Pro Vision:",
            value=response_text,
            height=200
        )
        st.success("Response generated successfully!")
