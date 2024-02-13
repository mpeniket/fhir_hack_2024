from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    
    transcription = "lorem fdsajk;fndsak;jfndjksalfnkdjlsafnkdlsjafnkjdsa"
    
    return render_template('index.html')