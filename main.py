from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models.models import Base
from app.database import engine
from app.api.routers.car_routers import router as router_car

@asynccontextmanager
async def lifespan(app:FastAPI):
  Base.metadata.create_all(bind=engine)
  yield

app = FastAPI(title="Car Catalog  API", lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router_car)