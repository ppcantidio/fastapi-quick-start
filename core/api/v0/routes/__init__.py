from fastapi import FastAPI

from core.api.v0.routes.health_routes_v0 import healt_router_v0


def add_routers_v0(app: FastAPI):
    app.include_router(healt_router_v0)
