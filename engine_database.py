from sqlalchemy import create_engine


def create_db(url):
    db = create_engine(url)
    return db


def execute_query(db, query):
    return db.execute(query)
