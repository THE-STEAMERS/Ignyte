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

## 2. Connect to Pi
- If using a monitor, proceed directly on the terminal
- If using SSH:
  ```bash
  ssh pi@<raspberrypi_ip_address>
  # default password: raspberry

## 3. Initial Configuration
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

## 📸 IMX500 Camera Setup

- Connect the IMX500 to the Raspberry Pi's camera interface
- Ensure the flat flex cable is firmly and correctly inserted
- The camera module should be pre-flashed with Sony's firmware (as per vendor instructions)
- ⚠️ Ensure correct voltage levels and secure physical connections to avoid hardware damage
- Use Sony's runtime tools or vendor SDK to deploy your AI model on the camera.

## 🐍 Python Dependencies
- Update system and install required packages:
  ```bash
  sudo apt update
  sudo apt install imx500-tools 
  sudo apt install python3-opencv python3-munkres python3-picamera2 python3-pil python3-numpy libzbar0 python3-pyzbar python3-requests python3-paho-mqtt

## 🌐 MQTT Configuration
- Set up an MQTT broker:

- Locally (e.g., install Mosquitto)
- Or use a cloud-based broker like HiveMQ or Adafruit IO

- In backend/app/management/commands/mqtt_listener.py, configure:
   - USERNAME = "your superuser name"
   - PASSWORD = "your password"

- The IMX500 will publish QR code and anomaly detection events.
  
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
  │   └── network.rpk             # Your AI model for camera  
  │
  └── setup.md                    # This setup file
```
## ▶️ How to Run the Model
- 1. The rpk file of the model is already created so you can directly run the model in the camera
     For QRDetection model navigate to the folder in rasperry pi os terminal and give the following command
     ```bash
     python app.py --model network.rpk
     ```
     For Damage Detection Model the model runs on cloud so u can directly start the program
     ```bash
     python app.py
- 2. Start Backend Listener
     ```bash
     cd backend/app/management/commands
     python mqtt_listener.py
- 3. Start backend server    
     Refer setup_guide.md in backend folder
- 4. Launch Frontend 
     ```bash
     cd frontend
     npm install
     npm run dev
- Ensure the frontend is configured to subscribe to the same MQTT topic and broker address.

## ✅ Final Checks
- Indicate it's powered and active
- Run a test QR code scan
- Check:

-    MQTT messages received in backend logs
-    Real-time updates on the frontend UI
