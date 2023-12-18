from fastapi import APIRouter

from app.api.v1.router import router_v1

router_api = APIRouter(
    prefix='/api',
)

router_api.include_router(router_v1)
