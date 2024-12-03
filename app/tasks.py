from celery import Celery
from app.ai_agent import analyze_code_with_gpt4

celery_app = Celery(
    "tasks",
    broker="redis://redis:6379/0",  # Redis as the message broker
    backend="redis://redis:6379/0"  # Redis as the result backend
)

@celery_app.task(bind=True)
def analyze_code_task(self, request_data):
    """
    Celery task to analyze code using GPT-4.
    """
    try:
        return analyze_code_with_gpt4(
            repo_url=request_data["repo_url"],
            pr_number=request_data["pr_number"],
            language=request_data.get("language", "python"),
        )
    except Exception as e:
        self.update_state(state="FAILURE", meta=str(e))
        raise