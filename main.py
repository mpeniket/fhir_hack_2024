from flask import render_template, redirect, request, Flask, Response
from utils.utils import upload_file_to_folder

from utils.utils import openai_chat_completion
from openai import OpenAI, audio
import openai
from flask import render_template, redirect, request, Flask
from utils.utils import upload_file_to_folder, openai_chat_completion
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
 
        transcription = response.json()['text']
    
        with open('uploads/transcription.txt', 'w') as f:
            f.write(transcription)


    return redirect("/encoding")


# This endpoint will be used to send the text to OpenAI
@app.route("/encoding", methods=["POST", "GET"])
def encoding():

    # transcription = None
    # with open('uploads/transcription.txt', 'r') as f:
    #     transcription = f.read()
    # fihr_json.replace('```json','').replace('```',''), clinical_letter = openai_chat_completion(transcription)
    
    # print(transcription)
    # print(fihr_json)
    # print(clinical_letter)
    
    fihr_json_debug = """{
                    "resourceType": "Encounter",
                    "status": "finished",
                    "class": {
                      "system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
                      "code": "AMB",
                      "display": "ambulatory"
                    },
                    "subject": {
                      "reference": "Patient/MarthaColeJones",
                      "display": "Martha Cole-Jones"
                    },
                    "period": {
                      "start": "2023-02-01",
                      "end": "2023-02-01"
                    },
                    "reasonCode": [
                      {
                        "text": "Feeling sad, tiredness, low energy, and headaches."
                      }
                    ],
                    "diagnosis": [
                      {
                        "condition": {
                          "display": "Seasonal Affective Disorder"
                        },
                        "use": {
                          "coding": [
                            {
                              "system": "http://terminology.hl7.org/CodeSystem/diagnosis-role",
                              "code": "CC",
                              "display": "Chief complaint"
                            }
                          ]
                        },
                        "rank": 1
                      },
                      {
                        "condition": {
                          "display": "Headaches related to screen time"
                        },
                        "use": {
                          "coding": [
                            {
                              "system": "http://terminology.hl7.org/CodeSystem/diagnosis-role",
                              "code": "AD",
                              "display": "Additional diagnosis"
                            }
                          ]
                        },
                        "rank": 2
                      }
                    ],
                    "participant": [
                      {
                        "individual": {
                          "display": "General Practitioner"
                        }
                      }
                    ],
                    "serviceProvider": {
                      "display": "Primary Care Clinic"
                    },
                    "text": {
                      "status": "generated",
                      "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\">Martha Cole-Jones, 30-Sep-1998, presents with seasonal sadness, low energy, and headaches. No suicidal thoughts. Feels safe at home. Headaches possibly due to screen time.</div>"
                    }
                  }"""
    transcription_debug = """Hello, could I confirm your full name and date of birth please? Martha Cole-Jones, the 30th of the 9th,
                    1998. Lovely to meet you. What's brought you in today? I'm feeling quite sad lately. It's February, it's
                    still quite dark, quite early. I think I'm really affected by the seasons and, yeah, just wanted to see
                    if you could help me. Okay, we'll do our best to get to the bottom of that. How are your energy levels?
                    Quite low. I'd say I'm quite tired all the time. I've not got much energy to do things. Okay, I'm really
                    sorry to hear that. Thank you. Have you had any thoughts of self-harm or suicide? No, I haven't. Some
                    days are quite hard. I feel quite low, but I don't think I've reached that point yet. Do you feel safe
                    at home where you are? Yes, I do feel safe. Yes, I do. And now just a few yes or no questions. Any
                    headaches? Yes. Tell me more about that. Yes, I have headaches probably two or three times a week. I
                    went to the opticians, they said it could be the screen time on my laptop all the time. Why are you on
                    your laptop a lot? What do you do? I have a desk job. That's my job. We're nine to five. That's great.
                    Thank you for coming in. I'll point you to some talking therapies and we can look into prescribing some
                    medications that might help. Great, thanks."""
    clinical_letter_debug = """Dear Dr. Wilson,
            
            [Information] RE: New Referral Ms. Martha Cole-Jones, DOB 30/09/1998 22 Grant Avenue, City, Postcode
            
            [Situation] I appreciate the referral of Ms. Martha Cole-Jones, a 24-year-old female, presenting with symptoms suggestive of Seasonal Affective Disorder (SAD).
            
            [Background] Ms. Cole-Jones reports feeling notably sad, particularly noting the impact of the season on her mood, with symptoms peaking during the darker months. She describes a significant decrease in energy levels, experiencing constant fatigue that impedes her daily activities. Despite these challenges, she denies any current thoughts of self-harm or suicide and confirms feeling safe in her home environment.
            
            [Assessment] Ms. Cole-Jones experiences frequent headaches, occurring two to three times a week, which she attributes to prolonged screen time related to her desk job. An examination by her optician suggested the headaches might be related to this excessive screen exposure, but no further investigations have been conducted to rule out other potential causes.
            
            [Request] Considering her symptomatology and the seasonal pattern of her low mood and energy, a diagnosis of Seasonal Affective Disorder is being considered. While Ms. Cole-Jones denies any thoughts of self-harm, the persistence of her low mood and its impact on her quality of life necessitate intervention.
            
            [Plan] I have recommended engaging in talking therapies to address her current emotional state and explore coping strategies for managing her symptoms. Additionally, we will consider the initiation of medication that may ameliorate her depressive symptoms. Further assessment of her frequent headaches is also advised to rule out any underlying issues not associated with screen time.
            
            I would be grateful if you could facilitate a referral to a service providing talking therapies suited to her needs. Furthermore, a review of her headache pattern with consideration of a neurological evaluation may be beneficial to ensure a comprehensive approach to her care.
            
            Thank you for entrusting her care to me. Please feel free to contact me if you require further information or wish to discuss her management plan in more detail.
            
            Kind regards,
            
            [Your Name]
            [Your Qualifications]
            [Contact Information]"""
    
    return render_template("form.html", transcription=transcription_debug, fihr_json=fihr_json_debug, clinical_letter=clinical_letter_debug)
