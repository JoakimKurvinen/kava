
// Our pin attachments
const int analog = A0;

// Setup
void setup() {  
  Serial.begin(9600);  
}

// The loop for reading temperature values
void loop() {
      int sensorVal = analogRead(analog);
      float voltage = (sensorVal / 1024.0) * 5.0; 
      int temperature = (voltage - .5) * 100; // The sensor changes 10 mV per degree (500 mV offset)
      Serial.println(temperature);  
      //delay(3600000); // 1 hour delay to display next value
  	delay(300000); // 5 minutes
}
