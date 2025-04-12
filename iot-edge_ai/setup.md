# 🛠️ Project Setup Guide - IoT Edge AI with Raspberry Pi and IMX500

Welcome to the **Edge AI Inventory Vision System**. This guide walks you through setting up your Raspberry Pi 4 with the IMX500 camera and other dependencies to run our edge-based AI vision system for inventory monitoring and anomaly detection.

---

## 📦 Hardware Requirements

- Raspberry Pi 4 (4GB or 8GB recommended)
- Sony IMX500 camera module (Raspberry Pi-compatible)
- Micro SD Card (32GB+ recommended)
- Power supply for Pi
- (Optional) Monitor, keyboard, and mouse (for direct setup)
- Internet connection (via Ethernet or Wi-Fi)

> 💡 **Note:** You can set up the Pi either:
> - With a monitor, keyboard, and mouse connected  
> - Or **headless** via **SSH** after enabling it on first boot

---

## 🔧 Software Setup

### 1. Install Raspberry Pi OS
- Download and flash **Raspberry Pi OS (Lite or Desktop)** using [Raspberry Pi Imager](https://www.raspberrypi.com/software/)
- (Optional for SSH) Enable SSH by adding a blank file named `ssh` (no extension) to the `/boot` partition of the SD card
- Insert SD card into Raspberry Pi and power it up

### 2. Connect to Pi
- If using a monitor, proceed directly on the terminal
- If using SSH:
  ```bash
  ssh pi@<raspberrypi_ip_address>
  # default password: raspberry

### 3. Initial Configuration
- Run:
  ```bash
  sudo raspi-config
- Enable the following:
- Camera Interface
- I2C
- SPI
- SSH (if not already)
- Expand filesystem (optional)

- Reboot the Pi after configuration:
  ```bash
  sudo reboot

###📸 IMX500 Camera Setup

- Connect the IMX500 to the Raspberry Pi's camera interface
- Ensure the flat flex cable is firmly and correctly inserted
- The camera module should be pre-flashed with Sony's firmware (as per vendor instructions)
- ⚠️ Ensure correct voltage levels and secure physical connections to avoid hardware damage
- Use Sony's runtime tools or vendor SDK to deploy your AI model on the camera.

###🐍 Python Dependencies
- Update system and install required packages:
  ```bash
  sudo apt update
  sudo apt install imx500-tools 
  sudo apt install python3-opencv python3-munkres python3-picamera2
  pip3 install paho-mqtt

###🌐 MQTT Configuration
- Set up an MQTT broker:

- Locally (e.g., install Mosquitto)
- Or use a cloud-based broker like HiveMQ or Adafruit IO

- In backend/mqtt_listener.py, configure:
  ```bash
  BROKER_ADDRESS = "your_broker_ip"
  PORT = 1883
  TOPIC = "camera/qr"

- The IMX500 will publish QR code and anomaly detection events to this topic.
📂 **Project Structure (Overview)**
  ```bash
  iot-edge_ai/
  │
  ├── backend/
  │   └── mqtt_listener.py        # Listens to IMX500 messages
  │
  ├── frontend/
  │   ├── QRScanner.tsx
  │   └── QRScannerContext.tsx    # React QR UI with MQTT
  │
  ├── model/
  │   └── inventory_model.tflite  # Your AI model for camera  
  │
  └── setup.md                    # This setup file

###▶️ How to Run the Project
- 1. Start MQTT Broker (if local)
  ```bash
  sudo systemctl start mosquitto
- Or run manually:
  ```bash
  mosquitto
- 2. Start Backend Listener
  ```bash
  cd backend
  python3 mqtt_listener.py
- 3. Launch Frontend 
  ```bash
  cd frontend
  npm install
  npm run dev
- Ensure the frontend is configured to subscribe to the same MQTT topic and broker address.

###✅ Final Checks
- Indicate it's powered and active
- Run a test QR code scan
- Check:

-    MQTT messages received in backend logs
-    Real-time updates on the frontend UI
