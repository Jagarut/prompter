import os
import pyperclip
import streamlit as st
from prompt_optimizer import PromptOptimizer
from groq_client import GroqClient
from dotenv import load_dotenv

load_dotenv()

DEFAULT_TEMPERATURE = float(os.getenv('GROQ_DEFAULT_TEMPERATURE'))
DEFAULT_MAX_TOKENS = int(os.getenv('GROQ_DEFAULT_MAX_TOKENS'))

st.set_page_config(layout="wide")

def main():
    
    st.markdown("<h1 style='text-align: center;'>Groq Prompt Optimizer</h1>", unsafe_allow_html=True)
    
    st.markdown("<h6 style='text-align: center; padding-bottom: 50px;'>App uses Groq's LLM services to instantly optimize prompts.</h6>", unsafe_allow_html=True)
    # col1, col2 = st.columns([1, 3])

    st.sidebar.title("Settings")
    api_key = st.sidebar.text_input("Enter your Groq API key (leave blank to use .env):", type="password")
    
    st.sidebar.markdown("---")
    st.sidebar.info(
        "Note: Your API key is used only for this session and is not stored. "
        "Always keep your API keys confidential."
    )
    st.sidebar.markdown("---")
    
    user_prompt = st.text_area("Enter your prompt:")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        model = st.selectbox("Select Model", [
            "llama-3.3-70b-versatile",
            "llama3-groq-8b-8192-tool-use-preview",
            "llama3-70b-8192",
            "llama3-8b-8192"
        ], index=0)
    with col2:
        temperature = st.slider("Temperature", 0.0, 1.0, DEFAULT_TEMPERATURE, 0.1)
    with col3:
        max_tokens = st.number_input("Max Tokens", 1, 32768, DEFAULT_MAX_TOKENS)    
        
    if st.button("Optimize"):
        if not user_prompt:
            st.error("Please enter a prompt.")
            return
        try:
            optimizer = PromptOptimizer(
            model=model, 
            groq_client=GroqClient(api_key=api_key) if api_key else None
        )
            optimized_prompt = optimizer.optimize_prompt(user_prompt)
            st.success("Optimized Prompt:")
            st.code(optimized_prompt, language="markdown")
        
                
        except Exception as e:
            st.error(f"Error: {e}")
                
    st.sidebar.markdown("---")
    st.sidebar.markdown("Created by ChusDeBoss")

if __name__ == "__main__":
    if 'copied_text' not in st.session_state:
        st.session_state.copied_text = ''
    main()
