from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker




engine = create_engine("sqlite+pysqlite:///./car_catalog.db",connect_args={"check_same_thread":False}, echo=True)

SessionLocal = sessionmaker(bind=engine, autoflush=False)

