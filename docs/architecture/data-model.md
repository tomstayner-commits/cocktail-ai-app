# Data Model

The current data model is intentionally minimal.

## Cocktail Record

Each cocktail is stored as a DynamoDB item with the following fields:

- id: integer primary identifier
- name: string
- spirit: string
- ingredients: list of strings

## Notes

The model reflects the current implementation and is designed to support simple CRUD operations through the API.

## Future Extension

The model can evolve to include fields such as:
- description
- image URL
- tags
- ratings
- pairing suggestions