import requests

def requestAccessToken():
    url = 'https://accounts.spotify.com/api/token'
    payload = {'grant_type': 'client_credentials',
        'client_id': '${{ secrets.CLIENT_ID }}',
        'client_secret': '${{ secrets.CLIENT_SECRET }}'}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    r = requests.post(url, params=payload, headers=headers)

    response = (r.json())
    return response

if __name__ == "__main__":
    requestAccessToken()