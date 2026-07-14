# Engineering Log

## 2026-07-14

### Implemented
- Added a health endpoint at `/health` for basic service monitoring.
- Moved cocktail CRUD logic behind the service layer to improve maintainability.
- Added regression tests covering the health endpoint and the cocktail collection route.
- Documented the evolving architecture and roadmap in the architecture docs.

### Notes
- The current application remains locally oriented while the long-term target architecture is AWS-serverless.
- Future work should focus on configuration management, error handling, and deployment automation.
