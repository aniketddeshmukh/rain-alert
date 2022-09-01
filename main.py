LAT = "19.076090"
LON = "72.877426"

import requests
from twilio.rest import Client
import creds #file containing all API keys


response = requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall?lat={LAT}&lon={LON}&appid={creds.API_KEY}&exclude=current,minutely,daily")
print(response.raise_for_status())
q = response.json()
A=[]
for j in range(6):
    code = int(q["hourly"][j]["weather"][0]["id"])
    A.append(code)
    if code <700:
        client = Client(creds.account_sid, creds.auth_token)
        message = client.messages.create(
            body="It's going to rain today. Remember to take an ☔",
            from_='+155555555',
            to='+919999999999'
        )
        print(message.sid)
        break

