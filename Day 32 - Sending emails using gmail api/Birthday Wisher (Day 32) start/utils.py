from __future__ import print_function
import base64
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.auth.transport.requests import Request 
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build, Resource
from googleapiclient.errors import HttpError
from email.message import EmailMessage
import pathlib


def get_creds():
    """Retrieves google credentials to use with api."""
    
    # reprpesends current file as a pathlib.Path object
    CURRENT_FILE_DIRECTORY = pathlib.Path(__file__)
    
    while not CURRENT_FILE_DIRECTORY.match("c:\\Users\\david\\Desktop\\Coding"):
        CURRENT_FILE_DIRECTORY = CURRENT_FILE_DIRECTORY.parent

    credentials_path: pathlib.Path = CURRENT_FILE_DIRECTORY / "Google related" / "client_secret.json"
    token_path: pathlib.Path = CURRENT_FILE_DIRECTORY / "Google related" / "token.json"

    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if token_path.exists():
        creds = Credentials.from_authorized_user_file(token_path, scopes=["https://www.googleapis.com/auth/gmail.modify"])
        
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                credentials_path, scopes=["https://www.googleapis.com/auth/gmail.modify"])
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token_path, 'w') as token:
            token.write(creds.to_json())
            
    return creds

def create_draft(users, to:str, content:str, subject: str = None) -> Resource:
    """Creates a draft with specified parameters, ready to send at any moment"""
    
    user_email = users.getProfile(userId="me").execute()["emailAddress"]
    
    message = EmailMessage()

    message.set_content(content)

    message['To'] = to
    message['From'] = user_email
    message['Subject'] = subject

    # encoded message
    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    create_message = {
            "message": {
                'raw': encoded_message
            }
            
    }
    # pylint: disable=E1101
    draft = users.drafts().create(userId="me", body=create_message).execute()
    
    return draft
    
