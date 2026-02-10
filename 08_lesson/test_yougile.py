import pytest
import requests
import uuid

# Константы для настройки
BASE_URL = "https://ru.yougile.com/api-v2/projects"
TOKEN = 'vp7k4OzS9fzop+vdl1pYyFwpOb+uD9aYhdk8q-DgCIcZflz-MWVvWypJEL0tHXsB'
COMPANY_ID = '1ea0d784-2536-4eae-9424-fc17cc0d4bff'
USER_ID = "5dd49dc0-0199-4d70-9537-d683828fdd90"
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}



# --- [POST] /api-v2/projects ---

def test_create_project_positive():
    payload = {
        "title": f"New Project {uuid.uuid4().hex[:6]}",
        "users": USER_ID
    }
    response = requests.post( BASE_URL, json=payload, headers=HEADERS)
    assert response.status_code == 201
    assert "id" in response.json()

def test_create_project_negative_empty_title():
    payload = {
        "title": "",
        "users": USER_ID
    }
    response = requests.post(BASE_URL, json=payload, headers=HEADERS)
    assert response.status_code == 400


# --- [GET] /api-v2/projects/{id} ---

def test_get_project_positive(created_project_id):
    response = requests.get(f"{BASE_URL}/{created_project_id}", headers=HEADERS)
    assert response.status_code == 200
    assert response.json()['id'] == created_project_id

def test_get_project_negative_invalid_id():
    invalid_id = "00000000-0000-0000-0000-000000000000"
    response = requests.get(f"{BASE_URL}/{invalid_id}", headers=HEADERS)
    assert response.status_code == 404


# --- [PUT] /api-v2/projects/{id} ---

def test_update_project_positive(created_project_id):
    new_title = f"Updated Title {uuid.uuid4().hex[:6]}"
    payload = {"title": new_title}
    response = requests.put(f"{BASE_URL}/{created_project_id}", json=payload, headers=HEADERS)
    
    assert response.status_code == 200
    # Проверяем, что изменения применились
    get_res = requests.get(f"{BASE_URL}/{created_project_id}", headers=HEADERS)
    assert get_res.json()['title'] == new_title

def test_update_project_negative_non_existent():
    invalid_id = uuid.uuid4()
    payload = {"title": "Should Fail"}
    response = requests.put(f"{BASE_URL}/{invalid_id}", json=payload, headers=HEADERS)
    assert response.status_code == 404
