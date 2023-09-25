from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()
engine = create_engine("sqlite:///sqlite.db", echo=False)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

    def __init__(self, name, email):
        self.name = name
        self.email = email


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String)
    body = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User")

    def __init__(self, title, body, user_id):
        self.title = title
        self.body = body
        self.user_id = user_id


def add_question(title, body, user_id):
    Session = sessionmaker(bind=engine)
    session = Session()

    question = Question(title=title, body=body, user_id=user_id)

    session.add(question)
    session.commit()

    return "Question added successfully"


Base.metadata.create_all(engine)
