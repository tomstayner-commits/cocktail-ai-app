# Deployment

The application is currently deployed locally for development.

## Current Deployment Model

- Run the FastAPI app with Uvicorn from the project root.
- Configure environment variables before launching the service.
- Use the local DynamoDB-compatible environment already expected by the application.

## Operational Notes

- Logging is written to the local logs directory.
- Health checks are available through the /health endpoint.
- The application is not yet packaged for cloud deployment.

## Next Step

The next deployment milestone is to move the service into a hosted AWS environment while preserving the existing FastAPI structure and service layer.