# Local Setup

This document is the authoritative guide for running Cocktail AI App locally. For a concise quick start, see the [README](../README.md).

## Prerequisites

- Python 3.14+
- A virtual environment
- AWS credentials available through the standard AWS credential provider chain
- Access to the DynamoDB table configured for the application

## Install and Run

1. Create and activate a virtual environment.
2. Install dependencies with `pip install -r requirements.txt`.
3. Copy the environment template with `Copy-Item .env.example .env` on Windows or `cp .env.example .env` on Linux or macOS.
4. Set the required variables in `.env`:

   ```text
   AWS_REGION=ap-southeast-2
   TABLE_NAME=Cocktails
   ```

   `LOG_LEVEL` may remain in the template for future use, but the current application logs at `INFO` and does not read it.
5. From the project root, start the application with `uvicorn src.main:app --reload`.

## Local Endpoints

- `/` — HTML landing page
- `/health` — basic health check
- `/docs` — Swagger UI
- `/favicon.ico` — browser favicon

## Configuration and Security

Connection settings are supplied through environment variables and are not stored in the repository. Do not commit `.env`, AWS credentials, API keys, or passwords.

The application uses the standard AWS credential provider chain to access DynamoDB and does not currently configure a local DynamoDB endpoint.

See [deployment notes](architecture/deployment.md) for the current operating model and [coding standards](development/coding-standards.md) for delivery expectations.
