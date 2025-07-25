import requests
import os
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='info.log', encoding='utf-8',
    level=logging.INFO, format='%(asctime)s %(message)s',
    datefmt='%m/%d/%Y %H:%M:%S')

def requestAccessToken():
    CLIENT_ID = os.environ["CLIENT_ID"]
    CLIENT_SECRET = os.environ["CLIENT_SECRET"]


    url = 'https://accounts.spotify.com/api/token'
    payload = {'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    r = requests.post(url, params=payload, headers=headers)

    response = (r.json())
    return response

if __name__ == "__main__":
    requestAccessToken()