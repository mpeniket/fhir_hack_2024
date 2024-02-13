from flask import render_template, redirect, request, Flask, Response
from utils.utils import upload_file_to_folder

from utils.utils import openai_chat_completion
from uploads.transcription import transcription
from openai import OpenAI, audio
import openai
from flask import render_template, redirect, request, Flask
from utils.utils import upload_file_to_folder, openai_chat_completion, unpack_json
import whisper
from uploads.transcription import transcription, res


OPENAI_API_KEY = "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"

client = OpenAI(api_key=OPENAI_API_KEY)

app = Flask(__name__)


@app.route("/")
def index():

    return render_template("index.html")


# This endpoint will be used to upload the audio file and send to OpenAI speech-to-text API
@app.route("/upload", methods=["POST"])
def upload_file():

    import requests

    url = "https://api.openai.com/v1/audio/transcriptions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
    }

    data = {
        "model": "whisper-1",
    }

    uploaded_file_path = upload_file_to_folder(request.files)

    with open(uploaded_file_path, "rb") as file:
        files = {
            "file": file
        }
        data = {
            "model": "whisper-1",
        }
        # Make the POST request
        response = requests.post(url, headers=headers, files=files, data=data)
        print(response.json())
        transcription = response.json()['text']
    
        with open('uploads/transcription.txt', 'w') as f:
            f.write(transcription)


    return redirect("/encoding")


# This endpoint will be used to send the text to OpenAI
@app.route("/encoding", methods=["POST", "GET"])
def encoding():

    t = transcription
    # res = openai_chat_completion(t)
    r = unpack_json(res)

    # return render_template("/form.html")
    return render_template("/form.html", field1=transcription, field2=r.reason_code_display, field3=r.supporting_info_items, field4=r.note)

