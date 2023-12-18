from fastapi import FastAPI

from app.api.router import router_api

app = FastAPI(
    title='Сurrencies',
    version='0.1.0',
    docs_url='/api/docs',
    openapi_url='/api/v1/openapi.json',
)

app.include_router(router_api)
