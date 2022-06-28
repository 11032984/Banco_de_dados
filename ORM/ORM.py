from sqlalchemy import create_engine, Integer, Column, String
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


db = "postgres"
user = "postgres"
host = "localhost"
password = ""
port = "5432"

engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}", echo = True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Herois(Base):
    __tablename__ = "heroi"

    id = Column(Integer, primary_key = True)
    name = Column(String)
    nivel = Column(Integer)

    def __repr__(self) -> str:
        return self.nome

Base.metadata.create_all(engine)

h1 = Herois(nome = "Zoo", nivel = 16)
h2 = Herois(nome = "Lokre", nivel = 18)

session.add_all([h1, h2])
session.commit()
