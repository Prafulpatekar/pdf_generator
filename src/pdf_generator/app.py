import logging

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from starlette import status
from starlette.responses import JSONResponse
from pdf_generator.core.utils.database import init_db


from pdf_generator.routers.users import router as user_router


logger = logging.getLogger(__name__)


app = FastAPI()
app.mount("/static", StaticFiles(directory="public"), name="static")

@app.middleware("http")
async def errors_handling(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"message": "internal server error", "status": False, "error": str(e)}
        )


@app.get("/api/v1/health-check")
def health_check():
    logger.info("Health check API is working")
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "status": True,
            "data": None,
            "message": "Service is working . . .",
        },
    )

@app.on_event("startup")
async def startup_event():
    init_db()

app.include_router(user_router, tags=["User Operation"], prefix="/api/v1/users")
