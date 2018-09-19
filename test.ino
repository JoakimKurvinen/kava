const int analog = A0;
const int digital = 3;

void setup() {  
  Serial.begin(9600);
  pinMode(digital, OUTPUT);
  digitalWrite(digital, LOW);
}

void loop() {
  int sensorVal = analogRead(analog);
  Serial.print("sensor Value: ");
  Serial.print(sensorVal);

  float voltage = (sensorVal / 1024.0) * 5.0;
  Serial.print(", Volts: ");
  Serial.print(voltage);

  // The sensor changes 10 mV per degree (500 mV offset)
  float temperature = (voltage - .5) * 100;
  Serial.print(", degrees C: ");
  Serial.println(temperature);

  if (temperature > 25) {
    digitalWrite(digital, HIGH);
  }

  else {
    digitalWrite(digital, LOW);
  }
  
  delay(1);
}
