const int emgPin = A0;  // EMG sensor connected to analog pin A0
const int threshold = 640;  // Adjust based on your sensor's output (0–1023)

void setup() {
  Serial.begin(9600);  // Start serial communication at 9600 baud
}
 
void loop() {
  int emgValue = analogRead(emgPin);  // Read EMG sensor value (0–1023)
  if (emgValue > threshold) {
    Serial.println("1");  // Send "1" when muscle flex is detected
    delay(200);  // Debounce to avoid multiple triggers (adjust as needed)
  }
  delay(10);  // Small delay for stability
}