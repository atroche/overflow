import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import main

engine = create_engine("sqlite:///sqlite.db")
Session = sessionmaker(bind=engine)
session = Session()


def test_add_question():
    try:
        user = main.User(name="John Doe", email="johndoe@example.com")
        session.add(user)
        session.commit()

        main.add_question(
            "What's the meaning of life?", "This is a philosophical question.", user.id
        )

        questions_for_user = (
            session.query(main.Question).filter(main.Question.user_id == user.id).all()
        )
        assert len(questions_for_user) > 0

        for question in questions_for_user:
            assert question.title == "What's the meaning of life?"
    except Exception as e:
        assert False, str(e)
