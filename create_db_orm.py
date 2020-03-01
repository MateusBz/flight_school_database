from sqlalchemy import create_engine
from models import Base


if __name__ == '__main__':
    url = 'sqlite:///school.sqlite'
    engine = create_engine(url)
    Base.metadata.create_all(engine)
