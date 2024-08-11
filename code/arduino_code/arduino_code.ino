#include <Servo.h>

Servo servo;
String str;

void setup() {
  // put your setup code here, to run once:
  servo.attach(9);
  pinMode(12,OUTPUT);
  Serial.begin(9600);
  servo.write(120);
  digitalWrite(12,LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()){
    str=Serial.readStringUntil('\n');
    if(str=="down"){
      servo.write(0);
      digitalWrite(12,HIGH);
    }else if(str=="up"){
      servo.write(120);
      digitalWrite(12,LOW);
    }
  }
}
