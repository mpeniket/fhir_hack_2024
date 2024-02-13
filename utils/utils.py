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