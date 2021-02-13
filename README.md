# Project 1 - Music Discovery Web App
This app will use the Spotify API and Genius API to dynamically generate data. It will display artists, songs, image of song, audio, and a link to the lyrics.

## Sign up for Spotify Developer Account and Genius API 
1. Use [this](https://developer.spotify.com/documentation/web-api/quick-start/) website for info on setting it up.
2. Also set up a premium or free account with Spotify.
3. Set up a free Genius account to register the app. Read [this](https://docs.genius.com/) to get started. 

## Install Requirements (if you don't already have them)
```bash
pip install -U python-dotenv
```
```bash
pip install requests
```

## Setup
1. Create .env file in your project directory
2. Add your SPOTIFY CLIENT ID, KEY AND GENIUS ID, KEY, TOKEN from your accounts with the lines: 
```bash
export CLIENT_ID='YOUR_ID'
export CLIENT_SECRET= 'YOUR_SECRET'
export GENIUS_CLIENT_ID='YOUR_ID'
export GENIUS_CLIENT_SECRET='YOUR_SECRET'
export GEN_TOKEN='YOUR_TOKEN'
```

## Run Application
1. Run command in terminal 
```bash
python app.py
```
2. Preview web page in browser '/'






