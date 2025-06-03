import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Flask To-Do App!" in response.data

def test_get_tasks_empty(client):
    response = client.get('/tasks')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_add_task_success(client):
    response = client.post('/tasks', json={'task': 'Write tests'})
    assert response.status_code == 201
    assert response.get_json()['message'] == 'Task added!'

def test_add_task_missing(client):
    response = client.post('/tasks', json={})
    assert response.status_code == 400
    assert response.get_json()['error'] == 'Task is required'
