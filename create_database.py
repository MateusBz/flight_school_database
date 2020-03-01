from sqlalchemy import create_engine
from utils import queries, execute_query


def createdb(url, script_path):
    engine = create_engine(url, echo=True)
    for query in queries(script_path):
        engine.execute(query)


if __name__ == '__main__':
    url = 'sqlite:///school.sqlite'
    script_path = 'createdb.sql'
    createdb(url, script_path)
