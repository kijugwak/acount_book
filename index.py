from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    la = "기주"
    # return {"message": "Hello World"}
    return la
