#include <Wire.h>
#include <MPU6050.h>

// MPU6050 object
MPU6050 mpu;

// Flex sensor pins (example: 5 fingers)
const int flexPins[5] = {A0, A1, A2, A3, A4};
int flexValues[5];

void setup() {
  Serial.begin(9600);
  Wire.begin();

  // Initialize MPU6050
  mpu.initialize();
  if (!mpu.testConnection()) {
    Serial.println("MPU6050 connection failed!");
    while (1);
  }
  Serial.println("MPU6050 initialized.");
}

void loop() {
  // Read flex sensors
  for (int i = 0; i < 5; i++) {
    flexValues[i] = analogRead(flexPins[i]);
  }

  // Read MPU6050 accelerometer & gyroscope
  int16_t ax, ay, az, gx, gy, gz;
  mpu.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);

  // Send data over Serial in CSV format
  Serial.print("FLEX,");
  for (int i = 0; i < 5; i++) {
    Serial.print(flexValues[i]);
    if (i < 4) Serial.print(",");
  }

  Serial.print(",MPU,");
  Serial.print(ax); Serial.print(",");
  Serial.print(ay); Serial.print(",");
  Serial.print(az); Serial.print(",");
  Serial.print(gx); Serial.print(",");
  Serial.print(gy); Serial.print(",");
  Serial.println(gz);

  delay(50); // ~20 Hz sampling rate
}
