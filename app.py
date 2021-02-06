import os
from flask import Flask, render_template
from spotify import get_info

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def hello_world():
    """ Returns root endpoint HTML """
    data_display = get_info()
    
    return render_template("index.html", data_display=data_display)
    
  
app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)