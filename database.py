import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


'''
sudo -i -u postgres
psql
CREATE USER docker_pg WITH SUPERUSER PASSWORD 'helloworld';
CREATE DATABASE flaskapp_db;
'''

user = "docker_pg"
pwd = "helloworld"
db = "flaskapp_db"
host = '127.0.0.1'
port = '5432'
engine = create_engine('postgresql+psycopg2://%s:%s@%s:%s/%s' % (user, pwd, host, port, db)) 
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import models
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()