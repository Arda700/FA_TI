from machine import Pin
import time

led_pins = [
    Pin(0, Pin.OUT),
    Pin(1, Pin.OUT),
    Pin(2, Pin.OUT),
    Pin(3, Pin.OUT),
    Pin(4, Pin.OUT)
]

def leds(value, delay):
    for led in led_pins:
        led.value(value & 1)  # Zet de waarde van het laagste bit
        value >>= 1  # Verschuif de bits naar rechts
    time.sleep(delay)

delay = 0.2
while True:
    for i in range(5):
        leds(1 << i, delay)  # Activeer elke LED één voor één van links naar rechts
    for i in range(3, 0, -1):
        leds(1 << i, delay)  # Activeer elke LED één voor één van rechts naar links
