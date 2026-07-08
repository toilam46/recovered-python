from db import Database
import pytest

@pytest.fixture
def db():
    database = Database()
    yield database # provide the fixture instance to the test
    # Note: No need to clean up the database after each test since it's an in-memory database and will be reset for each test. However, if you want to ensure that the database is clean after each test, you can clear it here.
    database.data.clear() # clean up after the test

def test_insert_and_retrieve(db):
    db.insert("key1", "value1")
    assert db.retrieve("key1") == "value1"

def test_update(db):
    db.insert("key1", "value1")
    db.update("key1", "value2")
    assert db.retrieve("key1") == "value2"

def test_delete(db):
    db.insert("key1", "value1")
    db.delete("key1")
    assert db.retrieve("key1") is None

def test_retrieve_nonexistent_key(db):
    assert db.retrieve("nonexistent_key") is None


