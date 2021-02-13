import requests
import os
from dotenv import load_dotenv, find_dotenv
import random

load_dotenv(find_dotenv()) # This is to load your API keys from .env

##################################
###'''CLIENT CREDENTIAL FLOW'''###
##################################

# keys from spotify and genius account hidden in .env
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
GENIUS_CLIENT_ID = os.getenv("GENIUS_CLIENT_ID")
GENIUS_CLIENT_SECRET = os.getenv("GENIUS_CLIENT_SECRET")
GEN_TOKEN = os.getenv("GEN_TOKEN")

AUTH_URL = 'https://accounts.spotify.com/api/token'

# POST a request 
auth_response = requests.post(AUTH_URL, {
'grant_type': 'client_credentials',
'client_id': CLIENT_ID,
'client_secret': CLIENT_SECRET,
})

# convert the response to JSON
auth_response_data = auth_response.json()

# save the access token
access_token = auth_response_data['access_token']

headers = {
'Authorization': 'Bearer {token}'.format(token=access_token)
}

######################################
###'''CLIENT CREDENTIAL FLOW END'''###
######################################

##############################################################################

# randomly choose an artist ID from a list
# Justin Bieber, Beyonce, Chris Brown 
id_list = ['1uNFoZAHBGtllmzznpCI3s','7bXgB6jMjp9ATFy66eO08Z', '6vWDO969PvNqNYHIOW5v0m']
artistID = random.choice(id_list)

BASE_URL ='https://api.spotify.com/v1/artists/{}/top-tracks'.format(artistID)

def get_info():
    '''Returns a list of a chosen song info: artist, name, url, image'''

    params = {'market' : 'US'}
        
    response = requests.get(BASE_URL,
                        headers=headers,
                        params=params)
    
    data = response.json()
    
    # choose a random song
    random_song_num = random.randint(0, 9)
    
    def get_artist_name():
        artist_name = data['tracks'][random_song_num]['artists'][0]['name']
        return (artist_name)
    
    def get_song_name():
        song_name = data['tracks'][random_song_num]['name']
        return (song_name)
        
    def get_preview_url():
        preview_url = data['tracks'][random_song_num]['preview_url']
        return (preview_url)
        
    def get_image_url():
        image_url = data['tracks'][random_song_num]['album']['images'][1]['url']
        return (image_url)
        
    info_array = [get_artist_name(), get_song_name(), get_preview_url(), get_image_url()]
    
    return (info_array)
    

def request_song_info(song_name, artist_name):
    base_url = 'https://api.genius.com'
    headers = {'Authorization': 'Bearer ' + GEN_TOKEN}
    search_url = base_url + '/search'
    data = {'q': song_name + ' ' + artist_name}
    response = requests.get(search_url, data=data, headers=headers)

    return response
  