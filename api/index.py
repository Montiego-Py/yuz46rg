from fastapi import FastAPI

app = FastAPI()

@app.get("/api")
def root():
    return {"message": "Python API çalışıyor 🚀"}
