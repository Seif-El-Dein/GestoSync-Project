import os
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

# Module: Google Drive Uploader
class GoogleDriveUploader:
    def __init__(self):
        gauth = GoogleAuth()
        gauth.LoadClientConfigFile("google_oauth.json")
        gauth.LocalWebserverAuth()
        self.drive = GoogleDrive(gauth)

    def upload_file(self, file_path, folder_id=None):
        file_name = os.path.basename(file_path)
        file_metadata = {'title': file_name, 'parents': [{'id': folder_id}]} if folder_id else {'title': file_name}
        gfile = self.drive.CreateFile(file_metadata)
        gfile.SetContentFile(file_path)
        gfile.Upload()
        return gfile['id']