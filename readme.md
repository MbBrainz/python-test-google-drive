# Test application for running a python simulation on Akash DeCloud

<!-- To make it work remove the .txt suffix from config.py.txt file and fill in your google api key

if you dont have a google api key you can get it by following [this tutorial](https://codingshiksha.com/python/how-to-upload-files-to-google-drive-using-python-3-using-google-drive-api-v3-full-project/)


The manifest is the one used for the deployment in Akashlytics -->

### Prerequisites:
- google drive api key setup at www.console.cloud.google.com
- .config folder setup: See instructions below



### setup .config/
create .config folder in main directory
download client_secrets_00SOMECODE00.json from console.cloud.google.com
rename it to client_secrets.json and put it in `.config/`
create a settings.yaml file in the following format and fill in the credentials, which are found in client_secrets.json:

```
    client_config_backend: file
    client_config:
        client_id: [your_client_id].apps.googleusercontent.com
        client_secret: [your_client_secret]

    save_credentials: True
    save_credentials_backend: file
    save_credentials_file: credentials.json

    get_refresh_token: True

    oauth_scope:
        - https://www.googleapis.com/auth/drive
```
