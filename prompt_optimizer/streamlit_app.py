import streamlit as st
from prompt_optimizer.prompt_optimizer import PromptOptimizer

def main():
    st.title("Groq Prompt Optimizer")

    api_key = st.text_input("Enter your Groq API key (leave blank to use .env):", type="password")
    user_prompt = st.text_area("Enter your prompt:")
    model = st.selectbox("Select Groq Model:", ["mixtral-8x7b-32768", "llama2-70b-4096"])
    
    if st.button("Optimize"):
        if not user_prompt:
            st.error("Please enter a prompt.")
            return
        try:
            optimizer = PromptOptimizer(model=model)
            if api_key:
                optimizer.groq_client.client.api_key = api_key
            optimized_prompt = optimizer.optimize_prompt(user_prompt)
            st.success("Optimized Prompt:")
            st.write(optimized_prompt)
        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
