#include "Adafruit_seesaw.h"
#include <Wire.h>
#include "Adafruit_VEML6070.h"

Adafruit_seesaw ss;
Adafruit_VEML6070 uv = Adafruit_VEML6070();
int delaytime = 2000; //edit this number in ms for delay time between readss

void setup() {
  Serial.begin(115200);
  Serial.println("VEML6070 Test");
  uv.begin(VEML6070_1_T);  // pass in the integration time constant

  Serial.println("seesaw Soil Sensor example!");
  
  if (!ss.begin(0x36)) {
    Serial.println("ERROR! seesaw not found");
    while(1) delay(1);
  } else {
    Serial.print("seesaw started! version: ");
    Serial.println(ss.getVersion(), HEX);
  }
}

void loop() {
  float tempC = ss.getTemp();
  uint16_t capread = ss.touchRead(0);

  Serial.print("Temperature: "); Serial.print(tempC); Serial.println("*C");
  Serial.print("Capacitive: "); Serial.println(capread);
  Serial.print("UV light level: "); Serial.println(uv.readUV());
  Serial.println("------------");
  delay(delaytime);
}
