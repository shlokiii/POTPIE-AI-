from unittest.mock import patch
from app.tasks import analyze_code_task

@patch("app.tasks.analyze_code_with_gpt4")
def test_analyze_code_task(mock_analyze):
    # Mock the response of the analyze_code_with_gpt4 function
    mock_analyze.return_value = {"status": "success"}

    # Prepare request data
    request_data = {
        "repo_url": "https://github.com/example/repo",
        "pr_number": 1,
        "language": "python"
    }

    # Call the task
    result = analyze_code_task(request_data)

    # Assert the result matches the mock
    assert result == {"status": "success"}
    mock_analyze.assert_called_once_with(
        repo_url="https://github.com/example/repo",
        pr_number=1,
        language="python"
    )