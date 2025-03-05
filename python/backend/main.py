from fastapi import FastAPI, Request

from backend.api import api_router

app = FastAPI()


@app.middleware("http")
async def dispatch(request: Request, call_next):
    print(request.headers)
    return await call_next(request)


app.include_router(api_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
