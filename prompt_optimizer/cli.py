import argparse
if __name__ == '__main__':
    from prompt_optimizer.prompt_optimizer import PromptOptimizer
else:
    from .prompt_optimizer import PromptOptimizer

def main():
    parser = argparse.ArgumentParser(description="Optimize user prompts using Groq LLM.")
    parser.add_argument("prompt", type=str, help="The prompt to optimize.")
    parser.add_argument("--model", type=str, default="llama-3.3-70b-versatile", help="The Groq model to use.")

    args = parser.parse_args()

    try:
        optimizer = PromptOptimizer(model=args.model)
        optimized_prompt = optimizer.optimize_prompt(args.prompt)
        print("Optimized Prompt:")
        print(optimized_prompt)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
