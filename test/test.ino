
#include <Servo.h>

int servoPin = 9;

Servo Servo1;

const int buzzerPin = 5; //WIP

const int songLength = 18; //WIP

char notes[] = "cdfda ag cdfdg gf "; //WIP

int beats[] = {1,1,1,1,1,1,4,4,2,1,1,1,1,1,1,4,4,2}; // WIP

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
    if(Serial.read() == 's') //checks for input from the python script
    {
      Servo1.write(90); //turns servo to 90 degrees
      digitalWrite(digital, HIGH); //turns the led on
      delay(2000);
    }
  }
  
    else
    {
      Servo1.write(0); //keeps the servo at 0 without python input
      digitalWrite(digital, LOW); //keeps the led off
    }

  int sensorVal = analogRead(analog);

  float voltage = (sensorVal / 1024.0) * 5.0; 

  // The sensor changes 10 mV per degree (500 mV offset)
  int temperature = (voltage - .5) * 100;
 
  Serial.println(temperature);
    int i, duration;
  delay(2000); //2 second delay to display next value
}


