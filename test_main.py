# content of test_sysexit.py
import pytest


def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()


def app(client):
    response = client.get('/')
    asset b'name' in response.data
    
