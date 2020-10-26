from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

class SessionAndEngine:

    session = None
    engine = None

    def __init__(self):
        self.engine = create_engine('sqlite:///restEasy.db', echo=None)
        self.session = sessionmaker(bind=self.engine)

    def getEngine(self):
        return self.engine

    def getSession(self):
        return self.session()
