import os
import requests

api_key = "41c61ad44de63527332ef755168f9e6f"
phone_number = input ("Enter the Phone Number which has to be Verified: ")
country_code = "IN"
data = requests.get ('http://apilayer.net/api/validate?access_key={}&number={}&country_code=IN&format=1'.format(api_key,phone_number))
if len(phone_number) == 10:
    print ('DETAILS OF THE PHONE NUMBER:\nLine Type: {}\nPhone Sim: {}\nPhone Location: {}\nPhone Country: {}'.format(data.json()['line_type'],data.json()['carrier'],data.json()['location'],data.json()['country_name']))
elif len(phone_number) == 11:
    print ('DETAILS OF THE PHONE NUMBER:\nLine Type: {}\nPhone Sim: {}\nPhone Location: {}\nPhone Country: {}'.format(data.json()['line_type'],data.json()['carrier'],data.json()['location'],data.json()['country_name']))
else:
    print('ERROR!! Enter a valid phone number')
