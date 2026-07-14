# Cocktail AI App

A cocktail recipe application built with Python, FastAPI, and AWS DynamoDB. It currently runs locally and connects to a configured DynamoDB table.

Cocktail AI App is a Cloud & AI Engineering portfolio project focused on production-quality engineering practices while evolving toward a cloud-native, AI-powered cocktail companion.

## Current Capabilities

- FastAPI JSON API and server-rendered HTML views
- Cocktail CRUD operations backed by DynamoDB
- Service-layer separation, health monitoring, structured logging, and regression tests
- Interactive Swagger API documentation

## Getting Started

From the project root, activate a virtual environment, install dependencies, copy the environment template, and start Uvicorn:

```powershell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
uvicorn src.main:app --reload
```

The application is available at `http://localhost:8000`; Swagger UI is available at `http://localhost:8000/docs`.

For prerequisites, AWS credentials, environment configuration, and available endpoints, see the [local setup guide](docs/setup.md).

## Documentation

- [Local setup](docs/setup.md)
- [Product roadmap](docs/roadmap.md)
- [Architecture overview](docs/architecture/overview.md)
- [AWS architecture](docs/architecture/aws.md)
- [Deployment](docs/architecture/deployment.md)
- [Data model](docs/architecture/data-model.md)
- [Coding standards](docs/development/coding-standards.md)
- [Engineering log](docs/development/engineering-log.md)

Repository engineering governance is defined in [AGENTS.md](AGENTS.md).
