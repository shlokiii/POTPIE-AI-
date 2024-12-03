import os
import requests  # Ensure both are imported
def analyze_code_with_gpt4(repo_url, pr_number, language):
    """
    Perform AI-based code analysis using GPT-3.5 Turbo via the OpenAI API.
    """
    # Get the OpenAI API key from the environment
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return {"error": "OpenAI API key is not set in the environment."}

    # Construct the prompt
    prompt = f"""
    You are an AI code review assistant. Analyze the code from:
    - Repository: {repo_url}
    - Pull Request Number: {pr_number}
    - Programming Language: {language}

    Provide feedback on:
    1. Style issues.
    2. Potential bugs.
    3. Performance improvements.
    4. Best practices.

    Respond in JSON format.
    """

    # Make a POST request to OpenAI API
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    data = {
        "model": "gpt-3.5-turbo",  # Update to the chosen model
        "messages": [{"role": "system", "content": prompt}],
        "max_tokens": 500,
    }

    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions", headers=headers, json=data
        )
        response.raise_for_status()  # Raise an error if the request fails
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Request failed: {e}"}