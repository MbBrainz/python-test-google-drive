import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def upload_file(filename, dir):
    gauth = GoogleAuth(settings_file=".config/settings.yaml")
    gauth.LoadClientConfigFile(".config/client_secrets.json")
    gauth.LoadCredentialsFile('.config/credentials.json')
    drive = GoogleDrive(gauth)

    folder = '1VsPgpgOpzlxNdn8JIQ0KjsfKFGPBa2sF'

    file1 = drive.CreateFile({'parents': [{'id': folder}], 'title':f'{filename}'})

    file1.SetContentFile(os.path.join(os.getcwd(), dir, filename))
    file1.SetContentString('Hello, world!')
    file1.Upload()

upload_file('test.txt', 'src/data')
