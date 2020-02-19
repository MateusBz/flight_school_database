from engine_database import create_db, execute_query

if __name__ == '__main__':

    with open('queries.txt', 'r') as f:
        lines = f.readlines()

    queries = [line.replace(';\n', ';') for line in lines]

    url = 'sqlite:///school.sqlite'

    database = create_db(url)
    for query in queries:
        execute_query(database, query)