from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import settings

engine = create_engine(f'sqlite:///{settings.URL_DB}/signal.sqlite')
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

SQLALCHEMY_TRACK_MODIFICATIONS = False

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
