#include <Arduino.h>

const int analogInputPin = A0;
const int outputPin = 9;

void setup()
{
  pinMode(outputPin, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  int analogValue = analogRead(analogInputPin);
  float processedValue = 2.5 - analogValue;
  processedValue = -processedValue;
  processedValue += 2.5;

  analogWrite(outputPin, processedValue);

  Serial.print("Analog Input: ");
  Serial.print(analogValue);
  Serial.print(", Processed Value: ");
  Serial.println(processedValue);

  delay(1000);
}