import requests

from testutils.utils import city_payload, create_city, get_city_by_id, ENDPOINT, HTTP_STATUS_OK, \
    HTTP_STATUS_UN_AUTHORIZED, HTTP_STATUS_INTERNAL_SERVER_ERROR, HTTP_STATUS_CREATED, HTTP_STATUS_BAD_REQUEST


def test_create_weather_of_hamburg_city_endpoint():
    payload = city_payload()
    hamburg_response = create_city(payload)
    assert hamburg_response.status_code == HTTP_STATUS_CREATED

    hamburg_city_data = hamburg_response.json()
    hamburg_city_id = hamburg_city_data["id"]
    get_hamburg_city_data = get_city_by_id(hamburg_city_id)
    assert get_hamburg_city_data.status_code == HTTP_STATUS_OK
    hamburg_city_get_data = get_hamburg_city_data.json()
    assert hamburg_city_get_data["city"] == hamburg_city_data["city"]

    pass


def test_weather_by_id_endpoint():
    response = requests.get(ENDPOINT + "/1")
    assert response.status_code == HTTP_STATUS_OK
    pass


def test_weather_of_all_cities_endpoint():
    response = requests.get(ENDPOINT, auth=('admin', 'admin123'))
    assert response.status_code == HTTP_STATUS_OK
    pass


def test_weather_of_all_cities_with_invalid_authorization_endpoint():
    response = requests.get(ENDPOINT, auth=('unknown-user', 'unknown-password'))
    assert response.status_code == HTTP_STATUS_UN_AUTHORIZED
    pass


def test_weather_of_unknown_city_endpoint():
    response = requests.get(ENDPOINT + "/unknown")
    assert response.status_code == HTTP_STATUS_INTERNAL_SERVER_ERROR
    pass


def test_weather_of_unexciting_city_endpoint():
    response = requests.get(ENDPOINT + "/unknownCity")
    assert response.status_code == HTTP_STATUS_BAD_REQUEST
    pass
