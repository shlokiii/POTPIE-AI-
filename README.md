Potpie AI: Pull Request Analysis API

Potpie AI internship assignment is a web application that uses OpenAI’s GPT-4 model to analyze GitHub pull requests for code style, potential bugs, performance improvements, and adherence to best practices. This project is designed with FastAPI, Celery, and Redis for scalable task execution.

Table of Contents

	•	Features
	•	Project Setup Instructions
	•	API Documentation
	•	Design Decisions
	•	Testing Instructions
	•	Test Summary Report
	•	Bonus Points
 		

 Features

	•	Analyze pull requests using OpenAI GPT-4.
	•	Task queuing and background processing with Celery and Redis.
	•	API endpoints for submitting tasks and retrieving task statuses.
	•	Scalable and modular design.



Project Setup Instructions

 Prerequisites

	1.	Environment: Ensure Python 3.9+ and Docker are installed.
	2.	API Key: Obtain an OpenAI API key to access GPT-4.

 Steps
 
	1.	Clone the Repository:
 		git clone <repository-url>
 		cd <repository-folder>

 	2.	Setup Environment Variables:
		Create a .env file in the root directory with the following content:
		OPENAI_API_KEY=your_openai_api_key_here
		REDIS_URL=redis://redis:6379/0

	3.	Install Dependencies:
		Create a virtual environment and install the required Python dependencies:
		python3 -m venv .venv
		source .venv/bin/activate
		pip install -r requirements.txt

	4.	Run the Application Using Docker:
		Build and start the containers:
		docker-compose up --build


	5.	Access the API:
		Open your browser and navigate to:
		http://localhost:8000/docs


API Documentation

 Endpoints

        1. 	POST /analyze-pr

		• Description: Submits a pull request for analysis.
		• Request Body:
			{
    				"repo_url": "https://github.com/<username>/<repository>",
    				"pr_number": 1,
    				"github_token": "<github_personal_access_token>",
    				"language": "python"
			}

	•	Response:
			{
    				"task_id": "<task-id>",
    				"status": "submitted"
			}
 
	2. GET /status/{task_id}

		•	Description: Retrieves the status of a submitted task.
		•	Response:
		•	When the task is pending:
			{
    				"task_id": "<task-id>",
    				"status": "pending"
			}
		•	When completed:
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








Design Decisions

	1.	FastAPI:
		• Selected for its simplicity, async support, and automatic generation of API documentation via OpenAPI.
	2.	Celery and Redis:
		• Celery enables task queuing for background task execution.
		• Redis acts as a message broker and a result backend, ensuring fast and reliable task processing.
	3.	OpenAI Integration:
		• GPT-4 model is leveraged for its natural language processing capabilities, making it ideal for code analysis.
	4.	Modular Design:
		• Designed to be modular and scalable, enabling easy integration of new features.
	5.	Docker:
		• Containerized the application to ensure a consistent environment across systems and simplify deployment.






Testing Instructions

 Manual Testing

	1.	Start the Application:
		docker-compose up --build

	2.	Access Swagger UI:
		Open http://localhost:8000/docs in your browser.
	3.	Submit a Pull Request Analysis:
		Use the POST /analyze-pr endpoint with the following request body:
		{
    			"repo_url": "https://github.com/example/repo",
    			"pr_number": 1,
    			"github_token": "your_github_token",
    			"language": "python"
		}
	4.	Check Task Status:
		Copy the task_id from the response and use the GET /status/{task_id} endpoint to check the status and retrieve results.
	5.	Debugging Redis Keys:
		• Access Redis CLI:
		docker exec -it <redis-container-name> redis-cli
		• View keys:
		keys *
		• Retrieve a key:
		get <task-key>




Automated Testing

	1.	Install Testing Framework:
		Ensure pytest is installed:
		pip install pytest
	2.	Run Tests:
		Execute all test cases in the tests directory:
		pytest
	3.	Results:
		• All tests were executed and passed successfully, confirming the API’s functionality and error handling.





 

Test Summary Report

 Summary

 All unit tests and integration tests were successfully executed using pytest. The test cases covered:
	1.	API endpoint functionality (/analyze-pr and /status/{task_id}).
	2.	Background task processing with Celery.
	3.	Integration with Redis for task management and status retrieval.

 Results

	•	Total Tests: 3
	•	Passed: 3
	•	Failed: 0
	•	Warning: 1 (non-critical configuration warning).

 How to Run Tests

	1.	Activate the virtual environment:
		source .venv/bin/activate
	2.	Run the pytest command:
		pytest
	3.	View the test results in the terminal.








 

Bonus Points

	•	Live Deployment: The project is deployed on Render for live testing and demonstration of API functionality. Access the live API here: https://potpie-ai-3.onrender.com
	•	Docker Configuration: The entire application is containerized with a robust Dockerfile and docker-compose.yml, enabling seamless development and deployment across environments.
	•	Result Caching System: Redis is used as a result backend to cache and manage task statuses efficiently, enhancing performance and reliability.
	•	Structured Logging: Logs from FastAPI, Celery, and Redis are structured and accessible for debugging and monitoring.
	•	Multi-language Support: The project is modular and designed to support multiple programming languages for pull request analysis (e.g., Python, JavaScript).
	•	Rate Limiting: The application enforces proper rate limiting for GPT-4 requests via OpenAI API to handle heavy loads gracefully.
	•	GitHub Webhook Support: The design can be extended to integrate GitHub webhooks for real-time pull request analysis triggers.









































  

  
