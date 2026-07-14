# Service Layer

## Current Structure

The application uses a small service layer to separate business logic from the FastAPI route handlers.

### Responsibilities
- Retrieve cocktails from the DynamoDB table.
- Validate whether a cocktail exists before update or delete operations.
- Keep route handlers focused on HTTP concerns and response shaping.

### Key Modules
- [src/services/cocktail_service.py](../../src/services/cocktail_service.py): Contains cocktail CRUD logic.
- [src/main.py](../../src/main.py): Hosts the FastAPI routes and HTML views.

## Future Improvements
- Add richer validation and domain rules.
- Introduce service interfaces for easier testing.
- Expand service coverage for AI-assisted recommendation flows.
