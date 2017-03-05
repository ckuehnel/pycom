import network
from network import WLAN
from network import LoRa
import socket
import binascii
import struct
import pycom
import utime   
import machine
import time

# Credentials for WLAN
SSID = 'FRITZ!Box Fon WLAN 7390'
KEY  = '6610601496452117'

# setup as a station
wlan = network.WLAN(mode=WLAN.STA)
wlan.connect(SSID, auth=(WLAN.WPA2,KEY))

print("Try to connect...")
while not wlan.isconnected():
    time.sleep_ms(100)
    print(".",  end="")

print("")   
print("Connected.")
print('IP address:', wlan.ifconfig()[0])

pycom.heartbeat(False)

adc = machine.ADC()               # create an ADC object
apin = adc.channel(pin='P16')   # create an analog pin on P16 & connect TMP36

# Initialize LoRa in LORAWAN mode.
lora = LoRa(mode=LoRa.LORAWAN)

# create an ABP authentication params
dev_addr = struct.unpack(">l", binascii.unhexlify('26011911'.replace(' ','')))[0]
nwk_swkey = binascii.unhexlify('08C37FEF034277CD7F7E2063E174B968'.replace(' ',''))
app_swkey = binascii.unhexlify('653064AAAECF140CB11EB882535E1549'.replace(' ',''))

# join a network using ABP (Activation By Personalization)
lora.join(activation=LoRa.ABP, auth=(dev_addr, nwk_swkey, app_swkey))

while not lora.has_joined():
    print('Trying to join LoRaWAN network')
    utime.sleep(1)
    pass
print('Joined LoRaWAN Network')

pycom.rgbled(0x00ff00)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)
count=0

while True:
    value = apin()

    # LoPy  has 1.1 V input range for ADC
    temp = ((value * 1100 ) / 1024 - 500) / 100
    print("Temperature = %5.1f *C" % (temp))
    print('Sending Packet')
    msg = repr(round(temp, 1)) + ' *C'''
    #print(msg)
    s.send(msg)
    count = count+1
    print('Done sending - %d' %(count))
    pycom.rgbled(0x00ffff)
    utime.sleep_ms(10)
    pycom.rgbled(0x00000)
    utime.sleep(60)
