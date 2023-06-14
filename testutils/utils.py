import requests

ENDPOINT = "http://localhost:8080/weather"
HTTP_STATUS_OK = 200
HTTP_STATUS_CREATED = 201
HTTP_STATUS_BAD_REQUEST = 400
HTTP_STATUS_UN_AUTHORIZED = 401
HTTP_STATUS_INTERNAL_SERVER_ERROR = 500


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
