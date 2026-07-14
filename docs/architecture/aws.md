# AWS Architecture

The current implementation does not yet use a full AWS deployment. The application is designed to be compatible with an AWS-hosted future state.

## Current State

- The backend uses DynamoDB as its persistence layer.
- Configuration is provided through environment variables such as AWS_REGION and TABLE_NAME.
- The application is currently run locally, but it is structured to fit an AWS-based deployment path.

## Planned Direction

A future version is expected to use:
- AWS Lambda or container-based hosting for the API
- Amazon DynamoDB as the primary data store
- Amazon Cognito for authentication
- Amazon S3 for image storage if media features are introduced

## Architectural Note

The repository keeps the AWS design intentionally lightweight at this stage so the implementation remains easy to evolve.