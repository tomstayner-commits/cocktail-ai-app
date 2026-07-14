# Setup

## Prerequisites

- Python 3.14+
- a virtual environment
- access to the DynamoDB table configured by environment variables

## Local setup

1. Create and activate a virtual environment.
2. Install dependencies with `pip install -r requirements.txt`.
3. Create a `.env` file in the project root with at least:
   - `AWS_REGION`
   - `TABLE_NAME`
   - `LOG_LEVEL`
4. Start the app with `uvicorn src.main:app --reload`.

## Useful endpoints

- `/` for the HTML landing page
- `/health` for a basic health check
- `/docs` for the Swagger UI