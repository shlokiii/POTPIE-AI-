#Potpie AI: Pull Request Analysis API#

Potpie AI internship assignment is a web application that uses OpenAI’s GPT-4 model to analyze GitHub pull requests for code style, potential bugs, performance improvements, and adherence to best practices. This project is designed with FastAPI, Celery, and Redis for scalable task execution.

Table of Contents

	•	Features
	•	Project Setup Instructions
	•	API Documentation
	•	Design Decisions
	•	Future Improvements
	•	Testing Instructions

 Features

 •	Analyze pull requests using OpenAI GPT-4.
 •	Task queuing and background processing with Celery and Redis.
 •	API endpoints for submitting tasks and retrieving task statuses.
 •	Scalable and modular design.


Project Setup Instructions

Prerequisites

	1.	Environment: Python 3.9+ and Docker installed.
	2.	API Key: OpenAI API key to access GPT-4.

Steps
	1.	Clone the repository:
       git clone <repository-url>
       cd <repository-folder>

  2.	Setup environment variables:
      Create a .env file in the root directory with the following content:
    	 OPENAI_API_KEY=your_openai_api_key_here
       REDIS_URL=redis://redis:6379/0

  3.	Install dependencies:
      Create a virtual environment and install Python dependencies:
    	 python3 -m venv .venv
       source .venv/bin/activate
       pip install -r requirements.txt

  4.	Run the application using Docker:
      Build and start the containers:
    	 docker-compose up --build

  5.	Access the API:
      Open your browser and navigate to:




  ## API Documentation

### Endpoints

#### 1. `POST /analyze-pr`
- **Description**: Submits a pull request for analysis.
- **Request Body**:
    ```json
    {
        "repo_url": "https://github.com/<username>/<repository>",
        "pr_number": 1,
        "github_token": "<github_personal_access_token>",
        "language": "python"
    }
    ```
- **Response**:
    ```json
    {
        "task_id": "<task-id>",
        "status": "submitted"
    }
    ```

#### 2. `GET /status/{task_id}`
- **Description**: Retrieves the status of a submitted task.
- **Response**:
    - When the task is pending:
      ```json
      {
          "task_id": "<task-id>",
          "status": "pending"
      }
      ```
    - When completed:
      ```json
      {
          "task_id": "<task-id>",
          "status": "completed",
          "result": {
              "style_issues": [...],
              "bugs": [...],
              "performance_improvements": [...],
              "best_practices": [...]
          }
      }
      ```

---

## Design Decisions

1. **FastAPI**:
   - Chosen for its simplicity, async support, and automatic generation of API documentation via OpenAPI.

2. **Celery and Redis**:
   - Celery enables task queuing for background task execution.
   - Redis acts as a message broker and a result backend, ensuring fast and reliable task processing.

3. **OpenAI Integration**:
   - The project leverages OpenAI's GPT-4 model for its natural language processing capabilities, making it ideal for code analysis and generating actionable feedback.

4. **Modular Design**:
   - The project is designed to be modular and scalable, ensuring easy integration of additional features or updates.

5. **Docker**:
   - The entire application is containerized using Docker, simplifying deployment and ensuring a consistent environment across different systems.

---

## Testing Instructions

### Manual Testing

1. **Start the Application**:
   - Run the application with Docker Compose:
     ```bash
     docker-compose up --build
     ```

2. **Access Swagger UI**:
   - Open `http://localhost:8000/docs` in your browser.

3. **Submit a Pull Request Analysis**:
   - Use the `POST /analyze-pr` endpoint with the following request body:
     ```json
     {
         "repo_url": "https://github.com/example/repo",
         "pr_number": 1,
         "github_token": "your_github_token",
         "language": "python"
     }
     ```

4. **Check Task Status**:
   - Copy the `task_id` from the response.
   - Use the `GET /status/{task_id}` endpoint to check the status and retrieve results.

5. **Verify Logs**:
   - Check logs for debugging:
     ```bash
     docker logs <container-name>
     ```

### Debugging Redis Keys

1. **Access Redis CLI**:
   - Execute:
     ```bash
     docker exec -it <redis-container-name> redis-cli
     ```

2. **Check Task Metadata**:
   - View all keys:
     ```bash
     keys *
     ```
   - Retrieve a specific key:
     ```bash
     get <task-key>
     ```

### Automated Testing

1. **Install Testing Framework**:
   - Ensure `pytest` is installed:
     ```bash
     pip install pytest
     ```

2. **Run Tests**:
   - Execute all test cases in the `tests` directory:
     ```bash
     pytest
     ```

3. **Add New Tests**:
   - Create additional test cases for API endpoints in the `tests` directory.
