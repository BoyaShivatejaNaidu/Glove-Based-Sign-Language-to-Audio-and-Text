# Glove-Based-Sign-Language-to-Audio-and-Text
A wearable system that converts American Sign Language (ASL) gestures into real-time speech and text using smart gloves equipped with flex sensors, accelerometer, and Arduino Uno.

🔹 Features
Real-Time Translation: Converts ASL gestures to both text on screen and audio output.
Wearable & Lightweight: Integrated into gloves for natural hand movement.
Sensor Fusion: Flex sensors track finger bends, while an accelerometer captures hand motion.

Pipeline:
Arduino (C firmware): Captures & transmits calibrated sensor data.
Python: Processes signals, applies gesture recognition, and outputs speech via TTS.

🔧 Tech Stack
Hardware: Arduino Uno, Flex Sensors, MPU6050 Accelerometer, Gloves
Firmware: C/C++ (Arduino IDE)
Processing & Output: Python, PySerial, NumPy, Speech Synthesis (pyttsx3 / gTTS)

🚀 Future Improvements
Expand dataset for more ASL phrases & words
Integrate machine learning classifier for adaptive recognition
Add Bluetooth/WiFi connectivity for mobile integration
