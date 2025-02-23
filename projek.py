from machine import Pin
import time
import dht
import ujson
import network
import requests

FLASK_SERVER_URL = 'http://192.168.1.100:5000/receive_data' # Ganti IP Address dengan IP Address Flask Server
SSID = ""
PASSWORD = ""

sensor = dht.DHT11(Pin(2))
led = Pin(5, Pin.OUT)
pir = Pin(4, Pin.IN)

motion_count = 0
motion_detected = 0
motion_stopped_printed = False

prev_weather = {
    "temp": 0,
    "humidity": 0,
}

def handle_interrupt(pin):
    global motion_detected
    motion_detected = pin.value()
    if motion_detected:
        led.value(1)
    else:
        led.value(0)
        
pir.irq(trigger=(Pin.IRQ_RISING | Pin.IRQ_FALLING), handler=handle_interrupt)

def check_wifi():
    print("Connecting to WiFi...", end="")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect(SSID, PASSWORD)
    while not sta_if.isconnected():
        print(".", end="")
        time.sleep(1)
    print("Connected!")

def build_payload():
    global motion_count
    global motion_stopped_printed
    
    if motion_detected and not motion_stopped_printed:
        print("Motion Detected!")
        motion_count += 1
        motion_stopped_printed = True
    elif not motion_detected and motion_stopped_printed:
        print("Motion Stopped!")
        motion_stopped_printed = False  

    print("Mengukur kondisi cuaca...\n", end="")
    sensor.measure()
    temp = sensor.temperature()
    humidity = sensor.humidity()
    
    message = {
        "temp": temp,
        "humidity": humidity,
    }
    
    print(message)
    
    if ujson.dumps(message) != ujson.dumps(prev_weather):
        print("Updated!")
        prev_weather = message
    else:
        print("Tidak ada perubahan")
    
    payload = {
        "motion_count": motion_count,
        "temperature": temp,
        "humidity": humidity,
    }
    
    return payload

def post_request(payload):
    headers = {"Content-Type": "application/json"}
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        try:
            req = requests.post(url=FLASK_SERVER_URL, headers=headers, json=payload)
            status = req.status_code
            attempts += 1
            time.sleep(2)
        except Exception as e:
            print(f"[ERROR] Exception occurred: {e}")
            status = 500
    if status >= 400:
        print("[ERROR] Could not send data after 5 attempts, please check your Flask server and internet connection")
        return False
    print("[INFO] Request made properly, your device is updated")
    time.sleep(0.5)
    return True

def main():
    try:
        check_wifi()
        payload = build_payload()
        post_request(payload)
        time.sleep(2)
        print("Data Sent!")

    except KeyboardInterrupt:
        print("Keyboard Interrupt")
        pir.irq(trigger=0)
        led.value(0)

    except Exception as e:
        print("An Unexpected error occurred:", e)

if __name__ == "__main__":
    while True:
        main()
        time.sleep(5)