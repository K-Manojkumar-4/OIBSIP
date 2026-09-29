# Basic Weather App

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![API](https://img.shields.io/badge/OpenWeatherMap-API-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Project-Completed-success?style=for-the-badge)
![Internship](https://img.shields.io/badge/Oasis%20Infobyte-Internship-orange?style=for-the-badge)

> A real-time **Weather Application** built in Python that fetches live weather data using the OpenWeatherMap API, developed as part of the Oasis Infobyte Python Programming Internship.

---

## 📌 Project Overview

This project is a command-line based weather application that allows users to get current weather information for any city around the world.  

The application makes an API call to OpenWeatherMap, processes the JSON response, and displays important weather details such as temperature, humidity, weather condition, and wind speed in a clean and readable format.

**Key Highlights:**
- Real-time weather data using OpenWeatherMap API
- Displays temperature in both Celsius and Fahrenheit
- Clean and structured output
- Proper error handling for invalid cities and network issues
- User-friendly command-line interface

---

## 🗂️ Project Structure

Task3_Weather_App/
│
├── weather_app.py     # Main application file
└── README.md          # Project documentation

---

## 🛠️ Technologies Used

| Technology          | Purpose                                      |
|---------------------|----------------------------------------------|
| Python 3            | Core programming language                    |
| `requests`          | For making HTTP requests to the weather API  |
| OpenWeatherMap API  | Source of live weather data                  |
| JSON                | For parsing API responses                    |

---

## ✨ Features

- Accepts city name as input from the user
- Fetches real-time weather data using OpenWeatherMap API
- Displays the following information:
  - City name and country
  - Temperature in °C and °F
  - Weather condition description
  - Humidity percentage
  - Wind speed
- Handles common errors gracefully (city not found, network issues, invalid API key)
- Rejects empty city input
- Option to check weather for multiple cities in one session

---

## 🚀 How to Run the Project

1. Ensure **Python 3** is installed on your system.
2. Install the required library:
   ```bash
   pip install requests
   ```
## Screenshots Outputs

![BMI Output](screenshots/)
