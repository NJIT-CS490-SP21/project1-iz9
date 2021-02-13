import os
from flask import Flask, render_template
from spotify import get_info, request_song_info, matches

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def hello_world():
    """ Returns root endpoint HTML """
    data_display = get_info()
    song_lyrics_url = matches(data_display[1], data_display[0])
    
    return render_template("index.html", data_display=data_display, song_lyrics_url=song_lyrics_url)
  
app.run(
    #visible server and port, server restarts with changes
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)