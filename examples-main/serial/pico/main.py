# Importeer de vereiste modules
from machine import Pin, ADC, UART
import time

# Configureer on-board led
led = Pin(25, Pin.OUT)

# Configureer ADC voor het lezen van de interne temperatuursensor
adc = ADC(4)  # Gebruik ADC-kanaal 4 voor de interne temperatuursensor

# Configureer UART voor seriele communicatie
uart = UART(0, baudrate=115200, tx=Pin(0), rx=Pin(1))

# Knipper de led om een succesvolle flits aan te geven
for _ in range(5):
    led(0)
    time.sleep(.1)
    led(1)
    time.sleep(.1)

# Wacht op gegevens van de verbinding
while True:
    data = input()

    print("Received '" + data + "'.")
    if data == '0':
        print("Turning led off.")
        led(0)
    elif data == '1':
        print("Turning led on.")
        led(1)
    elif data == '2':
        # Lees de interne temperatuursensor en stuur de temperatuur terug via UART
        voltage = adc.read_u16() * (3.3 / 65535)
        temperature = 27 - (voltage - 0.706) / 0.001721
        uart.write("{:.2f}\r\n".format(temperature))
        print("Temperature sent:", temperature)
    else:
        print("Unknown command.")
