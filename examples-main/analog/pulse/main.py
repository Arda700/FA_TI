from machine import ADC, Pin
import time

led = Pin(20, Pin.OUT)
adc = ADC(Pin(26))

def pulse(pin, duration):
    """
    Geef een puls op de pin:
    Maak de pin hoog voor de opgegeven duur.
    """

    pin.on()
    time.sleep(duration)
    pin.off()

while True:
    adc_value = adc.read_u16()

    scaled_adc = adc_value / 65535.0

    pulse_time = scaled_adc

    pulse(led, pulse_time)
    time.sleep(1)
