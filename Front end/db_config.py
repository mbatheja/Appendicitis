from sqlalchemy import create_engine,text

def get_db_engine():
    engine = create_engine(
        "postgresql+psycopg2://dadb:123456789qQ@localhost:5432/DSS"
    )
    return engine

if __name__ == "__main__":
    engine = get_db_engine()
    with engine.connect() as conn:
        result = conn.execute(text("SELECT NOW();"))
        print("current time：", result.fetchone()[0])

