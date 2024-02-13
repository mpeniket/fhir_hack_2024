from flask import render_template, redirect, request, Flask
from utils.utils import upload_file_to_folder
import whisper

app = Flask(__name__)


@app.route("/")
def index():

    return render_template("index.html")


# This endpoint will be used to upload the audio file and send to OpenAI speech-to-text API
@app.route("/upload", methods=["POST"])
def upload_file():

    uploaded_filepath = upload_file_to_folder(request.files)
    
    return redirect("/")
