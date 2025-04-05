import argparse
import time
import requests
import cv2
from functools import lru_cache
from picamera2 import MappedArray, Picamera2
from picamera2.devices.imx500 import IMX500

last_detections = []
SERVER_URL = "http://0.0.0.0:5000/qr-data"  
LABEL = "qr-code"  
CONFIDENCE_THRESHOLD = 0.3  # Only process detections with confidence >= 0.3


class Detection:
    def __init__(self, coords, category, conf, metadata):
        """Create a Detection object, recording the bounding box, category, and confidence."""
        self.category = category
        self.conf = conf
        self.box = imx500.convert_inference_coords(coords, metadata, picam2)


def parse_and_draw_detections(request):
    """Analyse the detected objects in the output tensor, draw them, and send QR data."""
    detections = parse_detections(request.get_metadata())
    draw_detections(request, detections)
    send_qr_data(request, detections)  # Now also decodes the QR code


def parse_detections(metadata: dict):
    """Parse the output tensor into detected objects, only keeping valid ones."""
    global last_detections

    np_outputs = imx500.get_outputs(metadata, add_batch=True)
    if np_outputs is None:
        return last_detections

    boxes, scores, classes = np_outputs[0][0], np_outputs[2][0], np_outputs[1][0]
    filtered_detections = [
        Detection(box, category, score, metadata)
        for box, score, category in zip(boxes, scores, classes)
        if score >= CONFIDENCE_THRESHOLD  # ✅ Only keep high-confidence detections
    ]

    last_detections = filtered_detections
    return filtered_detections


def draw_detections(request, detections, stream="main"):
    """Draw only high-confidence detections onto the ISP output."""
    with MappedArray(request, stream) as m:
        for detection in detections:
            x, y, w, h = detection.box
            label = f"{LABEL} ({detection.conf:.2f})"
            cv2.putText(
                m.array,
                label,
                (x + 5, y + 15),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 255, 0),
                1,
            )
            cv2.rectangle(m.array, (x, y), (x + w, y + h), (0, 255, 0), 2)


def decode_qr_code(frame, x, y, w, h):
    """Extracts the QR code from the detected region and decodes it."""
    roi = frame[y : y + h, x : x + w]  # Crop the detected region
    qr_decoder = cv2.QRCodeDetector()
    data, _, _ = qr_decoder.detectAndDecode(roi)  # Try to decode the QR code
    return data if data else None  # Return decoded data or None if not found


def send_qr_data(request, detections):
    """Send only high-confidence QR code detections with decoded data."""
    with MappedArray(request, "main") as m:
        for detection in detections:
            x, y, w, h = detection.box
            qr_data = decode_qr_code(m.array, x, y, w, h)  # Decode the QR code

            if qr_data:  # ✅ Send only if QR code is successfully decoded
                data = {"qr_data": qr_data}
                try:
                    response = requests.post(SERVER_URL, json=data, timeout=2)
                    if response.status_code == 200:
                        print("[✅] QR Data Sent:", response.json())
                    else:
                        print(f"[❌] Failed to send QR data. Status Code: {response.status_code}")
                except requests.exceptions.RequestException as e:
                    print(f"[⚠️] Error sending QR data: {e}")


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, required=True, help="Path of the model")
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()

    # Initialize IMX500 model
    imx500 = IMX500(args.model)
    picam2 = Picamera2()

    imx500.show_network_fw_progress_bar()
    config = picam2.create_preview_configuration(buffer_count=28)
    picam2.start(config, show_preview=True)
    picam2.pre_callback = parse_and_draw_detections

    while True:
        time.sleep(0.5)
