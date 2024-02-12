from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def output_fields():
    
    transcription = "lorem fdsajk;fndsak;jfndjksalfnkdjlsafnkdlsjafnkjdsa"
    
    return "<p>Hello, World!</p>"