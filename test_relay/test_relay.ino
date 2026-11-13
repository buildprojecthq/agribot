/**
 * ============================================================================
 * PURE RELAY TEST CODE (STANDALONE)
 * Target: Arduino Nano / Uno
 * Pin: Digital Pin 12 (D12)
 * Logic: Active-LOW (LOW = Relay ON, HIGH = Relay OFF)
 * ============================================================================
 * 
 * Hardware Connection:
 *   Relay VCC -> Breadboard 5V (+)
 *   Relay GND -> Breadboard GND (-)
 *   Relay IN  -> Arduino Nano D12 (Digital Pin 12)
 * ============================================================================
 */

const int RELAY_PIN = 12; // Dedicated Digital Pin D12

void setup() {
  Serial.begin(9600);
  delay(500);

  Serial.println(F("========================================"));
  Serial.println(F("    PURE RELAY TEST (PIN D12)           "));
  Serial.println(F("    Active-LOW Logic:                   "));
  Serial.println(F("    LOW  = ON (Pump Activated)          "));
  Serial.println(F("    HIGH = OFF (Pump Deactivated)       "));
  Serial.println(F("========================================"));

  // Preset pin HIGH before setting OUTPUT to prevent any startup glitch
  digitalWrite(RELAY_PIN, HIGH);
  pinMode(RELAY_PIN, OUTPUT);

  Serial.println(F("[BOOT] Relay initialized to OFF (HIGH)."));
  Serial.println(F("[BOOT] Starting in 2 seconds..."));
  delay(2000);
}

void loop() {
  // 1. Turn Relay ON (Active-LOW -> LOW)
  Serial.println(F(">>> [RELAY ON] Pin D12 set to LOW  (Coil energized, Pump running)"));
  digitalWrite(RELAY_PIN, LOW);
  delay(3000); // Stay ON for 3 seconds

  // 2. Turn Relay OFF (Active-LOW -> HIGH)
  Serial.println(F("--- [RELAY OFF] Pin D12 set to HIGH (Coil de-energized, Pump stopped)"));
  digitalWrite(RELAY_PIN, HIGH);
  delay(3000); // Stay OFF for 3 seconds
}

