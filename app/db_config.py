import os

from sqlalchemy import create_engine, text

# Set DATABASE_URL to point at a different PostgreSQL instance.
DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "postgresql+psycopg2://dadb:123456789qQ@localhost:5432/DSS",
)


def get_db_engine():
    return create_engine(DATABASE_URL)


if __name__ == "__main__":
    engine = get_db_engine()
    with engine.connect() as conn:
        result = conn.execute(text("SELECT NOW();"))
        print("current time:", result.fetchone()[0])
