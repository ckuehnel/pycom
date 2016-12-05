# MQTT

from network import WLAN
from umqtt import MQTTClient
import machine, time,  os
from mycredentials import SSID,  KEY
from mqtt_credentials import BROKER,  BRPORT,  BRUSER,  BRPWD

print("Running mqtt.py on firmware version %s" % os.uname().release)

adc = machine.ADC()               # create an ADC object
apin = adc.channel(pin='P16')   # create an analog pin on P16 & connect TMP36

def getTemperature():
    value = apin()
    temp = ((value * 1100 ) / 1024 - 500) / 10
    print("Temperature = %5.1f grdC" % (temp))
    return temp

def settimeout(duration): pass

wlan = WLAN(mode=WLAN.STA)
wlan.antenna(WLAN.INT_ANT)
wlan.connect(SSID, auth=(WLAN.WPA2, KEY), timeout=5000)
while not wlan.isconnected(): machine.idle()
print("Connected to Wifi\n")

# client_id, server, port=0, user=None, password=None, keepalive=0,
client = MQTTClient(BRUSER, BROKER, BRPORT, user=BRUSER, password=BRPWD)

client.settimeout = settimeout
client.connect()
while True:
    client.publish("TMP36", str(round(getTemperature(), 1)))
    time.sleep(60)
