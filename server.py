from flask import Flask, request, jsonify
from db import connect_mongo
import requests

app = Flask(__name__)

uri = "mongodb+srv://muhammadrafathrai:1snwDUNtakj0P5tY@clusteruni268.8hl4j.mongodb.net/?retryWrites=true&w=majority&appName=ClusterUNI268"
db = "db_Uni268"
collection = "collection_Uni268"

client = connect_mongo(uri, db, collection)

my_collection = client[db][collection]

UBIDOTS_TOKEN = "BBUS-NYDCvqxBKjKJwImVr9gMrSZ22IsMCR"
UBIDOTS_DEVICE_LABEL = "esp32-uni268"

@app.route('/receive_data', methods=['POST'])
def receive_data():
    try:
        data = request.json
        temperature = data.get('temperature')
        humidity = data.get('humidity')
        motion_count = data.get('motion_count')

        if temperature is None or humidity is None or motion_count is None:
            return jsonify({"error": "Missing temperature, humidity, or motion_count"}), 400

        print(f"[INFO] Received data - Temperature: {temperature}, Humidity: {humidity}, Motion Count: {motion_count}")

        ubidots_url = f"http://industrial.api.ubidots.com/api/v1.6/devices/{UBIDOTS_DEVICE_LABEL}"
        headers = {"X-Auth-Token": UBIDOTS_TOKEN, "Content-Type": "application/json"}
        payload = {
            "temperature": temperature,
            "humidity": humidity,
            "motion_count": motion_count
        }
        
        my_collection.insert_one(data)
        
        response = requests.post(ubidots_url, headers=headers, json=payload)
        if response.status_code >= 400:
            print(f"[ERROR] Failed to forward data to Ubidots: {response.status_code}")
            return jsonify({"error": "Failed to forward data to Ubidots"}), 500

        return jsonify({"message": "Data received and processed successfully"}), 200

    except Exception as e:
        print(f"[ERROR] Exception occurred: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)