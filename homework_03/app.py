from fastapi import FastAPI

app = FastAPI()


@app.get("/ping/", status_code=200)
def view():
    return {"message": "pong"}