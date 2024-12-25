import streamlit as st
from prompt_optimizer import PromptOptimizer
from prompt_optimizer.groq_client import GroqClient

def main():
    st.title("Groq Prompt Optimizer")

    api_key = st.text_input("Enter your Groq API key (leave blank to use .env):", type="password")
    user_prompt = st.text_area("Enter your prompt:")
    model = st.selectbox("Select Model", [
        "llama-3.3-70b-versatile",
        "llama3-groq-8b-8192-tool-use-preview",
        "llama3-70b-8192",
        "llama3-8b-8192"
    ], index=0)
    
    if st.button("Optimize"):
        if not user_prompt:
            st.error("Please enter a prompt.")
            return
        try:
            optimizer = PromptOptimizer(model=model, groq_client=GroqClient(api_key=api_key) if api_key else None)
            optimized_prompt = optimizer.optimize_prompt(user_prompt)
            st.success("Optimized Prompt:")
            st.write(optimized_prompt)
        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
