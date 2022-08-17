from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.errors import HttpError
from utils import create_draft, get_creds
import datetime
import pathlib
import random

def get_quotes() -> list[str]:
    
    
    CURRENT_FILE_DIRECTORY = pathlib.Path(__file__)
    quotes_directory = CURRENT_FILE_DIRECTORY.parent / "quotes.txt"
    
    quotes = []
    
    with open(quotes_directory, "r") as f:
        quotes = f.readlines()
        
    return quotes
    
def main():
    
    try:
        
        # create gmail api client
        service = build('gmail', 'v1', credentials=get_creds())

        users = service.users()
        
        quotes = get_quotes()
        
        random_quote = random.choice(quotes)
        
        draft = create_draft(users, "email@gmail.com", random_quote, "A random quote")
        
        draft_body = {
            "id": draft["id"]
        }
        
        message = users.drafts().send(userId="me", body=draft_body).execute()
        
        

    except HttpError as error:
        print(F'An error occurred: {error}')

if __name__ == '__main__':
    main()