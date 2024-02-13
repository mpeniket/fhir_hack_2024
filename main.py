from flask import render_template, redirect, request, Flask
from utils.utils import upload_file_to_folder
import whisper
from utils.utils import openai_chat_completion
from uploads.transcription import transcription
from openai import OpenAI

client = OpenAI()

OPENAI_API_KEY="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"

app = Flask(__name__)


@app.route("/")
def index():

    return render_template("index.html")


# This endpoint will be used to upload the audio file and send to OpenAI speech-to-text API
@app.route("/upload", methods=["POST"])
def upload_file():
    
    uploaded_filepath = upload_file_to_folder(request.files)

    audio_file= open(uploaded_filepath, "rb")
    transcript = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file,
    response_format="text",
    language= E)
    print(transcript.words)
    
    return redirect("/")


# This endpoint will be used to send the text to OpenAI
@app.route("/encoding", methods=["POST", "GET"])
def encoding():

    transcription = transcription
    res = openai_chat_completion(transcription)

    # return render_template("/form.html")
    return render_template("/form.html", field1=transcription, field2=res)
