# Django CI/CD Project

This repository contains a Django project set up for CI/CD workflows. It includes a basic Django application structure, Docker support, and testing configuration.

## Project Structure

- `app/` - Main Django app with models, views, and tests
- `core/` - Project settings and configuration
- `manage.py` - Django management script
- `Dockerfile` and `docker-compose.yml` - Containerization setup
- `requirements.txt` and `requirements-dev.txt` - Python dependencies
- `Makefile` - Common development commands

## Getting Started

### Prerequisites
- Python 3.8+
- Docker & Docker Compose (optional, for containerized development)
- pip (Python package manager)

### Setup (Local)
1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```
3. Run migrations:
   ```bash
   python manage.py migrate
   ```
4. Start the development server:
   ```bash
   python manage.py runserver
   ```

### Running with Docker
1. Build and start the containers:
   ```bash
   docker-compose up --build
   ```
2. The app will be available at `http://localhost:8000`

### Running Tests
```bash
pytest
```

## CI/CD
This project is ready for integration with CI/CD pipelines. You can use GitHub Actions, GitLab CI, or other tools to automate testing and deployment.

