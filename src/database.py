from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "mssql+pyodbc://@INFERIOROS\\SQL_SERVER/fastapi?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server",
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
