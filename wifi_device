#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

const char* ssid = "your-ssid";
const char* password = "your-password";

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
}

void loop() {
  // Read sensor data and perform actions

  sendWiFiData();
}

void sendWiFiData() {
  HTTPClient http;
  http.begin("http://your-api-endpoint");
  http.addHeader("Content-Type", "application/json");

  // Create JSON payload with sensor data
  String payload = "{\"temperature\":25, \"humidity\":50}";

  int httpResponseCode = http.POST(payload);

  if (httpResponseCode > 0) {
    Serial.print("HTTP Response code: ");
    Serial.println(httpResponseCode);
  }

  http.end();
}
