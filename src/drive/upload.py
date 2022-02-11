# import json
# import requests

# from config import API_KEY, FOLDER_ID

# # Authorization header for post request
# # TODO: create Uploader Class
# # TODO: let uploader have list of files to be uploaded
# # TODO: create upload all function
# # TODO: Handle response per file -> remove from upload queue and add to uploaded list

# def upload_file(filepath: str):
#     headers = {"Authorization": f"Bearer {API_KEY}"}
#     print(headers)
#     params = { "name": filepath ,
#                "parents": [FOLDER_ID]
#                }
#     files = {
#         "data": ('metadata', json.dumps(params), "application/json; charset=utf-8"),
#         "file": open(filepath, "rb")
#     }
#     r = requests.post(
#         "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
#         headers = headers,
#         files   = files
#     )

#     if r.status_code != 200:
#         print(f"Error uploading file {filepath}")
#         print(f"response: {r.text}")
#         # TODO: proper error handling here
#         return

#     print(f"Uploading file {filepath} succesful!")
#     return

# # TODO: def upload_files(paths):