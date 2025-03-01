#include <ESP8266WiFi.h>
#include <PubSubClient.h>

#define D5 14
#define D6 12

// WiFi credentials
const char* ssid = "<your-wifi-name>";
const char* password = "<your-wifi-password>";

// MQTT settings
const char* mqtt_broker = "<your-broker-address>";
const int mqtt_port = 1883;
const char* mqtt_username = "<your-mqtt-username>";
const char* mqtt_password = "<your-mqtt-password>";
const char* mqtt_topic = "desk";

// Pin definitions
const int PIN_UP = D5; 
const int PIN_DOWN = D6; 

// Times for desk movement
const int TIME_LOWERING_DESK = 5000;  
const int TIME_RAISING_DESK = 5000;

WiFiClient espClient;
PubSubClient client(espClient);

void setup_wifi() {
  WiFi.begin(ssid, password);
  Serial.print("\nConnecting to WiFi");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println();
  Serial.print("Connected to WiFi. IP: ");
  Serial.println(WiFi.localIP());
}

void lower_desk() {
  digitalWrite(PIN_UP, HIGH);     // Make sure UP is off
  delay(100);                     // Small safety delay
  digitalWrite(PIN_DOWN, LOW);    // Activate DOWN movement
  delay(TIME_LOWERING_DESK);
  digitalWrite(PIN_DOWN, HIGH);   // Stop movement
}

void raise_desk() {
  digitalWrite(PIN_DOWN, HIGH);   // Make sure DOWN is off
  delay(100);                     // Small safety delay
  digitalWrite(PIN_UP, LOW);      // Activate UP movement
  delay(TIME_RAISING_DESK);
  digitalWrite(PIN_UP, HIGH);     // Stop movement
}

void callback(char* topic, byte* payload, unsigned int length) {
  // Create a null-terminated string from the payload
  char message[50] = {0};
  if (length < 50) {
    memcpy(message, payload, length);
    message[length] = '\0';
  } else {
    Serial.println("Message too long!");
    return;
  }
  
  Serial.print("Received message: ");
  Serial.println(message);

  if (strcmp(message, "up") == 0) {
    Serial.println("Raising desk");
    raise_desk();
  } 
  else if (strcmp(message, "down") == 0) {
    Serial.println("Lowering desk");
    lower_desk();
  }
}

void reconnect() {
  while (!client.connected()) {
    Serial.print("Connecting to MQTT...");
    String clientId = "ESP8266Client-" + String(random(0xffff), HEX);
    
    if (client.connect(clientId.c_str(), mqtt_username, mqtt_password)) {
      Serial.println("connected");
      client.subscribe(mqtt_topic);
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" retrying in 5s");
      delay(5000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  Serial.println("\nStarting up...");
  
  // Initialize pins
  pinMode(PIN_UP, OUTPUT);
  pinMode(PIN_DOWN, OUTPUT);
  
  // Set both relays to HIGH (inactive) by default
  digitalWrite(PIN_UP, HIGH);
  digitalWrite(PIN_DOWN, HIGH);
  
  setup_wifi();
  client.setServer(mqtt_broker, mqtt_port);
  client.setCallback(callback);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
}
