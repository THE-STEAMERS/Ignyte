🚀 SME Digital Enablement Suite
Empowering UAE SMEs with AI-Driven Automation, IoT Integration, and Seamless Operations

🧩 Overview
This suite is tailored for digitally enabling Small and Medium Enterprises (SMEs) in inventory-driven and trading sectors. It combines modern UI/UX dashboards, a Django-powered intelligent backend, Edge-AI integration using the IMX500 camera module, and an AI chatbot assistant. It streamlines operations, enhances decision-making, automates inventory and supply chain workflows, and integrates with existing ERP systems through custom APIs.

📦 Package Structure
1. 🌐 UI/UX Dashboards (Frontend)
Developed with a React-based interface (deployed on Vercel), each user role has a tailored view:

Manager Dashboard

Real-time inventory overview

Automated order assignment tracking

Reports and analytics

Employee Dashboard

Assigned deliveries & tasks

Status updates on supply completion

Real-time work logs

Retailer Dashboard

Order from live stock view

Track fulfillment progress

Notifications for delays or confirmations

2. 🛠️ Backend (Django + DRF)
Hosted on Render with PostgreSQL (NeonDB), this backend controls:

Order Allocation Engine:
Auto-assigns orders to employees based on real-time load & availability.

Dynamic Inventory Tracking:
Syncs stock updates using data from the IoT system.

REST API Layer:
Role-based secure communication across frontend, chatbot, and future ERP/POS integrations.

3. 📦 IoT Edge-AI Module (IMX500 + Raspberry Pi 4)
A plug-and-play AI vision unit using Sony’s IMX500 camera running models on-device:

Features:

QR code scanning for item tracking

Anomaly detection (damaged boxes, mismatches)

Realtime event push via MQTT to backend

Hardware Stack:

Raspberry Pi 4 (4GB/8GB)

Sony IMX500 camera module

32GB+ microSD card

Optional monitor/keyboard for setup (also supports headless SSH)

Software Stack:

Raspberry Pi OS

Python (OpenCV, imx500-tools, paho-mqtt)

MQTT Broker (Mosquitto or cloud-based)

Deployment:
The camera publishes data (QR scans or anomalies) to a broker, which the backend consumes using mqtt_listener.py.

Frontend Integration:
React components subscribe to the broker and reflect live events.

➡️ See iot-edge_ai/setup.md for complete setup instructions and running steps.

4. 🤖 AI Chatbot (In Progress)
An intelligent assistant embedded into dashboards:

For Managers:

"Show all low stock items"

"Who is handling Order #105?"

For Retailers:

"Track my order"

"What's the estimated delivery?"

For Employees:

"What’s my next delivery?"

"List today’s assigned tasks"

Built with: Rasa or DeepseekAI API.

🚀 Key Features at a Glance
Feature	Description
✅ Automated Order Allocation	Real-time employee assignment logic
✅ Dynamic Inventory Management	Stock updates from real-world supply data
✅ Edge-AI Powered Detection	IMX500 camera with on-device inference
✅ AI Chatbot Assistance	Conversational task handling (WIP)
✅ Modular API-Driven Backend	Easily pluggable with third-party tools
✅ Role-Based Frontend Dashboards	Cleaner UX per stakeholder
📂 Tech Stack
Frontend: React, Tailwind, MQTT.js (Vercel-hosted)

Backend: Django, DRF, Python, Gunicorn (Render-hosted)

Database: PostgreSQL (NeonDB)

IoT + AI: Raspberry Pi 4, Sony IMX500, Python, OpenCV, TFLite

Chatbot: Rasa / DeepseekAI API (WIP)

Deployment Tools: Docker, Mosquitto, Nginx

