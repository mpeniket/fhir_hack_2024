import os
from openai import OpenAI

def upload_file_to_folder(request_files, folder_path='./uploads/'):
    """Uploads a file to a folder on the server's filesystem
    """
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
    
def openai_chat_completion(transcription):
    """Send the transcription to OpenAI's chat completion API
    """
    # The API key is stored in a .env file
    api_key = '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'

    client = OpenAI(api_key=api_key)

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ]
    )
    messages = completion.choices[0].message
    print(messages)
    return messages.content