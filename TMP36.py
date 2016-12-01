# Measuring temperature by TMP36

import machine

adc = machine.ADC()               # create an ADC object
apin = adc.channel(pin='P16')   # create an analog pin on P16 & connect TMP36

print("")
print("Reading TMP36 Sensor...")
value = apin()
print("ADC count = %d" %(value))

# LoPy  has 1.1 V input range for ADC
temp = ((value * 1100 ) / 1024 - 500) / 10
print("Temperature = %5.1f grdC" % (temp))
