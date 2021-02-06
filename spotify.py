import requests
import os
from dotenv import load_dotenv, find_dotenv
import random

load_dotenv(find_dotenv()) # This is to load your API keys from .env

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

AUTH_URL = 'https://accounts.spotify.com/api/token'

# POST
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

# randomly choose an artist ID from a list
id_list = ['1uNFoZAHBGtllmzznpCI3s','7bXgB6jMjp9ATFy66eO08Z', '6vWDO969PvNqNYHIOW5v0m']
songID = random.choice(id_list)

BASE_URL ='https://api.spotify.com/v1/artists/{}/top-tracks'.format(songID)


def get_info():

    params = {'market' : 'US'}
        
    response = requests.get(BASE_URL,
                        headers=headers,
                        params=params)
    
    data = response.json()
    
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
    
    
    
    


#print(artist_name())


'''
def get_track_info():
    
    params = {'limit' : 10}
    
    response = requests.get(BASE_URL,
                        headers=headers,
                        params=params)
    
    data = response.json()
    
    def get_artist_name():
        for i in range(0, 10):
            var1 = (data['tracks'][i]['artists'][0]['name'])
            print(var1)
        return var1
    
    names = get_artist_name()
    return names
'''

    # Print tracks and info for first 10 tracks returned by artist id
    #for i in range(0, 10):
        #print(data['tracks'][i]["name"])  #song name
        #print(data['tracks'][i]["album"]["images"][2]["url"]) #song-related image
        #print(data['tracks'][i]["external_urls"]["spotify"]) # song preview URL
        #print(data['tracks'][i]['artists'][0]['name']) #artist
        
    
    