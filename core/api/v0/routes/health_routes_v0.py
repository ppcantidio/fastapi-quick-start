from datetime import datetime

from fastapi import APIRouter, status

from core.adapters.logger_adapter import LoggerAdapter
from core.api.v0.response_models.generic_response_v0 import GenericResponseV0
from core.api.v0.response_models.health_response_v0 import HealthResponseV0

healt_router_v0 = APIRouter(prefix="/v0/health")
logger = LoggerAdapter.get_logger(__name__)


@healt_router_v0.get(
    "/",
    name="Health check",
    response_model=GenericResponseV0[HealthResponseV0],
    status_code=status.HTTP_200_OK,
)
async def health_check():
    logger.info("Health check V0")

    return GenericResponseV0[HealthResponseV0](
        message="Health check",
        data=HealthResponseV0(time=datetime.now(), status="OK", api_version="v0"),
    )
