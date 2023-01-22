/*********
  Rui Santos
  Complete project details at https://RandomNerdTutorials.com/esp32-web-server-sent-events-sse/
  
  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files.
  
  The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.
*********/

#include <WiFi.h>
#include <AsyncTCP.h>
#include <ESPAsyncWebServer.h>
#include "time.h"
#include "Adafruit_seesaw.h"
#include <Wire.h>
#include "Adafruit_VEML6070.h"
//#include <Adafruit_BME280.h>
//#include <Adafruit_Sensor.h>
Adafruit_seesaw ss;
Adafruit_VEML6070 ultrav = Adafruit_VEML6070();
int delaytime = 1020; //edit this number in ms for delay time between readss
time_t seconds;

// Replace with your network credentials
const char* ssid = "IEEE";
const char* password = "Ilovesolder";

// Create AsyncWebServer object on port 80
AsyncWebServer server(80);

// Create an Event Source on /events
AsyncEventSource events("/events");

// Timer variables
unsigned long lastTime = 0;  
unsigned long timerDelay = 1020;

// Create a sensor object
//Adafruit_BME280 bme;         // BME280 connect to ESP32 I2C (GPIO 21 = SDA, GPIO 22 = SCL)

float timeStamp;
float uv;
float soilMoisture;

// Init BME280
// void initBME(){
//     if (!bme.begin(0x76)) {
//     Serial.println("Could not find a valid BME280 sensor, check wiring!");
//     while (1);
//   }
// }

void getSensorReadings(){
  timeStamp = millis()/1000;
  // Convert timeStamp to Fahrenheit
  //timeStamp = 1.8 * bme.readtimeStamp() + 32;
  uv = ultrav.readUV();
  soilMoisture = ss.touchRead(0);
}

// Initialize WiFi
void initWiFi() {
    WiFi.mode(WIFI_STA);
    WiFi.begin(ssid, password);
    Serial.print("Connecting to WiFi ..");
    while (WiFi.status() != WL_CONNECTED) {
        Serial.print('.');
        delay(1000);
    }
    Serial.println(WiFi.localIP());
}

String processor(const String& var){
  getSensorReadings();
  //Serial.println(var);
  if(var == "timeStamp"){
    return String(timeStamp);
  }
  else if(var == "uv"){
    return String(uv);
  }
  else if(var == "soilMoisture"){
    return String(soilMoisture);
  }
  return String();
}

const char index_html[] PROGMEM = R"rawliteral(
<!DOCTYPE HTML><html>
<head>
  <title>ESP Web Server</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
  <link rel="icon" href="data:,">
  <style>
    html {font-family: Arial; display: inline-block; text-align: center;}
    p { font-size: 1.2rem;}
    body {  margin: 0;}
    .topnav { overflow: hidden; background-color: #50B8B4; color: white; font-size: 1rem; }
    .content { padding: 20px; }
    .card { background-color: white; box-shadow: 2px 2px 12px 1px rgba(140,140,140,.5); }
    .cards { max-width: 800px; margin: 0 auto; display: grid; grid-gap: 2rem; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); }
    .reading { font-size: 1.4rem; }
  </style>
</head>
<body>
  <div class="topnav">
    <h1>Plants Vs Trojans</h1>
  </div>
  <div class="content">
    <div class="cards">
      <div class="card">
        <p><i class="fas fa-clock" style="color:#059e8a;"></i> timeStamp</p><p><span class="reading"><span id="ts">%timeStamp%</span>
      </div>
      <div class="card">
        <p><i class="fas fa-sun" style="color:#00add6;"></i> uv</p><p><span class="reading"><span id="ulv">%uv%</span> 
      </div>
      <div class="card">
        <p><i class="fas fa-poop" style="color:#e1e437;"></i> soilMoisture</p><p><span class="reading"><span id="sm">%soilMoisture%</span>
      </div>
    </div>
  </div>
<script>
if (!!window.EventSource) {
 var source = new EventSource('/events'); 
 source.addEventListener('timeStamp', function(e) {

  document.getElementById("ts").innerHTML = e.data;
 }, false);
 


 source.addEventListener('uv', function(e) {
  console.log("uv", e.data);
  document.getElementById("ulv").innerHTML = e.data;
 }, false);
 
 source.addEventListener('soilMoisture', function(e) {
  console.log("soilMoisture", e.data);
  document.getElementById("sm").innerHTML = e.data;
 }, false);
}
</script>
</body>
</html>)rawliteral";

void setup() {
  Serial.begin(115200);
  initWiFi();
  //initBME();
  //initialize uv
  Serial.println("VEML6070 Test");
  ultrav.begin(VEML6070_1_T);  // pass in the integration time constant

  Serial.println("seesaw Soil Sensor example!");
  
  if (!ss.begin(0x36)) {
    Serial.println("ERROR! seesaw not found");
    while(1) delay(1);
  } else {
    Serial.print("seesaw started! version: ");
    Serial.println(ss.getVersion(), HEX);
  }


  // Handle Web Server
  server.on("/", HTTP_GET, [](AsyncWebServerRequest *request){
    request->send_P(200, "text/html", index_html, processor);
  });

  // Handle Web Server Events
  events.onConnect([](AsyncEventSourceClient *client){
    if(client->lastId()){
      Serial.printf("Client reconnected! Last message ID that it got is: %u\n", client->lastId());
    }
    // send event with message "hello!", id current millis
    // and set reconnect delay to 1 second
    client->send("hello!", NULL, millis(), 10000);
  });
  server.addHandler(&events);
  server.begin();
}

void loop() {
  if ((millis() - lastTime) > timerDelay) {
    getSensorReadings();
    // Serial.printf("timeStamp = %.2f ºC \n", timeStamp);
    // Serial.printf("uv = %.2f \n", uv);
    // Serial.printf("soilMoisture = %.2f hPa \n", soilMoisture);
    // Serial.println();

    // Send Events to the Web Client with the Sensor Readings
    

    events.send(String(timeStamp).c_str(),"timeStamp",millis());
    events.send(String(uv).c_str(),"uv",millis());
    events.send(String(soilMoisture).c_str(),"soilMoisture",millis());
    
    lastTime = millis();
  }
}