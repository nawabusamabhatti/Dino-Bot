#include <Servo.h>
#include <String.h>

Servo myservo;
String S;

void setup() {
  Serial.begin(9600);
  myservo.attach(9);
  myservo.write(90);  
   
}

void loop() {
int x = 0;
    if(Serial.read() == "1")
    { 
      digitalWrite(13, HIGH);
      myservo.write(45);
      delay(25        0);
      digitalWrite(13, LOW);
      myservo.write(90); 
      delay(250);
      } 
      
}                                      
