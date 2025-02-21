from machine import Pin
import time
from umqtt.simple import MQTTClient
import dht
import ujson
import network

sensor = dht.DHT11(Pin(2))
led = Pin(5, Pin.OUT)
pir = Pin(4, Pin.IN)

motion_detected = False
motion_stopped_printed = False
prev_weather = ""  

def handle_interrupt(pin):
    global motion_detected
    if pin.value() == 1:
        motion_detected = True
        led.value(1)
    else:
        motion_detected = False
        led.value(0)

pir.irq(trigger=(Pin.IRQ_RISING | Pin.IRQ_FALLING), handler=handle_interrupt)

try:
    while True:
        if motion_detected and not motion_stopped_printed:
            data = {
                "message": "Motion Detected",
                "status": motion_detected
            }
            #msg = ujson.dumps(data)
            print("Motion Detected!")
            print(data)
            motion_stopped_printed = True
        elif not motion_detected and motion_stopped_printed:
            print("Motion Stopped!")
            motion_stopped_printed = False  

        print("Mengukur kondisi cuaca...\n", end="")
        sensor.measure()
        message = {
            "temp": sensor.temperature(),
            "humidity": sensor.humidity(),
        }
        print(message)
        
        if message != prev_weather:
            print("Updated!")
            prev_weather = message
        else:
            print("Tidak ada perubahan")

        time.sleep(2)

except KeyboardInterrupt:
    print("Keyboard Interrupt")
    pir.irq(trigger=0)
    led.value(0)

except Exception as e:
    print("An Unexpected error occurred:", e)
