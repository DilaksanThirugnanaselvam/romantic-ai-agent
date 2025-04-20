import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

# --- Load Environment Variables ---
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = "llama-3.3-70b-versatile"  # Model you want to use

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

# Love AI Agent Function via Groq
def love_ai_agent(prompt):
    system_prompt = """
    You are LoveAI, a friendly, empathetic, romantic chatbot.
    You write poetic love messages, romantic advice, and emotional support.
    Be kind, supportive, and emotionally intelligent.
    Use attractive and relevant emojis in your responses to make them more engaging.
    """
    try:
        completion = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500,
            top_p=1,
            stream=False,
            stop=None,
        )
        return completion.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {e}"

# --- Streamlit UI ---
st.set_page_config(page_title="💖 Love AI Agent 🌹👩‍❤️‍💋‍👨", layout="centered")

# Custom CSS for animations, stickers, and UI enhancements
st.markdown(
    """
    <style>
    .stApp {
        background-color: #ffe6e6;
    }
    .stTextInput input {
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    .stTextInput input::placeholder {
        color: red;
    }
    h1 {
        color: red;
        animation: glow 2s infinite alternate;
    }
    @keyframes glow {
        0% { text-shadow: 0 0 5px #ff69b4; }
        100% { text-shadow: 0 0 20px #ff1493; }
    }
    .sticker {
        position: fixed;
        animation: float 6s infinite ease-in-out;
    }
    @keyframes float {
        0% { transform: translateY(0); }
        50% { transform: translateY(-20px); }
        100% { transform: translateY(0); }
    }
    .sticker-1 { top: 10%; left: 5%; font-size: 50px; }
    .sticker-2 { top: 20%; right: 5%; font-size: 50px; }
    .sticker-3 { bottom: 10%; left: 10%; font-size: 50px; }
    .sticker-4 { bottom: 20%; right: 10%; font-size: 50px; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Add animated stickers (emojis) to the UI
st.markdown(
    """
    <div class="sticker sticker-1">💖</div>
    <div class="sticker sticker-2">🎶</div>
    <div class="sticker sticker-3">🌸</div>
    <div class="sticker sticker-4">💌</div>
    """,
    unsafe_allow_html=True,
)

st.title("💖 Love AI Agent 🌹 ")

st.markdown("""
Welcome to LoveAI! Ask for love messages, poems, stress busters, and heartwarming words.
""")

user_input = st.text_input("Tell me how you feel or what you want:", "", placeholder="💖 Type your message here...")

if st.button("Send Love 💌"):
    if user_input:
        with st.spinner("LoveAI is thinking... 💭"):
            response = love_ai_agent(user_input)
            st.success(response)
    else:
        st.warning("Please type something for LoveAI!")

st.markdown("---")
st.caption("Made with ❤️ by Dilaksan Thirugnanaselvam")
