from __future__ import print_function
import datetime
import os.path
import webbrowser

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar']

def get_service():
    creds = None

    # Load existing token if available
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # If no valid credentials, start OAuth flow
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES
        )

        # Force Google to show account chooser
        auth_url, _ = flow.authorization_url(prompt='select_account')

        print("\nOpen this URL in Chrome to choose your account:")
        print(auth_url)

        # Open Chrome explicitly
        try:
            webbrowser.get("Chrome").open(auth_url)
        except:
            print("\nChrome browser not found. Please paste the URL manually into Chrome.\n")

        # Complete OAuth in terminal
        creds = flow.run_local_server(port=0)

        # Save token
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return build('calendar', 'v3', credentials=creds)

def upload_event():
    service = get_service()

    event = {
        'summary': 'Test Event',
        'description': 'Uploaded via Python',
        'start': {
            'dateTime': '2026-09-24T10:00:00+03:00',
        },
        'end': {
            'dateTime': '2026-09-24T11:00:00+03:00',
        }
    }

    created_event = service.events().insert(calendarId='primary', body=event).execute()
    print("Event created:", created_event.get('htmlLink'))

upload_event()
