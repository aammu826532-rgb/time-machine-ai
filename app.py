import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="Time Machine AI", page_icon="⏳")
st.title("⏳ PHOTO TIME MACHINE")
st.write("Upload any photo - I tell Past, Present, Future!")

api = st.sidebar.text_input("Enter Gemini API Key", type="password")
st.sidebar.link_button("Get FREE Key", "https://aistudio.google.com/app/apikey")

if not api:
    st.warning("Enter API key in sidebar daa 👈")
    st.stop()

genai.configure(api_key=api)
model = genai.GenerativeModel('gemini-1.5-flash')

file = st.file_uploader("📸 Upload photo", type=["jpg","png","jpeg"])
if file:
    img = Image.open(file)
    st.image(img, width=300)
    if st.button("🚀 TRAVEL IN TIME", type="primary"):
        with st.spinner("Time traveling daa..."):
            prompt = "You are Photo Time Machine AI. For this image give: 1) 5 mins BEFORE - what happened story 2) NOW - what person thinking 3) 5 mins AFTER - future prediction. Use funny Gen-Z Kannada slang daa, emojis"
            res = model.generate_content([prompt, img])
            st.markdown(res.text)
            st.balloons()
