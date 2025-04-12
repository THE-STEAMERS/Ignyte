# SME Digital Enablement Suite 🚀  
Empowering UAE SMEs with AI-Driven Automation, IoT Integration, and Seamless Operations
## 🧩 Overview
This comprehensive package is designed to digitally enable Small and Medium Enterprises (SMEs) in the **trading and inventory-based sectors**. It brings together **modern UI/UX dashboards**, a **Django-powered intelligent backend**, **IMX500 edge-AI integration** for quality control, and an **AI Chatbot** to streamline operations, enhance decision-making, and improve employee-customer-manager experiences,automates inventory, accounting, and supply chain tasks, and connects seamlessly to existing ERP systems via custom APIs.
---
## 📦 Package Structure
### 1. 🌐 UI/UX Dashboards
Designed with usability in mind, each user type gets a dedicated role-based interface:
- **Manager Dashboard (Inventory Overview & Control):**
 - Real-time stock levels
 - Order alerts and auto-assignments
 - Reports and analytics view
- **Employee Dashboard (Supply Operations):**
 - Assigned tasks and delivery schedule
 - Status updates for order fulfillment
 - Real-time instructions and reporting interface
- **Retailer Dashboard (Buyer Interaction Portal):**
 - Place orders from available stock
 - Track order status
 - Instant notifications on fulfillment/delays
---
### 2. 🛠️ Backend Package (Django)
Built on Django, this backend handles all logic, communication, and automation:
- **Automatic Order Allocation System:**
 - Orders placed by retailers are automatically assigned to available employees based on workload and location.
 
- **Stock Management System:**
 - Intelligent stock updates triggered by real-time supply completion.
 - Stock levels update dynamically without manual intervention.
- **API Suite:**
 - All UI dashboards communicate with Django via secure REST APIs.
 - Future integrations (POS, ERP) are supported via modular endpoints.
---
### 3. 📦 IoT Edge-AI Package (IMX500 Integration)
An AI-powered edge system using the **Sony IMX500 sensor** for vision-based intelligence:
- **QR Code & Box Detection:**
 - Detects, verifies, and tracks packages using AI model deployed on-device.
 
- **Defect & Mismatch Detection:**
 - Identifies damaged/mispacked items before delivery.
 
- **Edge Analytics & Communication:**
 - Sends data securely to the backend via MQTT/HTTP.
 - Low-latency processing enables real-time decisions.
---
### 4. 🤖 AI Chatbot Package (Under development)
An AI Assistant embedded across dashboards to support all roles:
- **Manager View:**
 - "Show low stock items"  
 - "Who is handling Order #1021?"
- **Retailer View:**
 - "Track my order"
 - "Expected delivery time?"
- **Employee View:**
 - "Where do I deliver next?"  
 - "Show today's task list"
**Built with:** Rasa.
---
## 🚀 Features At a Glance
| Feature                             | Description |
|-------------------------------------|-------------|
| ✅ Fully Automated Order Allocation | Employees are assigned orders based on live metrics |
| ✅ Real-Time Inventory Management   | Dynamic stock update using IoT and supply data |
| ✅ Edge-AI Powered Vision           | On-device detection using IMX500 |
| ✅ AI Chatbot Support               | Contextual help & task assistance |
| ✅ Scalable & Modular Backend       | Easily extendable via APIs |
| ✅ Clean UI for Each Stakeholder    | Role-specific dashboards to improve usability |
---
## 📂 Tech Stack
- **Frontend:** HTML, CSS, JavaScript (React or Bootstrap-based UI)
- **Backend:** Django, Django REST Framework
- **Database:** PostgreSQL
- **IoT/AI:** IMX500, OpenCV, Edge AI Models (YOLOv5, MobileNet)
- **Chatbot:** DeepseekAI API / Dialogflow / Rasa
- **Deployment:** Docker, Nginx, Gunicorn (for production setup)
---

> **Note:** Setup guides have been added to their respective directories:
> - Frontend setup guide is available in `frontend/setup.md`
> - IoT Edge AI setup guide is available in `iot_edge_ai/setup.md`
