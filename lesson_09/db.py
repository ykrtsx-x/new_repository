from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URL = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine)
