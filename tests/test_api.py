from src.api import app
import json

def test_index_route():
    response = app.test_client().get('/')
    assert response.status_code == 200

def test_index_route_params():
    response = app.test_client().get('/', query_string={'input':'test'}, content_type='application/json')
    assert json.loads(response.data) == {'input':'test'}
    assert response.status_code == 200