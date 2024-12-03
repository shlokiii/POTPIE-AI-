from unittest.mock import patch
from app.tasks import analyze_code_task

def test_analyze_pr_endpoint(client):
    with patch("app.tasks.analyze_code_task.apply_async") as mock_task:
        mock_task.return_value.id = "fake-task-id"
        response = client.post("/analyze-pr", json={
            "repo_url": "https://github.com/example/repo",
            "pr_number": 1,
            "github_token": "fake-token",
            "language": "python"
        })
        assert response.status_code == 200
        assert response.json() == {"task_id": "fake-task-id", "status": "submitted"}