def queries(filepath):
    with open(filepath, 'r') as f:
        for line in f:
            yield line.replace(';\n', ';')


def execute_query(engine, query):
    return engine.execute(query)
