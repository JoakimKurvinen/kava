
#include <Servo.h>

int servoPin = 9;

Servo Servo1;

const int buzzerPin = 5;

const int songLength = 18;

char notes[] = "cdfda ag cdfdg gf ";

int beats[] = {1,1,1,1,1,1,4,4,2,1,1,1,1,1,1,4,4,2};

int tempo = 113;

// Our pin attachments
const int analog = A0;
const int digital = 3;

void setup() {  
  Serial.begin(9600);
  pinMode(digital, OUTPUT);
  digitalWrite(digital, LOW);
  Servo1.attach(servoPin);
  pinMode(buzzerPin, OUTPUT);
}

void loop() {
  if(Serial.available()){
    if(Serial.read() == 's')
    {
      Servo1.write(90);
      digitalWrite(digital, HIGH);
      delay(2000);
    }
  }
  
    else
    {
      Servo1.write(0);
      digitalWrite(digital, LOW);
    }

  int sensorVal = analogRead(analog);

  float voltage = (sensorVal / 1024.0) * 5.0; 

  // The sensor changes 10 mV per degree (500 mV offset)
  int temperature = (voltage - .5) * 100;
 
  Serial.println(temperature);
    int i, duration;
  delay(2000);
}


