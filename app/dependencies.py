from app.database import SessionLocal
from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session

def get_session():
  session = SessionLocal()
  try:
    yield session
  finally:
    session.close()


SessionDep =Annotated[Session, Depends(get_session)]