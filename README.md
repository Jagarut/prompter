# Groq Prompt Optimizer

This Python utility uses the Groq LLM provider service to instantly refactor and optimize user prompts. It is designed to improve the effectiveness of prompts when working with large language models.

## Features

- **Prompt Optimization:** Rephrases and optimizes user prompts using Groq's LLM services.
- **Configurable:** Uses environment variables or a `.env` file for configuration.
- **Modular Design:** Can be used as a module in other Python scripts or run from the command line.
- **Groq Models:** Supports various Groq models and customizable parameters.
- **Streamlit App:** Includes a Streamlit web app for easy demonstration and testing.
- **API Key Input:** Streamlit app supports API key input for use in hosted environments.
- **Optimization Strategies:** Supports different optimization strategies like concise, detailed, and default.

## Core Components

1.  **`groq_client.py`:** Handles communication with the Groq LLM API.
2.  **`prompt_optimizer.py`:** Contains the core logic for rephrasing and optimizing user prompts.
3.  **`cli.py`:** Provides a command-line interface for the utility.
4.  **`streamlit_app.py`:** Provides a web interface for demonstration and testing.
5.  **`.env`:** Stores the Groq API key and other configuration settings.

## Setup

1.  **Install Dependencies:**
    ```bash
    pip install -r requirements.in
    ```
2.  **Set up your `.env` file:**
    Create a `.env` file in the root directory and add your Groq API key:
    ```
    GROQ_API_KEY=your_groq_api_key
    ```
    Replace `your_groq_api_key` with your actual Groq API key.

## Usage

### Command-Line Interface

To use the command-line interface, run:

```bash
python prompt_optimizer/cli.py "Your prompt here" --model llama3-8b-8192
```

Replace `"Your prompt here"` with the prompt you want to optimize and `--model llama3-8b-8192` with the desired Groq model.

### Streamlit Web App

To use the Streamlit web app, run:

```bash
streamlit run prompt_optimizer/streamlit_app.py
```

Then, open the provided URL in your browser.

## Optimization Strategies

The `prompt_optimizer.py` supports different optimization strategies:

- **default:** Rephrases and optimizes the prompt to be more effective for LLMs.
- **concise:** Rephrases the prompt to be more concise and to the point.
- **detailed:** Rephrases the prompt to be more detailed and explicit.

You can select the strategy in the `streamlit_app.py` or by modifying the `PromptOptimizer` class in `prompt_optimizer.py`.

## Example File Structure

```
prompt_optimizer/
├── groq_client.py
├── prompt_optimizer.py
├── cli.py
├── streamlit_app.py
├── .env
└── README.md
requirements.in
```

## Contributing

Feel free to contribute to this project by submitting pull requests.

## License

This project is licensed under the MIT License.

## Acknowledgments

- Thanks to Groq for providing the LLM services used in this utility.

- Created by ChusDeBoss.
