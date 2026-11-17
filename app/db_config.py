import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine, text

# Reads DATABASE_URL from app/.env (copy .env.example) or the environment.
load_dotenv(Path(__file__).parent / ".env")


def get_db_engine():
    url = os.environ.get("DATABASE_URL")
    if not url:
        raise RuntimeError(
            "DATABASE_URL is not set. Copy app/.env.example to app/.env and fill it in."
        )
    return create_engine(url)


if __name__ == "__main__":
    engine = get_db_engine()
    with engine.connect() as conn:
        result = conn.execute(text("SELECT NOW();"))
        print("current time:", result.fetchone()[0])
