"""
This module implements a Streamlit web application for optimizing prompts using Groq's LLM services.
"""
import os
import streamlit as st
from prompt_optimizer import PromptOptimizer
from groq_client import GroqClient
from dotenv import load_dotenv

load_dotenv()

DEFAULT_TEMPERATURE = float(os.getenv('GROQ_DEFAULT_TEMPERATURE'))
DEFAULT_MAX_TOKENS = int(os.getenv('GROQ_DEFAULT_MAX_TOKENS'))

st.set_page_config(layout="wide")

def main():
    """
    Main function to set up the Streamlit app and handle user interactions.
    """
    
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
    
    strategy = st.sidebar.selectbox("Select Strategy", ["default", "concise", "detailed"], index=0)
    
    user_prompt = st.text_area("Enter your prompt:")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        model = st.selectbox("Select Model", [
            "llama3-8b-8192",
            "llama-3.3-70b-versatile",
            "llama3-groq-8b-8192-tool-use-preview",
            "llama3-70b-8192"
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
            groq_client = GroqClient(api_key=api_key) if api_key else None
            optimizer = PromptOptimizer(
                model=model,
                strategy=strategy,
                groq_client=groq_client
            )
            optimized_prompt = optimizer.optimize_prompt(user_prompt, temperature=temperature, max_tokens=max_tokens)
            st.success("Optimized Prompt:")
            with st.expander("Optimized Prompt Details"):
                st.code(optimized_prompt, language="markdown", wrap_lines=True)
                st.text("Additional analysis")
                st.metric("Token count", len(optimized_prompt))
        except Exception as e:
            st.error(f"Error: {e}")
                
    st.sidebar.markdown("---")
    st.sidebar.markdown("Created by ChusDeBoss")

if __name__ == "__main__":
    if 'copied_text' not in st.session_state:
        st.session_state.copied_text = ''
    main()
