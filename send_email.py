from __future__ import print_function
import pickle
from os import path,environ
# from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request
# from google.oauth2 import service_account, credentials
from email.mime.text import MIMEText
import base64
# from urllib.error import HTTPError

from random import seed, choice
from dotenv import load_dotenv
import schedule
import time
import smtplib, ssl
from create_content.ice_breaker import create_content_ice_breaker
from create_content.nikhil import create_content_nikhil
from create_content.german import create_content_german
from create_content.nacho import create_content_nacho
load_dotenv()
 



# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.compose']
sender = environ.get('SENDER')
receiver = environ.get('RECEIVER')
receiver_cc = environ.get('RECEIVER_CC')
receiver_german = environ.get('RECEIVER_GERMAN')
receiver_german_cc = environ.get('RECEIVER_GERMAN_CC')
sender_nacho = environ.get('RECEIVER_NACHO') 
receiver_nacho = environ.get('RECEIVER_NACHO') 
email_password = environ.get('EMAIL_PASSWORD')    

# print(path.dirname(__file__))
dir_abs = path.dirname(__file__)
dir_abs = dir_abs + '/' if len(dir_abs) > 0 else dir_abs


def main():

    print('starting')
    schedule.every().monday.at("07:30").do(send_email)
    #schedule.every(5).minutes.do(send_email)
    # send_email()

       
    # while True:
    #   schedule.run_pending()
    #   time.sleep(100)
 




def send_email():

    port = 465  # For SSL

    # Create a secure SSL context
    context = ssl.create_default_context()
    
    # send email - ice breaker
    # subject = 'Good morning!'
    # message_text = create_content_ice_breaker(dir_abs)
    print('sending icebreaker email')
    #print(message_text)
    # message_1 = create_message(sender, receiver, subject, message_text, cc=receiver_cc, parse_html=True)

    # send email - german idiom
    # message_text_german = create_content_german(dir_abs)
    # print('sending german email')
    #print(message_text_german)
    # subject_german = "Kein Problem!!"
    # message_2 = create_message(sender, receiver_german, subject_german, message_text_german, cc=receiver_cc, parse_html=True)

    # send email - Nacho
    message_text_nacho = create_content_nacho(dir_abs)
    print('sending nacho email')
    #print(message_text_german)
    subject_nacho = "Felices 18 Nacho!"
    message_3 = create_message(sender_nacho, receiver_nacho, subject_nacho, message_text_nacho, cc=receiver_cc, parse_html=True)


    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, email_password)
        # server.sendmail(sender, receiver.split(',') + receiver_cc.split(',') , message_1)
        # server.sendmail(sender, receiver_german.split(',') + receiver_cc.split(',') , message_2)
        server.sendmail(sender, receiver_german.split(',') + receiver_cc.split(',') , message_3)









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
  return message.as_string()



if __name__ == '__main__':
    main()