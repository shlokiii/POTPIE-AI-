import os
from celery import Celery
from app.ai_agent import analyze_code_with_gpt4

# Use environment variable for Redis URL, with a fallback to localhost
redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")

# Initialize Celery with Redis as the broker and backend
celery_app = Celery(
    "tasks",
    broker=redis_url,  # Redis as the message broker
    backend=redis_url  # Redis as the result backend
)

@celery_app.task(bind=True)
def analyze_code_task(self, request_data):
    """
    Celery task to analyze code using GPT-4.
    """
    try:
        # Use the analyze_code_with_gpt4 function to process the task
        return analyze_code_with_gpt4(
            repo_url=request_data["repo_url"],
            pr_number=request_data["pr_number"],
            language=request_data.get("language", "python"),
        )
    except Exception as e:
        # Update task state to FAILURE if an error occurs
        self.update_state(state="FAILURE", meta=str(e))
        raise