import streamlit as st
from prompt_optimizer import PromptOptimizer
from groq_client import GroqClient

st.set_page_config(layout="wide")

def main():
    st.markdown(
        """
        <style>
            .main {
                padding-bottom: 50px;
                background-color: #f0f2f6;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("<h1 style='text-align: center;'>Groq Prompt Optimizer</h1>", unsafe_allow_html=True)

    st.markdown(
        """
        <style>
            [data-testid="column"]:nth-child(1) {
                background-color: #e0e0e0;
                padding: 10px;
            }
            [data-testid="column"]:nth-child(2) {
                background-color: #f0f0f0;
                padding: 10px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([1, 3])

    with col1:
        api_key = st.text_input("Enter your Groq API key (leave blank to use .env):", type="password")
    
    with col2:
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
