from dotenv import load_dotenv
import streamlit as st
import os 
import google.generativeai as genai

##laod the genmini api key


genai.configure(api_key="")


## funtion to generate gemini pro model
model=genai.GenerativeModel.get("gemini-pro-2024-06-20")
def gemini_response(prompt):
    model_response = model.generate_text(prompt= prompt , max_output_tokens=1024)
    return model_response.text

st.set_page_config(page_title="Gemini Pro with Streamlit", page_icon=":robot_face:")

st.header("💬 Gemini Pro with Streamlit")
input = st.text_input("Ask anything to Gemini Pro:", key="input")
submit = st.button( "Submit", key="submit")
if submit and input:
    response_text = gemini_response(input)
    st.text_area("Response from Gemini Pro:", value=response_text, height=200)
    st.success("Response generated successfully!")
