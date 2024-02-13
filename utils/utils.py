import os
from openai import OpenAI
import json


def upload_file_to_folder(request_files, folder_path="./uploads/"):
    """Uploads a file to a folder on the server's filesystem"""
    if "file" not in request_files:
        return "No file part"
    file = request_files["file"]
    if file.filename == "":
        return "No selected file"
    if file:
        # Save the file to the server's filesystem
        filepath = f"{folder_path}{file.filename}"
        file.save(filepath)
        return filepath
    
def extract_data(json_data):
    data = json.loads(json_data)
    
    reason_code = data.get("reasonCode", [])
    reason_code_display = [code.get("coding", [{}])[0].get("display") for code in reason_code]
    
    supporting_info = data.get("supportingInfo", [])
    supporting_info_items = []
    for info in supporting_info:
        category = info.get("category", {}).get("coding", [{}])[0].get("display")
        code = info.get("code", {}).get("coding", [{}])[0].get("display")
        value_codeable_concept = info.get("valueCodeableConcept", {}).get("coding", [{}])[0].get("display")
        supporting_info_items.append({"category": category, "code": code, "valueCodeableConcept": value_codeable_concept})
    
    note = data.get("note", [{}])[0].get("text")
    
    return reason_code_display, supporting_info_items, note

def openai_chat_completion(transcription):
    """Send the transcription to OpenAI's chat completion API"""
    # The API key is stored in a .env file
    api_key = "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"

    client = OpenAI(api_key=api_key)

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": f"""You are a beneficial, computer science professor who's the foremost expert in the FIHR open health data standard. You have been tasked with converting the following transcription (everything following the text "TRANSCRIPTION:") of a clinical consultation into a FIHR query that is perfectly formatted in JSON format that could be inserted into a FIHR database. The usecase is for inserting this transcription into a FIHR-supported EHR. Only respond with the JSON object. \n\n""",
            },
            {"role": "user", "content": "TRANSCRIPTION:" + transcription},
        ],
    )
    messages = completion.choices[0].message
    print(messages)
    return messages.content
