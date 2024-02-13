from flask import render_template, redirect, request, Flask
from utils.utils import upload_file_to_folder
import whisper
from utils.utils import openai_chat_completion
from uploads.transcription import transcription


app = Flask(__name__)


@app.route("/")
def index():

    return render_template("index.html")


# This endpoint will be used to upload the audio file and send to OpenAI speech-to-text API
@app.route("/upload", methods=["POST"])
def upload_file():

    uploaded_filepath = upload_file_to_folder(request.files)

    model = whisper.load_model("base")
    options = whisper.DecodingOptions(language="en")
    result = model.transcribe(uploaded_filepath, verbose=True, **options)

    return redirect("/")


# This endpoint will be used to send the text to OpenAI
@app.route("/encoding", methods=["POST", "GET"])
def encoding():

    t = transcription
    res = openai_chat_completion(t)

    # return render_template("/form.html")
    return render_template("/form.html", field1=transcription, field2=res)
