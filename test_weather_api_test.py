import requests

ENDPOINT = "http://localhost:8080/weather"


def test_create_weather_of_hamburg_city_endpoint():
    payload = city_payload()
    hamburg_response = create_city(payload)
    assert hamburg_response.status_code == 201

    hamburg_city_data = hamburg_response.json()
    hamburg_city_id = hamburg_city_data["id"]
    get_hamburg_city_data = get_city_by_id(hamburg_city_id)
    assert get_hamburg_city_data.status_code == 200
    hamburg_city_get_data = get_hamburg_city_data.json()
    assert hamburg_city_get_data["city"] == hamburg_city_data["city"]

    pass


def test_weather_by_id_endpoint():
    response = requests.get(ENDPOINT + "/1")
    assert response.status_code == 200
    pass


def test_weather_of_all_cities_endpoint():
    response = requests.get(ENDPOINT, auth=('admin', 'admin123'))
    assert response.status_code == 200
    pass


def test_weather_of_all_cities_with_invalid_authorization_endpoint():
    response = requests.get(ENDPOINT, auth=('unknown-user', 'unknown-password'))
    assert response.status_code == 401
    pass


def test_weather_of_unknown_city_endpoint():
    response = requests.get(ENDPOINT + "/unknown")
    assert response.status_code == 500
    pass


def test_weather_of_unexciting_city_endpoint():
    response = requests.get(ENDPOINT + "/unknownCity")
    assert response.status_code == 400
    pass


def get_city_by_id(city_id):
    return requests.get(ENDPOINT + f"/{city_id}")


def create_city(payload):
    return requests.post(ENDPOINT, auth=('admin', 'admin123'), json=payload)


def city_payload():
    return {
        "date": "2023-03-13",
        "lat": 123.3,
        "lon": 123.4,
        "city": "hamburg",
        "state": "germany",
        "temperatures": [
            21.2
        ]
    }
