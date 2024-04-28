from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


expected_data = {
    "Italy": {
        "Rome": {
            "January": {"high": 50, "low": 32}
        }
    }
}

def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_countries():
    response = client.get("/countries")
    assert response.status_code == 200
    assert sorted(response.json()) == ["England", "France", "Germany", "Italy", "Peru", "Portugal", "Spain"]

def test_cities():
    response = client.get("/countries/Italy")
    assert response.status_code == 200
    assert sorted(response.json()) == ["Milan", "Rome"]

def test_monthly_average():
    response = client.get("/countries/Italy/Rome/January")
    assert response.status_code == 200
    assert response.json() == expected_data["Italy"]["Rome"]["January"]