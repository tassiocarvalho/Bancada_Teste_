#include "HX711.h"

// --- Configurações HX711 ---
#define DT D0
#define SCK D6

HX711 escala;

// --- Configurações ESC ---
const int ESC_PIN = D1;            
const int ESC_MIN = 1000;          
const int ESC_MAX = 2000;          
const int ESC_NEUTRAL = 1500;      

int currentSpeed = ESC_NEUTRAL;    
int speedStep = 2.5;                
unsigned long lastPulse = 0;
unsigned long lastWeightReading = 0;

// --- Funções ESC ---
void sendPulse(int microseconds) {
  digitalWrite(ESC_PIN, HIGH);
  delayMicroseconds(microseconds);
  digitalWrite(ESC_PIN, LOW);
}

void processCommand(char cmd) {
  switch (cmd) {
    case '+':
    case 'w':
    case 'W':
      if (currentSpeed < ESC_MAX) {
        currentSpeed += speedStep;
        if (currentSpeed > ESC_MAX) currentSpeed = ESC_MAX;
        Serial.print("↑ Velocidade: ");
        Serial.print(getPercent());
        Serial.println("%");
      }
      break;

    case '-':
    case 's':
    case 'S':
      if (currentSpeed > ESC_MIN) {
        currentSpeed -= speedStep;
        if (currentSpeed < ESC_MIN) currentSpeed = ESC_MIN;
        Serial.print("↓ Velocidade: ");
        Serial.print(getPercent());
        Serial.println("%");
      }
      break;

    case '0':
      currentSpeed = ESC_NEUTRAL;
      Serial.println("⏹ Motor parado");
      break;

    case 'f':
    case 'F':
      currentSpeed = ESC_MAX;
      Serial.println("⏩ Máximo frente");
      break;

    case 'r':
    case 'R':
      currentSpeed = ESC_MIN;
      Serial.println("⏪ Máximo reverso");
      break;

    case 'i':
    case 'I':
      printStatus();
      break;

    case 't':
    case 'T':
      Serial.println("Tarando...");
      escala.tare(10);
      Serial.println("OK!");
      break;
  }
}

int getPercent() {
  if (currentSpeed == ESC_NEUTRAL) return 0;
  if (currentSpeed > ESC_NEUTRAL) {
    return map(currentSpeed, ESC_NEUTRAL, ESC_MAX, 0, 100);
  } else {
    return map(currentSpeed, ESC_MIN, ESC_NEUTRAL, -100, 0);
  }
}

void printStatus() {
  Serial.println("=== STATUS ===");
  Serial.print("Velocidade: ");
  Serial.print(getPercent());
  Serial.println("%");
  Serial.print("Pulso: ");
  Serial.println(currentSpeed);
  Serial.println("==============");
}

// --- Setup HX711 ---
void setupHX711() {
  escala.begin(DT, SCK);
  Serial.println("Retire peso da balança!");
  delay(2000);
  escala.set_scale(-101);      
  escala.tare(20);
  Serial.println("Balança OK!");
}

// --- Setup ESC ---
void setupESC() {
  pinMode(ESC_PIN, OUTPUT);
  digitalWrite(ESC_PIN, LOW);
  
  Serial.println("Inicializando ESC...");
  
  // Inicialização mais curta
  for(int i = 0; i < 30; i++) {
    sendPulse(ESC_MIN);
    delay(20);
  }
  
  for(int i = 0; i < 15; i++) {
    sendPulse(ESC_NEUTRAL);
    delay(20);
  }
  
  Serial.println("ESC OK!");
  Serial.println("Comandos: +/- (vel), 0 (parar), f/r (max), i (info), t (tarar)");
}

// --- Loop HX711 ---
void loopHX711() {
  unsigned long currentTime = millis();
  
  // Lê peso mais devagar quando motor ligado para evitar interferência
  unsigned long interval = (currentSpeed == ESC_NEUTRAL) ? 300 : 1000;
  
  if (currentTime - lastWeightReading >= interval) {
    lastWeightReading = currentTime;
    
    // Desabilita temporariamente PWM durante leitura crítica
    bool motorWasRunning = (currentSpeed != ESC_NEUTRAL);
    if (motorWasRunning) {
      digitalWrite(ESC_PIN, LOW);
      delayMicroseconds(100); // Pausa brevíssima
    }
    
    if (escala.is_ready()) {
      // Menos leituras quando motor ligado
      int readings = motorWasRunning ? 3 : 10;
      float peso_kg = escala.get_units(readings) / 1000.0;
      
      Serial.print("Peso: ");
      Serial.print(peso_kg, 3);
      Serial.println(" kg");
    }
    
    // Reativa PWM imediatamente
    if (motorWasRunning) {
      lastPulse = millis(); // Reset timer PWM
    }
  }
}

// --- Loop ESC ---
void loopESC() {
  unsigned long currentTime = millis();
  
  // PWM 50Hz para ESC
  if (currentTime - lastPulse >= 20) {
    lastPulse = currentTime;
    sendPulse(currentSpeed);
  }

  if (Serial.available()) {
    String cmd = Serial.readString();
    cmd.trim();
    if (cmd.length() > 0) {
      processCommand(cmd[0]);
    }
  }
}

// --- Setup principal ---
void setup() {
  Serial.begin(115200);
  delay(1000);
  
  Serial.println("=== ESP8266 + HX711 + ESC ===");
  setupHX711();
  setupESC();
  printStatus();
}

// --- Loop principal ---
void loop() {
  loopHX711();    
  loopESC();      
  yield(); // Para não travar WiFi
}