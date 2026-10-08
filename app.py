import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="Time Machine AI", page_icon="⏳")
st.title("⏳ PHOTO TIME MACHINE")
st.write("Upload any photo - I tell Past, Present, Future!")

api = st.sidebar.text_input("Enter Gemini API Key", type="password")
st.sidebar.link_button("Get FREE Key", "https://aistudio.google.com/app/apikey")

if not api:
    st.warning("Enter API key in sidebar daa ☝️")
    st.stop()

genai.configure(api_key=api)
model = genai.GenerativeModel('gemini-1.5-flash')

file = st.file_uploader("📸 Upload photo", type=["jpg","png","jpeg"])

if file:
    img = Image.open(file)
    st.image(img, width=300)
    if st.button("🚀 TRAVEL IN TIME", type="primary"):
        with st.spinner("Time travelling daa..."):
            prompt = """
            You are a fun Photo Time Machine AI. Look at this image and give 3 parts:

            1) 5 MINS BEFORE - What funny story happened just before this photo?
            2) PRESENT - What is happening now? Describe dress, mood, background.
            3) 5 MINS AFTER - What will happen next? Predict funny future.

            Use emojis, make it very entertaining, in simple English.
            """
            res = model.generate_content([prompt, img])
            st.success("Time Travel Done! 🎉")
            st.markdown(res.text)
            st.balloons()
