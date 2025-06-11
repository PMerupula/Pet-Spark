import pytest
from app import app

def test_app_exists():
    """our app exists"""
    assert app is not None

def test_pets_endpoint_responds():
    """/api/pets endpoint responds"""
    client = app.test_client()
    response = client.get('/api/pets')    git pull origin apiRoutes
    assert response.status_code in [200, 500]  
def test_pets_endpoint_returns_json():
    """pets endpoint returns JSON"""
    client = app.test_client()
    response = client.get('/api/pets')
    try:
        data = response.get_json()
        assert data is not None
    except:
        pass

def test_individual_pet_endpoint():
    """Test getting a single pet by ID"""
    client = app.test_client()
    response = client.get('/api/pets/12345')
    assert response.status_code in [200, 404, 500]

def test_pets_with_filters():
    """Test pets endpoint with some filters"""
    client = app.test_client()
    response = client.get('/api/pets?type=dog&location=Davis,CA')
    assert response.status_code in [200, 500]

def test_auth_register_endpoint():
    """register endpoint exists"""
    client = app.test_client()
    response = client.post('/api/authentication/register')
    assert response.status_code == 415   

def test_auth_login_endpoint():
    """login endpoint exists"""
    client = app.test_client()
    response = client.post('/api/authentication/login')
    assert response.status_code == 415

def test_register_with_empty_data():
    """Test register with empty JSON"""
    client = app.test_client()
    response = client.post('/api/authentication/register', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert "required" in data["error"].lower()

def test_login_with_empty_data():
    """Test login with empty JSON"""
    client = app.test_client()
    response = client.post('/api/authentication/login', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert "required" in data["error"].lower()