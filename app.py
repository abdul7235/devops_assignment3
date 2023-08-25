from fastapi import FastAPI
from models import RequestData

app = FastAPI()


@app.post("/hello_message/")
async def get_data(requestData:RequestData):
    return {"message": f"Hello {requestData.name}"}