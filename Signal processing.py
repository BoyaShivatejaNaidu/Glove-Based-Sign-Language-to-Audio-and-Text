import serial
import csv
import pyttsx3
import time

# --- CONFIGURATION ---
SERIAL_PORT = "COM3"   # Change this to your Arduino port (e.g., "/dev/ttyUSB0" for Linux/Mac)
BAUD_RATE = 9600
CSV_FILE = "data_log.csv"

# --- Initialize Speech Engine ---
engine = pyttsx3.init()

# --- Open Serial Connection ---
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
time.sleep(2)  # Wait for Arduino reset

print("Connected to Arduino on", SERIAL_PORT)

# --- Open CSV File for Logging ---
with open(CSV_FILE, mode="w", newline="") as file:
    writer = csv.writer(file)
    # Header row
    writer.writerow(["thumb", "index", "middle", "ring", "little", "ax", "ay", "az", "gx", "gy", "gz"])

    try:
        while True:
            line = ser.readline().decode("utf-8").strip()
            if not line:
                continue

            # Example line: FLEX,512,540,600,480,510,MPU,-1234,456,16384,200,-100,50
            if line.startswith("FLEX"):
                parts = line.replace("FLEX,", "").replace("MPU,", "").split(",")
                if len(parts) == 11:
                    # Save values to CSV
                    writer.writerow(parts)
                    file.flush()  # write immediately
                    print("Data:", parts)

                    # Convert strings to integers
                    values = list(map(int, parts))
                    thumb, index, middle, ring, little, ax, ay, az, gx, gy, gz = values

                    # --- Simple Gesture Mapping (Example Rules) ---
                    if index > 600 and middle > 600 and ring > 600 and little > 600:
                        gesture = "Fist"
                    elif thumb < 400 and index < 400 and middle < 400:
                        gesture = "Open Hand"
                    else:
                        gesture = None

                    if gesture:
                        print("Recognized Gesture:", gesture)
                        engine.say(gesture)
                        engine.runAndWait()

    except KeyboardInterrupt:
        print("\nStopped by user.")
    finally:
        ser.close()
