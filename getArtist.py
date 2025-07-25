from requestToken import requestAccessToken
import requests
import logging
import time

# Get bearer token info from requestToken.py
tokenInfo = requestAccessToken()
bearerToken = tokenInfo['access_token']

# Logging of artist info
logger = logging.getLogger(__name__)
logging.basicConfig(filename='info.log', encoding='utf-8',
    level=logging.INFO, format='%(asctime)s %(message)s',
    datefmt='%m/%d/%Y %H:%M:%S')

# Set the time converter to UTC
logging.Formatter.converter = time.gmtime

# Function to retrieve data of artist from Spotify ID in python dictionary format
def getArtistData(bearerToken):
    url = 'https://api.spotify.com/v1/artists/0TnOYISbd1XYRBk9myaseg'
    headers = {'Authorization':'Bearer ' +  bearerToken}
    
    r = requests.get(url, headers=headers)
    
    response = (r.json())
    return response

# Function to retrieve follower count for an artist
def getArtistFollowers():
    artist = getArtistData(bearerToken)['name']
    followers = getArtistData(bearerToken)['followers']['total']
    result = artist + ' has ' + str(followers) + ' followers on Spotify.'
    logger.info(result)
    return result


if __name__ == "__main__":
    getArtistData(bearerToken)
    getArtistFollowers()