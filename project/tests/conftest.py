import pytest
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import config
from project.models import TestUserTable, Base
import pycoingecko
import telebot

COUNT_OF_ROWS = 3


@pytest.fixture(scope='module')
def test_session():
    test_engine = create_engine(config.DATABASE_URI)

    TestSession = sessionmaker(bind=test_engine)
    test_session = TestSession()

    Base.metadata.create_all(test_engine)

    if len(test_session.query(TestUserTable).all()) < COUNT_OF_ROWS:
        test_session.add_all([
            TestUserTable(name='Name1', telegram_id='1123321', email='email1@emal.com', password_hash='123saedqw123rt'),
            TestUserTable(name='Name2', telegram_id='1223321', email='email2@emal.com', password_hash='124saedqw123rt'),
            TestUserTable(name='Name3', telegram_id='1323321', email='email3@emal.com', password_hash='125saedqw123rt'),
        ])
        test_session.commit()

    return test_session


@pytest.fixture(scope='module')
def cg():
    return pycoingecko.CoinGeckoAPI()

