# Project 1 - Music Discovery Web App
This app will use the Spotify API and Genius API to dynamically generate data. It will display artists, songs, image of song, audio, and a link to the lyrics. It also has a search bar in which the user can input an artist or an album and the data that best matches the search will fetch results and display them. The project uses the Flask python library to display the html on the '/' endpoint.

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
```bash
npm install -g heroku
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


## To Deploy App
1. Install the above heroku package. Create your free account [here](https://www.heroku.com/).
2. Follow [this](https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true) guide to deploy the app.


## Questions
1. What are at least 3 technical issues (between M1 and M2 combined) you encountered with your project? How did you fix them?
    1. Some of the issues I found in M1 were organizing the code using def and getting around using the API to extract some data. Some of my variables were not being recognized. 
    2. The way I fixed these issues was to look into how def can be better organized, such as what parameters go inside the function and what is being returned. Another way to fix the API issue was to play around and see what each field prints.
    3. Some issues in M2 were figuring out how to extract the lyrics using the Genius API since little information was provided. Another issue I found was with the jquery code. This part was for extra credit and js and ajax were not covered in class. However, I have some exprience with js and ajax, so it wasn't too bad to follow. 
    4. I fixed this issue by reading the documentation for the Genius API and reading through some stackoverflow answers. I fixed the other issue using stackoverflow and some youtube videos. 
2. What are known problems (still existing), if any, with your project
    1. There are no known problems that exist with the project.
3. What would you do to improve your project in the future? 
    1. Instead of using the audio element web player, I would customize the player widget from scratch. I would also add more features, such as adding the song playing to the user's personal spotify account's library, which will require the user to log in. I would also try to have a more advanced front-end design.







