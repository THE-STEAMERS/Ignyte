import time
import os
import json
import paho.mqtt.client as mqtt
from inference_sdk import InferenceHTTPClient
from picamera2 import Picamera2

# MQTT Config
MQTT_BROKER = "mqtt.eclipseprojects.io"
MQTT_PORT = 1883
MQTT_TOPIC = "manufacturing/anomalies"

# Roboflow Client
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="sRSPM4kRiPcPF4yGHdzG"
)

# Confidence threshold
damaged_box_threshold = 0.7

# Initialize Camera
picam2 = Picamera2()
picam2.configure(picam2.create_still_configuration())

# Initialize MQTT Client
mqtt_client = mqtt.Client()
mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)

try:
    while True:
        image_path = "captured_image.jpg"
        picam2.start()
        time.sleep(2)
        picam2.capture_file(image_path)
        picam2.stop()
        print("[✅] Image captured:", image_path)

        # Run inference
        result = CLIENT.infer(image_path, model_id="detecting-defected-boxes-xvtve/2")
        print("\n[📊] Inference Result:\n", result)

        # Check predictions for damaged boxes
        for prediction in result.get('predictions', []):
            if prediction['class'] == 'Box' and prediction['confidence'] >= damaged_box_threshold:
                print(f"[🚨] Defective Box Detected with confidence {prediction['confidence']:.2f}")

                # Publish over MQTT
                payload = {
                    "class": prediction['class'],
                    "confidence": prediction['confidence'],
                    "x": prediction['x'],
                    "y": prediction['y'],
                    "width": prediction['width'],
                    "height": prediction['height'],
                    "timestamp": time.time()
                }
                mqtt_client.publish(MQTT_TOPIC, json.dumps(payload))
                print(f"[📤] Published to MQTT: {payload}")

        os.remove(image_path)
        print("[🗑] Temporary image deleted.\n")

        time.sleep(3)

except KeyboardInterrupt:
    print("\n[❌] Stopped by user")

finally:
    mqtt_client.disconnect()