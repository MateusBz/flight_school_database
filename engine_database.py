from sqlalchemy import create_engine


def create_db(url):
    db = create_engine(url, echo=True)
    return db


def execute_query(db, query):
    return db.execute(query)
