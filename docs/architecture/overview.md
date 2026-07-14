# Architecture Overview

This document gives the high-level shape of the Cocktail AI App and points to the more detailed architecture pages in this folder.

## Current Scope

The project is currently a Python FastAPI application with:
- a small HTTP API for cocktail data
- HTML views served from the same application
- a service layer that separates business logic from route handlers
- DynamoDB as the persistence layer

## Architectural Intent

The long-term direction is a cloud-native, AWS-based application with AI-assisted features. The current implementation is intentionally small and local-first so the core architecture can evolve without unnecessary complexity.

## Main Components

- FastAPI application: request handling and HTML rendering
- Service layer: cocktail CRUD operations and business logic
- DynamoDB table: persistent storage for cocktail records
- Logging: structured application logging for local operations

## Documentation Map

- Overview: this file
- aws.md: current AWS and storage considerations
- deployment.md: deployment posture and next steps
- data-model.md: data shape and persistence model
- roadmap.md: planned evolution
- engineering-log.md: implementation history and decisions