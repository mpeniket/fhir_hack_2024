from flask import render_template, redirect, request, Flask
from utils.utils import upload_file_to_folder
from utils.utils import openai_chat_completion


app = Flask(__name__)


@app.route("/")
def index():

    return render_template("index.html")


# This endpoint will be used to upload the audio file and send to OpenAI speech-to-text API
@app.route("/upload", methods=["POST"])
def upload_file():

    print(request.files)

    uploaded_filepath = upload_file_to_folder(request.files)
    
    return redirect("/")

# This endpoint will be used to send the text to OpenAI 
@app.route("/encoding", methods=["POST", "GET"])
def encoding():

    transcription = request.form.get("transcription")
    res = openai_chat_completion(transcription)

    # return render_template("/form.html")
    return render_template("/form.html", field1=transcription, field2=res)
