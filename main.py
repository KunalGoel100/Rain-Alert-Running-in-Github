import requests
import os
from twilio.rest import Client

ApiKey = os.environ.get("APIKEY")
address = "https://api.openweathermap.org/data/2.5/forecast"

param = {"lat":28.704060,
         "lon":77.102493,
         "cnt":1,
         "appid":"8f3464385339a75ee7d59e18b8e6e7bb"
         }
Forecast = ""
response = requests.get(url=address,params=param)
data = response.json()["list"]
day = data[0]
if day["weather"][0]["id"] < 300:
    Forecast = "ThunderStormy"
elif day["weather"][0]["id"] < 400:
    Forecast = "Drizzly"
elif day["weather"][0]["id"] < 600:
    Forecast = "Rainy"
elif day["weather"][0]["id"] < 700:
    Forecast = "Snowy"
elif day["weather"][0]["id"] >= 800:
    Forecast = "Cloudy"
else:
    pass
print(Forecast)

Actual_SID = os.environ.get("ACTUAL_SID")
Actual_Token = os.environ.get("ACTUAL_TOKEN")
Actual_Number = "whatsapp:+14155238886"
Actual_Receiver_Number = "whatsapp:+919743718133"

client = Client(Actual_SID,Actual_Token)
message = client.messages.create(
    body = f"Wats up, The weather forecast by Kunal, for you is, {Forecast}! ",
    from_ = Actual_Number,
    to = Actual_Receiver_Number
)
print(message.status)
