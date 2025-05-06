from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "postgresql://neondb_owner:npg_S82BzsldfLTy@ep-sparkling-band-a4w4foaq-pooler.us-east-1.aws.neon.tech/neondb?sslmode=require"

engine = create_engine(DATABASE_URL, echo=True,)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
