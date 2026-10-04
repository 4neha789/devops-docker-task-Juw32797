# DevOps Docker Task

## Student Information
- Name: Neha Maqbool
- Student ID: Juw 32797
- Course: DevOps

## Application Description
This project contains a simple Flask web application that displays student details and confirms that it is running inside a Docker container. It is designed to demonstrate the full DevOps workflow from source code to Docker image creation and deployment.

## Technologies Used
- Git
- GitHub
- Docker
- Docker Hub
- Python
- Flask

## Dockerfile Explanation
The Dockerfile used for this project is:

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 3000
CMD ["python", "app.py"]
```

Explanation of each instruction:
- FROM python:3.12-slim: Selects the base image for the container.
- WORKDIR /app: Sets the working directory inside the container.
- COPY requirements.txt .: Copies the requirements file into the container.
- RUN pip install --no-cache-dir -r requirements.txt: Installs app dependencies.
- COPY . .: Copies the application code into the container.
- EXPOSE 3000: Declares the port used by the web application.
- CMD ["python", "app.py"]: Starts the Flask application when the container runs.

## Docker Commands
```bash
docker build -t devops-task:v1 .
docker run -d -p 3000:3000 --name devops-task devops-task:v1
docker ps
docker logs devops-task
docker inspect devops-task
docker tag devops-task <dockerhub-username>/devops-task:v1
docker push <dockerhub-username>/devops-task:v1
docker pull <dockerhub-username>/devops-task:v1
```

## Docker Hub
Docker Hub Repository:
https://hub.docker.com/r/<dockerhub-username>/devops-task

## How to Run
```bash
docker pull <dockerhub-username>/devops-task:v1
docker run -d -p 3000:3000 --name devops-task <dockerhub-username>/devops-task:v1
```

Then open the browser at:
http://localhost:3000

## Screenshots
The project should include screenshots for:
1. GitHub repository
2. Dockerfile
3. .dockerignore
4. Successful docker build
5. Running container using docker ps
6. Application running in browser
7. Docker Hub repository
8. Successful docker pull and execution from Docker Hub

## GitHub Repository
GitHub URL:
https://github.com/<username>/devops-docker-task-<student-id>

## Submission Notes
This task demonstrates the complete workflow:
GitHub -> Docker Build -> Docker Image -> Docker Hub -> Docker Pull -> Docker Container -> Running Application
