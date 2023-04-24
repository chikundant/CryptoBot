import pytest
from project.models import TestUserTable


@pytest.mark.parametrize('data', ['Name1', 'Name2', 'Name3'])
def test_get_name_from_db(test_session, data):
    assert data == test_session.query(TestUserTable).filter_by(name=data).first().name


@pytest.mark.parametrize('data', ['1123321', '1223321', '1323321'])
def test_get_telegram_id_from_db(test_session, data):
    assert data == test_session.query(TestUserTable).filter_by(telegram_id=data).first().telegram_id


@pytest.mark.parametrize('data', ['email1@emal.com', 'email2@emal.com', 'email3@emal.com'])
def test_get_email_from_db(test_session, data):
    assert data == test_session.query(TestUserTable).filter_by(email=data).first().email


@pytest.mark.parametrize('data', ['123saedqw123rt', '124saedqw123rt', '125saedqw123rt'])
def test_get_password_hash_from_db(test_session, data):
    assert data == test_session.query(TestUserTable).filter_by(password_hash=data).first().password_hash
