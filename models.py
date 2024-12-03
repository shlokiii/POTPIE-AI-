from pydantic import BaseModel

class AnalyzePRRequest(BaseModel):
    repo_url: str            # GitHub repository URL
    pr_number: int           # Pull request number
    github_token: str = None # Optional GitHub token
    language: str = "python" # Programming language (default: Python)