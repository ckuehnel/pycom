# Init WLAN  STA Mode

import network
import time
import mycredentials

# setup as a station
wlan = network.WLAN(mode=WLAN.STA)
wlan.connect(credentials.SSID, auth=(WLAN.WPA2,credentials.KEY))

print("Try to connect...")
while not wlan.isconnected():
    time.sleep_ms(100)
    print(".",  end="")

print("")   
print("Connected.")
print('IP address:', wlan.ifconfig()[0])

while True:
    for i in range(0, 40):
        print(".",  end="")
        time.sleep(1)
    print("")
