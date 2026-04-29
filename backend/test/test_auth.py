from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


#test registration
def test_register_user():
    response = client.post("/users/register", json={
        "name" : "Rahma",
        "email": "test@test.com",
        "password": "123456"
    })

    assert response.status_code == 201
    assert "email" in response.json()

#test email forma
def test_email_user():
    response = client.post("/users/register", json={
        "name" : "Rahma",
        "email": "test-email",
        "password": "123456"
    })

    assert response.status_code == 422  # validation error

#test password lenght

def test_register_short_password():
    response = client.post("/users/register", json={
        "name" : "Rahma",
        "email": "testpassword@gmail.com",
        "password": "123"
    })

    assert response.status_code == 422




def test_register_existing_email():
    # First request (should pass)
    client.post("/users/register", json={
        "name": "Rahma",
        "email": "duplicate@test.com",
        "password": "123456"
    })

    # Second request (should fail)
    response = client.post("/users/register", json={
        "name": "Rahma",
        "email": "duplicate@test.com",
        "password": "123456"
    })

    assert response.status_code == 400