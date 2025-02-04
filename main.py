import streamlit as st
from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

if API_KEY:
    genai.configure(api_key=API_KEY)

# Streamlit page config with theme enhancements
st.set_page_config(
    page_title="YouTube Video Summarizer",
    page_icon="📹",
    layout="wide"
)

st.markdown(
    """
    <style>
    body {
        background-color: #f4f4f4;
        font-family: Arial, sans-serif;
    }
    .title {
        text-align: center;
        font-size: 32px;
        color: #333;
        font-weight: bold;
    }
    .header {
        text-align: center;
        font-size: 24px;
        color: #666;
    }
    .stTextArea textarea{
        height: 100px;
        font-size: 16px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 24px;
        font-size: 16px;
        border-radius: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='title'>🎥 AI-Powered YouTube Video Summarizer</div>", unsafe_allow_html=True)
st.markdown("<div class='header'>Powered by Gemini 2.0 Flash Exp</div>", unsafe_allow_html=True)

@st.cache_resource
def initialize_agent():
    return Agent(
        model=Gemini(id="gemini-2.0-flash-exp"),
        name="YouTube AI Summarizer",
        tools=[DuckDuckGo()],
        markdown=True
    )

# Initialize the Agent
ai_agent = initialize_agent()

# Get YouTube Video Link
video_url = st.text_input("Enter YouTube Video URL", "https://www.youtube.com/watch?v=example")

# Extract Video ID from URL
def extract_video_id(url):
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be" in url:
        return url.split(".be/")[1].split("?")[0]
    return None

video_id = extract_video_id(video_url)

try:
    # Try fetching the transcript in English first
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
except:
    try:
        # If English transcript is unavailable, fetch the Hindi auto-generated one
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['hi'])
    except Exception as e:
        st.error(f"Error fetching transcript: {e}")
        transcript = None  # Set transcript to None if fetching fails

# Proceed only if transcript is successfully fetched
if transcript:
    transcript_text = " ".join([entry['text'] for entry in transcript])


if video_id:
    st.video(video_url)
    
    user_query = st.text_area(
        "What insights are you seeking from this video?",
        placeholder="Ask anything about the video content",
        help="Provide specific questions or insights you want from the video"
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Summarize Video"):
            try:
                with st.spinner("Fetching transcript and analyzing video..."):
                    
                    analysis_prompt = f"""
                    Summarize the following YouTube video transcript:
                    {transcript_text}

                    Additionally, answer the user query: {user_query}
                    """
                    
                    response = ai_agent.run(analysis_prompt)
                    
                    st.subheader("Summary & Insights")
                    st.markdown(response.content)
            except Exception as error:
                st.error(f"Error fetching transcript: {error}")
    
    with col2:
        if user_query and st.button("Get Insights"):
            try:
                with st.spinner("Analyzing insights..."):
                   
                    # Debugging: Print transcript to confirm
                    
                    # Explicitly tell Gemini the transcript is available
                    insight_prompt = f"""
                    The following is the transcript of a YouTube video. You **DO HAVE** access to this text.
                    
                    Transcript:
                    {transcript_text}

                    Based on the video transcript, answer the following question:
                    {user_query}
                    """
                    insight_response = ai_agent.run(insight_prompt)
                    
                    st.subheader("User-Specific Insights")
                    st.markdown(insight_response.content)
            except Exception as error:
                st.error(f"Error analyzing insights: {error}")
else:
    st.info("Enter a valid YouTube URL to begin analysis")

st.markdown("""<br><hr><center><b>Developed by Sunil Kumar Modi</b></center>""", unsafe_allow_html=True)
