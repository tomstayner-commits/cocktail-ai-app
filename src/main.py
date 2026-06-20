from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Welcome to Tom's Cocktail API"
    }

@app.get("/cocktails")
def get_cocktails():
    return [
        {
            "id": 1,
            "name": "Old Fashioned",
            "spirit": "Bourbon"
        },
        {
            "id": 2,
            "name": "Negroni",
            "spirit": "Gin"
        }
    ]