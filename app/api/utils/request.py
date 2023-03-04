import logging
import requests

BASE_URL = "https://yfapi.net"
headers = {'X-API-KEY': 'jWWDN3ZiEb4EE932Klemt6V2qxUcFkQx17JqmZrf', 'accept': 'application/json'}

LOGGER = logging.getLogger(__name__)

def get(url, params=None):
    try:
        r = requests.get(BASE_URL + url, params=params, headers=headers)
        return r.json()
    except:
        LOGGER.exception('Request error')
        return None