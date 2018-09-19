
#include <Servo.h>

int servoPin = 9;
int n;

Servo Servo1;

const int analog = A0;
const int digital = 3;

void setup() {  
  Serial.begin(9600);
  pinMode(digital, OUTPUT);
  digitalWrite(digital, LOW);
  Servo1.attach(servoPin);
  n = 0;
}

void loop() {
  if(Serial.available()){
    n = Serial.read() - '0';
  }
  int sensorVal = analogRead(analog);

  float voltage = (sensorVal / 1024.0) * 5.0; 

  // The sensor changes 10 mV per degree (500 mV offset)
  int temperature = (voltage - .5) * 100;
 
  Serial.println(temperature);

  if (temperature > 25) {
    digitalWrite(digital, HIGH);
  }

  else {
    digitalWrite(digital, LOW);
  }
  
  // Make servo go to n degrees 
  Servo1.write(n);
  delay(1000);
  // Make servo go to 0 degrees 
  Servo1.write(0);
  
  delay(2000);
  


}
