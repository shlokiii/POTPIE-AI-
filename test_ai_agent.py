import pytest
from app.ai_agent import analyze_code_with_gpt4

def test_analyze_code_with_gpt4(mocker):
    # Mock the requests.post method
    mocker.patch("app.ai_agent.requests.post", return_value=mocker.Mock(
        status_code=200,
        json=lambda: {"response": "Success"}
    ))
    response = analyze_code_with_gpt4(
        repo_url="https://github.com/example/repo",
        pr_number=1,
        language="python"
    )
    assert response == {"response": "Success"}