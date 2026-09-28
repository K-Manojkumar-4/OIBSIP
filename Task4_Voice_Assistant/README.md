# Voice Assistant

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![SpeechRecognition](https://img.shields.io/badge/SpeechRecognition-Library-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Project-Completed-success?style=for-the-badge)
![Internship](https://img.shields.io/badge/Oasis%20Infobyte-Internship-orange?style=for-the-badge)

> A simple yet functional **Voice Assistant** built in Python that listens to spoken commands and responds with useful actions, developed as part of the Oasis Infobyte Python Programming Internship.

---

## 📌 Project Overview

This project is a beginner-friendly voice assistant that uses speech recognition and text-to-speech technologies.  

The assistant can greet the user, tell the current time and date, perform web searches, and respond to basic voice commands. It also includes graceful error handling when speech is not understood.

**Key Highlights:**
- Real-time voice input using microphone
- Text-to-speech responses
- Current time and date functionality
- Web search capability
- Clean and modular code structure

---

## 🗂️ Project Structure

Task4_Voice_Assistant/
│
├── voice_assistant.py     # Main application file
└── README.md              # Project documentation

---

## 🛠️ Technologies Used

| Technology            | Purpose                                      |
|-----------------------|----------------------------------------------|
| Python 3              | Core programming language                    |
| `SpeechRecognition`   | Converts speech to text                      |
| `pyttsx3`             | Text-to-speech engine                        |
| `datetime`            | For fetching current time and date           |
| `webbrowser`          | For opening web search results               |

---

## ✨ Features

- Captures voice input using the microphone
- Responds to the greeting “Hello”
- Tells the current time when requested
- Tells the current date when requested
- Performs a web search on a user-specified topic
- Graceful error handling when speech is not understood
- Text-to-speech feedback for all responses
- Option to exit the assistant using voice commands

---

## 🚀 How to Run the Project

1. Ensure **Python 3** is installed on your system.
2. Install the required libraries:

```bash
pip install SpeechRecognition
pip install pyttsx3
pip install pyaudio