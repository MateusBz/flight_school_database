from engine_database import create_db
from models import Base


if __name__ == '__main__':

    url = 'sqlite:///school.sqlite'

    engine = create_db(url)
    Base.metadata.create_all(engine)



