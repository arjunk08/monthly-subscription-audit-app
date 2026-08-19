import os 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

database=os.getenv("DATABASE_URL", "sqlite:///./test.db")

engine=create_engine(
    database,
    pool_pre_ping=True
)

SessionLocal=sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

base=declarative_base()