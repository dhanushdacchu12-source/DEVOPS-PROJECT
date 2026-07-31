from app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_dhanush_result():
    client = app.test_client()
    response = client.get('/result/dhanush')
    assert response.status_code == 200
    assert b'85' in response.data
    assert b'PASS' in response.data

def test_health():
    client = app.test_client()
    response = client.get('/health')
    assert response.status_code == 200

def test_invalid_student():
    client = app.test_client()
    response = client.get('/result/unknown')
    assert response.status_code == 404
