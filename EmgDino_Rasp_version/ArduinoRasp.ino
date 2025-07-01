const int emgPin = A0;
const int threshold = 640;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int emgValue = analogRead(emgPin);
  if (emgValue > threshold) {
    Serial.println("1");
    delay(200);  // debounce
  }
  delay(10);
}
