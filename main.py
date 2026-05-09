import twilio.rest
import requests
import os

#-------------------------- CONFIG API CLIMA --------------------------------------------------------
apikey = os.environ.get("OWM_API_KEY")
apidoor = "https://api.openweathermap.org/data/2.5/forecast"
latitud = 39.889622
longitud = 4.264240

parameters = {
    "lat": latitud,
    "lon": longitud,
    "appid": apikey,
    "cnt": 4,#solamente coge las cuatro primeras horas
    "units": "metric",
    "lang": "es",
}

respuesta = requests.get(url=apidoor, params=parameters)
respuesta.raise_for_status()

data = respuesta.json()
#-------------------------- CONFIG API SMS --------------------------------------------------------


account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")


lluvia = False
for d in data["list"]:
    if int(d["weather"][0]["id"]) < 700:
        lluvia = True
if lluvia:
    client = twilio.rest.Client(account_sid, auth_token)
    #BLOQUE PARA MANDAR SMS
    # message = client.messages.create(
    # messaging_service_sid='MG0b7f295e3c1f8333a2f5fbcf9fa938c4',
    #     body='Está lloviendo. Coge el paraguas ☔',
    #     to='+34606530438'
    # )
    #BLOQUE PARA MANDAR WHATSAPP
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        content_sid='HXb5b62575e6e4ff6129ad7c8efe1f983e',
        body='Está lloviendo. Coge el paraguas ☔',
        to='whatsapp:+34606530438'
    )
    #print(message.status)
    print("Lloviendo")
