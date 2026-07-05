Cocktail AI Application
    How to Run the Application
        Open Visual Studio Code.
        Open the project folder.
        Open a new terminal.

        Activate the virtual environment.

        Windows PowerShell:
        ..venv\Scripts\Activate.ps1

        Windows Command Prompt:
        .venv\Scripts\activate.bat

        Ensure you are in the project root directory.

        Start the application.

        Weeks 1–2 (Command Line Application):
        python src/main.py

        Week 3+ (FastAPI Web Application):
        uvicorn src.main --reload

        Open your browser (Week 3+).

        http://localhost:8000

        FastAPI Interactive API Documentation:

        http://localhost:8000/docs
    Notes
        If using FastAPI, ensure app = FastAPI() exists in src/main.py.
        If using a different project structure (for example app/ instead of src/), adjust the Uvicorn command accordingly.
        Ensure the virtual environment is activated before running the application.