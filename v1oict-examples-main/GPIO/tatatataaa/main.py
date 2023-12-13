from machine import Pin
import time

gpio_pin = Pin(20, Pin.OUT)


def pulse(pin, high_time, low_time):
    """
    Geef een puls op de pin:
    Maak de pin pin_nr hoog, wacht high_time,
    maak de pin laag, en wacht nog low_time
    """

    pin.value(1)
    time.sleep(high_time)
    pin.value(0)
    time.sleep(low_time)

while True:
    pulse(gpio_pin, 0.2, 0.2)
    pulse(gpio_pin, 0.2, 0.2)
    pulse(gpio_pin, 0.2, 0.2)
    pulse(gpio_pin, 1, 1)
    break