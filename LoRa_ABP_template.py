# LoRa_ABP.py
# LoPy LoRaWAN Node measures temperature by TMP36 sensors and sends data to TTN
# 2017-05-06 Claus Kuehnel info[at]ckuehnel.ch

import network
from network import LoRa
import socket
import binascii
import struct
import pycom
import utime   
import machine

pycom.heartbeat(False)

adc = machine.ADC()               # create an ADC object
apin = adc.channel(pin='P16')   # create an analog pin on P16 & connect TMP36

# Initialize LoRa in LORAWAN mode.
lora = LoRa(mode=LoRa.LORAWAN)

# create an ABP authentication params
dev_addr = struct.unpack(">l", binascii.unhexlify('<Your DevAddr>'.replace(' ','')))[0]
nwk_swkey = binascii.unhexlify('<Your network key>'.replace(' ',''))
app_swkey = binascii.unhexlify('<Your app key'.replace(' ',''))

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
