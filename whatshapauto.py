"""
1-twilio client setup
2-user input
3-scheduling logic
4-send message
"""
#step=1 install required libraries"""

from twilio.rest import Client
from datetime import datetime,timedelta
import time


#step=2 twilio credentials


account_sid='TWILIO_ACCOUNT_SID=your_actual_sid_here'
auth_token='TWILIO_AUTH_TOKEN=your_actual_token_here'

client = Client(account_sid,auth_token)


#step=3 designe send message function


def send_whatsapp_message(recipient_number,message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f'message sent successfully! message SID{message.sid}')
    except Exception as e:
        print("An error occured")



#step=4 user input
name=input("Enter The Recipient Name = ")
recipient_number=input("Enter the recipient whatsapp number with country code (eg=+918118)=    ")
message_body=input(f'Enter the message you want to send to {name}:')


#step=5 date/time and calculate delay
date_str=input("Enter the date to send the message (yyyy-mm-dd): ")
time_str=input("Enter the time to send the message (HH:MM in 24hour format): ")

#datetime
schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")

current_datetime=datetime.now()

#calculate delay
time_difference=schedule_datetime - current_datetime
delay_seconds=time_difference.total_seconds()

if delay_seconds<=0: 
    print("The specificed time is in past. please enter a future date and time :")
else:
    print(f'message scheduled to be sent to {name} at {schedule_datetime}.')

#wait untill the scheduled time
    time.sleep(delay_seconds)
    send_whatsapp_message(recipient_number,message_body)
