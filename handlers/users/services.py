import requests

from data.config import (
    YANDEX_LINK_GEOCODER,
    YANDEX_LINK_ORGANIZATIONS,
    YANDEX_API_TOKEN_GEOCODER,
    YANDEX_API_TOKEN_ORGANIZATIONS,
)


async def get_address(longitude: float, latitude: float) -> list:
    """ Get the address from the given coordinates """

    params = {
        "apikey": YANDEX_API_TOKEN_GEOCODER,
        "format": "json",
        "lang": "ru_RU",
        "kind": "house",
        "geocode": f'{longitude},{latitude}'
    }
    response = requests.get(url=YANDEX_LINK_GEOCODER, params=params)
    json_data = response.json()
    address = json_data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["metaDataProperty"][
        "GeocoderMetaData"]["AddressDetails"]["Country"]["AddressLine"].replace(' ', '').split(',')
    return address


async def get_location(longitude: float, latitude: float, name: str) -> list or bool:
    """ Get location of nearest one chosen restaurant """

    params = {
        "apikey": YANDEX_API_TOKEN_ORGANIZATIONS,
        'type': 'biz',
        "lang": "ru_RU",
        'text': name,
        'll': f'{longitude},{latitude}',
        'spn': '0.08,0.08',
        'rspn': '1'
    }
    response = requests.get(url=YANDEX_LINK_ORGANIZATIONS, params=params)
    try:
        location = response.json()['features'][0]['properties']['boundedBy'][0]
        return location
    except IndexError as e:
        print(e)
        return False
