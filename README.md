# Samsung Innovation Campus Stage 2 - IoT Project  
*Team Barudak Depok Baik Hati dan Rajin Menabung*  

Welcome to our IoT project repository! This project is part of the **Samsung Innovation Campus Stage 2** program, where we applied Design Thinking, IoT development, and collaborative tools to create a meaningful solution. Our project focuses on using a **PIR Motion Sensor** and **DHT11 Temperature & Humidity Sensor** to monitor environmental conditions and detect motion in real-time. The data is visualized using **Ubidots**, an IoT platform.

---

## Table of Contents  
1. [Project Overview](#project-overview)  
2. [Hardware Components](#hardware-components)  
3. [Software Tools](#software-tools)  
4. [Setup Instructions](#setup-instructions)  
5. [How It Works](#how-it-works)  
6. [Screenshots/Demo](#screenshotsdemo)  
7. [Team Members](#team-members)  
8. [Acknowledgments](#acknowledgments)  

---

## Project Overview  
Our IoT project aims to monitor environmental conditions (temperature and humidity) and detect motion in a specific area. The system uses:  
- **PIR Motion Sensor**: Detects movement and sends alerts when motion is detected.  
- **DHT11 Sensor**: Measures temperature and humidity levels in real-time.  
- **ESP32 Microcontroller**: Acts as the brain of the system, collecting sensor data and sending it to the cloud.  
- **Ubidots IoT Platform**: Visualizes the collected data through interactive dashboards for monitoring and analysis.  

This solution can be used for applications like home security systems, smart agriculture, or environmental monitoring.

---

## Hardware Components  
Here’s the list of hardware components used in this project:  
- **ESP32 Development Board**  
- **PIR Motion Sensor**  
- **DHT11 Temperature & Humidity Sensor**  
- **Breadboard and Jumper Wires**  
- **Power Supply (USB Cable or Battery)**  

---

## Software Tools  
The following software tools were used during development:  
- **Thonny IDE**: For programming the ESP32 microcontroller.  
- **Git & GitHub**: For version control and collaboration.  
- **MongoDB & PyMongo**: For database management (optional, if storing data locally).  
- **Ubidots**: IoT platform for real-time data visualization.  
- **Python Libraries**:  
  - `machine` (for ESP32 GPIO control)  
  - `dht` (for DHT11 sensor readings)  
  - `urequests` (for HTTP requests to Ubidots API)  

---

## Setup Instructions  
Follow these steps to set up the project on your local environment:  

### 1. Install Required Tools  
- Download and install [Thonny IDE](https://thonny.org/).  
- Set up Git and GitHub for version control.  

### 2. Connect Hardware  
- Connect the **PIR Motion Sensor** and **DHT11 Sensor** to the ESP32 board using jumper wires.  
  - PIR Sensor: Connect VCC to 3.3V, GND to GND, and OUT to a GPIO pin (e.g., GPIO14).  
  - DHT11 Sensor: Connect VCC to 3.3V, GND to GND, and DATA to a GPIO pin (e.g., GPIO4).  

### 3. Configure Ubidots  
- Create an account on [Ubidots](https://ubidots.com/).  
- Add a new device and note down the **Device Token** and **Variable IDs** for temperature, humidity, and motion detection.  

### 4. Upload Code to ESP32  
- Clone this repository:  
  ```bash
  git clone https://github.com/your-repo-url.git](https://github.com/RakaPratama8/iot-project-uni268.git
  ```
- Open the project folder in Thonny IDE.  
- Update the Ubidots API token and variable IDs in the code.  
- Upload the code to your ESP32 board.  

### 5. Test the System  
- Power up the ESP32 and observe the sensor readings on the Ubidots dashboard.  
- Test the PIR Motion Sensor by moving in front of it and check for motion detection alerts.  

---

## How It Works  
1. The **DHT11 Sensor** collects temperature and humidity data at regular intervals.  
2. The **PIR Motion Sensor** detects movement and sends a signal when motion is detected.  
3. The ESP32 processes the data and sends it to the Ubidots cloud platform via HTTP requests.  
4. Users can view real-time sensor data and motion alerts on the Ubidots dashboard.  

---

## Screenshots/Demo  
### Ubidots Dashboard  
![Ubidots Dashboard](link-to-dashboard-screenshot)  
*Real-time visualization of temperature, humidity, and motion detection.*  

### Hardware Setup  
![Hardware Setup](link-to-hardware-photo)  
*ESP32 connected to PIR Motion Sensor and DHT11 Sensor.*  

---

## Team Members  
- **Farras Dzaky Faisa**
- **Muhamad Raka Pratama**
- **Philo Satriya**  
- **Eka Arya Gading**  

---

## Acknowledgments  
We would like to thank:  
- **Samsung Innovation Campus** for providing this incredible learning opportunity.  
- **Hacktiv8 Indonesia** for their guidance and support throughout the program.  
- Our mentors and instructors for their valuable feedback and encouragement.  

---

Feel free to contribute to this project or use it as inspiration for your own IoT solutions! 🚀  

**Let’s innovate together!**  
#SIC6Stage2 #SIC_Indonesia_2025 #enabling_people #samsunginnovationcampus
