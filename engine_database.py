from sqlalchemy import create_engine


def execute_query(engine, query):
    return engine.execute(query)


def create_database(url, queries):
    engine = create_engine(url)
    for query in queries:
        execute_query(engine, query)


if __name__ == '__main__':

    url = 'sqlite:///school.sqlite'

    with open('queries.txt', 'r') as f:
        lines = f.readlines()

    queries = [line.replace(';\n', ';') for line in lines]

    database = create_database(url, queries)
