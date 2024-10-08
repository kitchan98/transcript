import streamlit as st
from api import get_transcript

st.title("YouTube Transcript Fetcher")

video_url = st.text_input("Enter YouTube Video URL:")

if video_url:
    video_id = video_url.split("v=")[-1]
    if st.button("Get Transcript"):
        transcript = get_transcript(video_id)
        st.text_area("Transcript", transcript, height=300)