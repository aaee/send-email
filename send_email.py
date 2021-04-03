from __future__ import print_function
import pickle
from os import path,environ
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from email.mime.text import MIMEText
import base64
from urllib.error import HTTPError
from datetime import datetime
from random import seed, choice
from dotenv import load_dotenv

load_dotenv()
 



# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.compose']
sender = environ['SENDER']
receiver = environ['RECEIVER']
receiver_cc = environ['RECEIVER_CC']



dir_abs = path.dirname(__file__)
print(dir_abs)

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    print(dir_abs)
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if path.exists(dir_abs + '/token.pickle'):
        with open(dir_abs + '/token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                dir_abs + '/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(dir_abs + '/token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    # send email
    subject = 'Good luck...'
    message_text = create_content_ice_breaker()
    print('sending')
    print(message_text)
    message_1 = create_message(sender, receiver, subject, message_text, cc=receiver_cc)
    #message_2 = create_message(sender, 'nikhil.ninne@gmail.com', subject, message_text, cc='alicia.esquivias@gmail.com, nikhil.ninne@gmail.com')
    send_message(service, 'me', message_1)
    #send_message(service, 'me', message_2)


    # # Call the Gmail API
    # results = service.users().labels().list(userId='me').execute()
    # labels = results.get('labels', [])
    #
    # if not labels:
    #     print('No labels found.')
    # else:
    #     print('Labels:')
    #     for label in labels:
    #         print(label['name'])


def create_content_nikhil():
    text = """
    Good Morning Nikhil!!!
    
    I just want to wish you a happy {day}th day in your new job!
    Have fun and learn a lot! 
    
    Here is your quote of the day to keep you motivated! (this time about {topic})
    
        "{quote}"
        -- {by}
        
    Best, 
    
    Ali's bot on behalf of Ali :) 
    """

    # get number of the day we are in
    first_day = datetime.strptime('2021-01-15', '%Y-%m-%d')
    # test = datetime.strptime('2021-01-28', '%Y-%m-%d')
    days_diff = (datetime.now() - first_day).days + 1
    # print(((days_diff+4)//7))
    day = days_diff - (((days_diff+4)//7) * 2)
    # print(day)



    with open(dir_abs + '/Quotes.csv', 'r') as quotes_file:
        # seed random number generator
        seed(day)
        # prepare a sequence
        sequence = [i for i in range(75900)]
        # make a choice
        selection = choice(sequence)
        daily_quote = quotes_file.readlines()[selection]
        daily_quote = daily_quote.rstrip()
        daily_quote = daily_quote.split(';')
        # print(daily_quote)

    return text.format(day=day, quote=daily_quote[0], by=daily_quote[1], topic=daily_quote[2])


def create_content_ice_breaker():
    text = """
Good Morning Everyone!!!
    
I would like to brighten up the start of your day by sharing a super funny joke. Here you have:

       {joke}

Moreover, I would like to share some wisdom about {topic}. Here you have a super deep and useful quote. Please reflect on it and try to find its meaning and moral.
    
        "{quote}"
        -- {by}
        
    
Any thoughts? I'm sure you can share something interesting!

Have an awesome day! 
    
Best, 
    
    Ali's bot on behalf of Ali :) 
    """

    with open(dir_abs + '/Quotes.csv', 'r') as quotes_file:
        # prepare a sequence
        lines_quote = [i for i in range(75900)]
        # make a choice
        selection_quote = choice(lines_quote)
        daily_quote = quotes_file.readlines()[selection_quote]
        daily_quote = daily_quote.rstrip()
        daily_quote = daily_quote.split(';')
        # print(daily_quote)
    
    # source of jokes: https://github.com/amoudgl/short-jokes-dataset
    with open(dir_abs + '/reddit-cleanjokes.csv', 'r') as jokes_file:
        # choose a line
        lines_joke = [i for i in range(1,1622)]  
        selection_joke = choice(lines_joke)    
        daily_joke = jokes_file.readlines()[selection_joke]
        print(daily_joke)
        daily_joke = daily_joke.split(',', maxsplit=1)
      
    return text.format(joke=daily_joke[1], quote=daily_quote[0], by=daily_quote[1], topic=daily_quote[2])


def create_message(sender, to, subject, message_text, cc=None):
  """Create a message for an email.

  Args:
    sender: Email address of the sender.
    to: Email address of the receiver.
    subject: The subject of the email message.
    message_text: The text of the email message.

  Returns:
    An object containing a base64url encoded email object.
  """
  message = MIMEText(message_text)
  message['to'] = to
  message['from'] = sender
  message['subject'] = subject
  if cc is not None:
      message['cc'] = cc
  # print(base64.urlsafe_b64encode(message.as_string().encode()).decode())
  return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}



def send_message(service, user_id, message):
  """Send an email message.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    message: Message to be sent.

  Returns:
    Sent Message.
  """
  try:
    message = (service.users().messages().send(userId=user_id, body=message).execute())
    print('Message Id: ', message['id'])
    return message
  except HTTPError as error:
    print('An error occurred: ', error)

if __name__ == '__main__':
    main()