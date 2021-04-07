from __future__ import print_function
import pickle
from os import path,environ
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2 import service_account, credentials
from email.mime.text import MIMEText
import base64
from urllib.error import HTTPError
from datetime import datetime
from random import seed, choice
from dotenv import load_dotenv
import schedule
import time

load_dotenv()
 



# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.compose']
sender = environ['SENDER']
receiver = environ['RECEIVER']
receiver_cc = environ['RECEIVER_CC']
receiver_german = environ['RECEIVER_GERMAN']
receiver_german_cc = environ['RECEIVER_GERMAN_CC']
refresh_token_var = environ['REFRESH_TOKEN']
token_uri = environ['TOKEN_URI']
client_id = environ['CLIENT_ID']
client_secret = environ['CLIENT_SECRET']
    


dir_abs = path.dirname(__file__)
dir_abs = dir_abs + '/' if len(dir_abs) > 0 else dir_abs


def main():

    print('starting')
    schedule.every().day.at("07:30").do(send_email)
    #schedule.every(5).minutes.do(send_email)
    #send_email()

       
    while True:
      schedule.run_pending()
      time.sleep(1)
 








def send_email():

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if path.exists(dir_abs + 'token.pickle'):
        with open(dir_abs + 'token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        elif refresh_token_var:
          print('using refresh tocket for OAUTH')
          creds = credentials.Credentials(None,refresh_token=refresh_token_var, token_uri=token_uri, client_id=client_id, client_secret=client_secret)
          creds.refresh(Request())
        else:
            print(dir_abs + '/credentials.json')
            flow = InstalledAppFlow.from_client_secrets_file(
                dir_abs + 'credentials.json', SCOPES)
            creds = flow.run_local_server(port=8080)

        # Save the credentials for the next run
        with open(dir_abs + 'token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)
    # send email - ice breaker
    subject = 'Good morning!'
    message_text = create_content_ice_breaker()
    print('sending icebreaker email')
    #print(message_text)
    message_1 = create_message(sender, receiver, subject, message_text, cc=receiver_cc, parse_html=True)
    send_message(service, 'me', message_1)
    
    # send email - german idiom
    message_text_german = create_content_german()
    print('sending german email')
    #print(message_text_german)
    subject_german = "Kein Problem!!"
    message_2 = create_message(sender, receiver_german, subject_german, message_text_german, cc=receiver_cc, parse_html=True)
    send_message(service, 'me', message_2)






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



    with open(dir_abs + 'Quotes.csv', 'r') as quotes_file:
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
    font_family = "'Open Sans','Helvetica Neue',Helvetica,Arial,sans-serif"
    text = """

    <div style="margin-left:20%; margin-right:20%">
    <h4 style="font-family:{font_family};font-size:20px;font-style:normal;font-weight:bold;line-height:150%;letter-spacing:1px;text-align:center">Good Morning Everyone!!!</h4>

    <p style="text-align: center;"><img src="https://img.icons8.com/doodle/96/000000/sun--v1.png"/>
    <p style="font-family:{font_family};font-size:18px;font-style:normal;font-weight:normal;line-height:100%;letter-spacing:1px;text-align:center">I would like to brighten up the start of your day by sharing a super funny joke. Here you have:<span>&nbsp;</span></p>
    <hr style="text-align:center;color:gray;border: 0 none;border-top:dotted 1px;">
    <p style="text-align: center;"><img src="https://img.icons8.com/doodle/96/000000/garland.png"/>
 
    <p style="color:#43404d;font-family:{font_family};font-size:16px;font-style:italic;font-weight:normal;line-height:120%;letter-spacing:2px;text-align:center"><span>{joke}</span></p>

    <hr style="text-align:center;color:gray;border: 0 none;border-top:dotted 1px;">

    
    <p style="font-family:{font_family};font-size:18px;font-style:normal;font-weight:normal;line-height:100%;letter-spacing:1px;text-align:center">Moreover, I would like to share some wisdom about <strong> {topic} </strong>. Here you have a super deep and useful quote. Please reflect on it and try to find its meaning and moral.<span>&nbsp;</span></p>
    <hr style="text-align:center;color:gray;border: 0 none;border-top:dotted 1px;">
    <p style="text-align: center;"><img src="https://img.icons8.com/bubbles/100/000000/comments.png"/>

    <p style="color:#43404d;font-family:{font_family};font-size:16px;font-style:italic;font-weight:normal;line-height:120%;letter-spacing:2px;text-align:center"><span>"{quote}"</span></p>
    <p style="color:#43404d;font-family:{font_family};font-size:16px;font-style:normal;font-weight:normal;line-height:120%;letter-spacing:2px;text-align:center"><span>-- {by}</span></p>

    <hr style="text-align:center;color:gray;border: 0 none;border-top:dotted 1px;">

    <p style="text-align: center;"><img src="https://img.icons8.com/officel/80/000000/idea.png"/>
    <p style="font-family:{font_family};font-size:18px;font-style:normal;font-weight:normal;line-height:100%;letter-spacing:1px;text-align:center">Any thoughts? I'm sure you can share something interesting!<span>&nbsp;</span></p>

   
    <p style="font-family:{font_family};font-size:18px;font-style:normal;font-weight:normal;line-height:100%;letter-spacing:1px;text-align:center">Have an awesome day! <span>&nbsp;</span></p>

    <p style="font-family:{font_family};font-size:18px;font-style:normal;font-weight:normal;line-height:100%;letter-spacing:1px;text-align:center">Ali's bot on behalf of Ali :) <span>&nbsp;</span></p>
    </div>
    """



    with open(dir_abs + 'Quotes.csv', 'r') as quotes_file:
        # prepare a sequence
        lines_quote = [i for i in range(75900)]
        # make a choice
        selection_quote = choice(lines_quote)
        daily_quote = quotes_file.readlines()[selection_quote]
        daily_quote = daily_quote.rstrip()
        daily_quote = daily_quote.split(';')
        # print(daily_quote)
    
    # source of jokes: https://github.com/amoudgl/short-jokes-dataset
    with open(dir_abs + 'reddit-cleanjokes.csv', 'r') as jokes_file:
        # choose a line
        lines_joke = [i for i in range(1,1622)]  
        selection_joke = choice(lines_joke)    
        daily_joke = jokes_file.readlines()[selection_joke]
        daily_joke = daily_joke.split(',', maxsplit=1)
      
    return text.format(font_family=font_family, joke=daily_joke[1], quote=daily_quote[0], by=daily_quote[1], topic=daily_quote[2])


def create_content_german():
    font_family = "'Open Sans','Helvetica Neue',Helvetica,Arial,sans-serif"
    text = '''
    <div style="margin-left:10%; margin-right:10%">
    <h4 style="font-family:{font_family};font-size:20px;font-style:normal;font-weight:bold;line-height:150%;letter-spacing:1px;text-align:center">Hallo Blanchis Burger!</h4>
    <p style="text-align: center;"><img src="https://img.icons8.com/doodle/96/000000/sun--v1.png"/>
    <p style="font-family:{font_family};font-size:18px;font-style:normal;font-weight:normal;line-height:100%;letter-spacing:1px;text-align:center">Ich m&ouml;chte dass wir perfekt Deutsch sprechen k&ouml;nnen. Daf&uuml;r m&uuml;ssen wir viele Redewendungen lernen.<span>&nbsp;</span></p>

    <p style="color:#43404d;font-family:{font_family};font-size:16px;font-style:normal;font-weight:normal;line-height:100%;letter-spacing:2px;text-align:center"><span>UNTEN FINDEST DU DIE HEUTIGEN REDEWENDUNGEN:</span></p>
    
    <hr style="text-align:center;color:gray;border: 0 none;border-top:dotted 1px;">

    <p style="color:#4485b8;font-family:{font_family};font-size:20px;font-style:normal;font-weight:bold;line-height:100%;text-align:center"><span>{idiom}</span></p>
    
    <hr style="text-align:center;color:gray;border: 0 none;border-top:dotted 1px;">

    <p style="color:#43404d;font-family:{font_family};font-size:16px;font-style:normal;font-weight:bold;line-height:100%;letter-spacing:1px;text-align:center"><span>W&ouml;rtliche &Uuml;bersetzung:</span></p>
    <p style="color:#43404d;font-family:{font_family};font-size:16px;font-style:normal;font-weight:normal;line-height:100%;letter-spacing:1px;text-align:center"><em>{literal_translation}</em></p>
    <p style="color:#43404d;font-family:{font_family};font-size:16px;font-style:normal;font-weight:bold;line-height:100%;letter-spacing:1px;text-align:center"><span>Englische &Uuml;bersetzung:</span></p>
    <p style="color:#43404d;font-family:{font_family};font-size:16px;font-style:normal;font-weight:normal;line-height:100%;letter-spacing:1px;text-align:center"><em>{english_translation}</em></p>
    <p style="color:#43404d;font-family:{font_family};font-size:16px;font-style:normal;font-weight:bold;line-height:100%;letter-spacing:1px;text-align:center"><span><b class="b5">Spanische</b> &Uuml;bersetzung:</span></p>
    <p style="color:#43404d;font-family:{font_family};font-size:16px;font-style:normal;font-weight:normal;line-height:100%;letter-spacing:1px;text-align:center"><em>{spanish_translation}</em></p>
    
    <hr style="text-align:center;color:gray;border: 0 none;border-top:dotted 1px;width:80%"">
    <p style="text-align: center;"><img src="{image}" alt= "" width="70%" height="auto""img" />
    
    <hr style="text-align:center;color:gray;border: 0 none;border-top:dotted 1px;"">
    
    <p style="font-family:{font_family};font-size:18px;font-style:normal;font-weight:normal;line-height:100%;letter-spacing:1px;text-align:center">Ich w&uuml;nsche dir einen sch&ouml;nen Tag!</p>
    <p style="font-family:{font_family};font-size:18px;font-style:normal;font-weight:normal;line-height:100%;letter-spacing:1px;text-align:center">Ali's german bot :)&nbsp;</p>
    <p></p>

    </div>
    '''
    # get index for idiom
    first_day = datetime.strptime('2021-04-07', '%Y-%m-%d')
    days_diff = (datetime.now() - first_day).days + 1
    #print(days_diff)

    with open(dir_abs + 'german_idioms.csv', 'r') as german_idioms:
        daily_idiom= german_idioms.readlines()[days_diff]
        daily_idiom = daily_idiom.split(';')



    return text.format(font_family=font_family, idiom=daily_idiom[0], literal_translation=daily_idiom[1], english_translation=daily_idiom[2], spanish_translation=daily_idiom[3], image=daily_idiom[4])




def create_message(sender, to, subject, message_text, cc=None, parse_html=False):
  """Create a message for an email.

  Args:
    sender: Email address of the sender.
    to: Email address of the receiver.
    subject: The subject of the email message.
    message_text: The text of the email message.

  Returns:
    An object containing a base64url encoded email object.
  """
  if parse_html is True:
    message = MIMEText(message_text, 'html')
  else:
    message = MIMEText(message_text)
  
  message['to'] = to
  message['from'] = sender
  message['subject'] = subject
  if cc is not None:
      message['cc'] = cc
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