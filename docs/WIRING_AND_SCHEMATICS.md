# Hardware Wiring & Schematic Guide
## Smart Ploughing and Cultivation Agriculture Robot

This document provides the complete, pin-by-pin interconnection matrix, voltage divider schematic, and dual-isolated power distribution architecture (Method 2).

---

## 1. Itemized Hardware Bill of Materials (BOM)

| Component Description | Qty | Role in Robot |
| :--- | :---: | :--- |
| **Arduino Nano V3.0 (ATmega328P 16MHz) Microcontroller** | 1 | Master embedded controller running non-blocking firmware |
| **HC-05 Bluetooth 2.0 Serial Pass-Through Module** | 1 | Wireless telemetry link receiving SPP commands @ 9600 bps |
| **L298N Dual H-Bridge High-Power Motor Driver Module** | 1 | Dual H-bridge driver switching 12V power to wheel motors |
| **4WD Mobile Robot Chassis Frame** | 1 | Structural chassis supporting tools, tanks, and electronics |
| **12V DC High-Torque Geared Motors** | 4 | Drive motors for 4WD differential skid-steer locomotion |
| **Agricultural High-Traction Robot Rubber Wheels** | 4 | Deep-tread rubber tires providing grip on loose agricultural soil |
| **TowerPro SG90 Micro Servos (Tillage & Seed Dispenser)** | 2 | Precision actuators for soil tillage blade and seed hopper agitator |
| **1-Channel 5V Optocoupled Relay Isolation Module** | 1 | Opto-isolated Active-LOW switch driving the 5V water pump |
| **5V DC Submersible Mini Water Pump** | 1 | Submersible liquid pump spraying water/pesticide from reservoir |
| **3S 18650 11.1V–12.6V High-Drain Li-ion Battery Pack (Motor Bus)** | 1 | High-current power pack feeding L298N 12V terminal |
| **Single 18650 Cell + SM5401 5V Step-Up Boost Module (Logic Bus)** | 1 | Clean, isolated 5.0V power source for Nano, HC-05, and servos |

---

## 2. Master Pin Allocation Matrix

| Arduino Nano Pin | Component / Subsystem | Pin on Module | Signal Direction | Electrical / Logic Level |
| :---: | :--- | :--- | :--- | :--- |
| **`D2`** | HC-05 Bluetooth Module | **`TXD`** | Input to Arduino | 3.3V TTL (Meets Nano 5V TTL high threshold $\ge 3.0\text{V}$) |
| **`D3`** | HC-05 Bluetooth Module | **`RXD`** | Output from Arduino | **5V stepped down to 3.3V** via 1kΩ/2kΩ divider |
| **`D4`** | L298N Motor Driver | **`IN1`** | Output | Left Motors Forward control |
| **`D5`** | L298N Motor Driver | **`IN2`** | Output | Left Motors Reverse control |
| **`D6`** | L298N Motor Driver | **`IN3`** | Output | Right Motors Forward control |
| **`D7`** | L298N Motor Driver | **`IN4`** | Output | Right Motors Reverse control |
| **`D9`** | Seed Metering Servo (TowerPro SG90) | **Signal (Orange/Yellow)**| Output | 50 Hz PWM; VCC from SM5401 5V rail ($73^\circ \leftrightarrow 123^\circ$) |
| **`D10`** | Plough Lifter Servo (TowerPro SG90) | **Signal (Orange/Yellow)**| Output | 50 Hz PWM; VCC from SM5401 5V rail ($72^\circ \leftrightarrow 120^\circ$) |
| **`D12`** | 1-Channel Relay Module | **`IN`** | Output | Active-LOW trigger (LOW = Pump ON, HIGH = Pump OFF) |
| **`D13`** | Status Indicator LED | Onboard LED | Output | Pulses for 70 ms on valid Bluetooth command |
| **`GND`** | Common Ground Bus | `GND` | Power | Unified Ground for all system modules |
| **`5V`** | Breadboard Red Rail | `5V` | Power Input | Regulated 5.0V DC from SM5401 boost module |

---

## 3. Dual-Isolated Power Architecture (Method 2)

```
        [ 3S 18650 Li-ion Battery Pack (11.1V - 12.6V) ]      [ Single 18650 Cell (3.7V - 4.2V) ]
                                |                                              |
                                v                                              v
                 +-------------------------------+             +-------------------------------+
                 |  L298N Motor Driver Terminal  |             |  SM5401 5V Step-Up Boost PCB  |
                 |  +12V Power      GND Terminal |             |  5V (+) Output  GND (-) Output|
                 +-------------------------------+             +-------------------------------+
                     |                   |                                 |            |
                     | (12V Motor Bus)   |                                 v            |
                     v                   |                        +------------------+  |
           4x 12V Geared Motors          |                        | Breadboard Red   |  |
                                        |                        | 5.0V Power Bus   |  |
                                         |                        +------------------+  |
                                         |                           |   |   |   |      |
                                         |    Arduino Nano 5V Pin <--+   |   |   |      |
                                         |    Relay Module VCC <---------+   |   |      |
                                         |    TowerPro SG90 Servos VCC ------+   |      |
                                         |    HC-05 Bluetooth VCC ---------------+      |
                                         |                                              |
                                         +==============================================+
                                                                 |
                                                       [ COMMON GROUND BUS ]
                                                  (Breadboard Blue (-) Ground Rail)
```

> [!IMPORTANT]
> **L298N 5V-EN Jumper Cap:** Must be **REMOVED**. The L298N logic is powered via its `+5V` terminal directly from the breadboard 5V rail, keeping the high-noise 12V motor supply isolated while sharing common ground.

---

## 4. HC-05 UART Voltage Divider

The HC-05 Bluetooth module has a $3.3\text{V}$ RX pin. Sending a $5\text{V}$ logic signal from Arduino pin `D3` directly into the HC-05 RX pin can degrade or damage the Bluetooth receiver over time.

Use two resistors to form a voltage divider:
* $R_1 = 1\text{ k}\Omega$ (between Arduino `D3` and HC-05 `RXD`)
* $R_2 = 2\text{ k}\Omega$ (between HC-05 `RXD` and `GND`)

$$V_{\text{out}} = V_{\text{in}} \times \frac{R_2}{R_1 + R_2} = 5.0\text{ V} \times \frac{2000}{1000 + 2000} \approx 3.33\text{ V}$$

```
   Arduino Pin D3 (TX) ----[ 1 kΩ ]----+----> HC-05 RXD Pin
                                       |
                                    [ 2 kΩ ]
                                       |
                                      GND
```

---

## 5. L298N Motor Driver Wiring & Direction Truth Table

* **Left Motors:** 2x 12V Geared Motors wired in parallel to OUT1 & OUT2.
* **Right Motors:** 2x 12V Geared Motors wired in parallel to OUT3 & OUT4.
* **Speed Modulation:** Software duty-cycle PWM ($50\text{ Hz}$, 75% duty cycle) slows wheels by ~25% for smooth, controlled motion.

### Calibrated Direction Truth Table:
| Operation | Command | IN1 (D4) | IN2 (D5) | IN3 (D6) | IN4 (D7) | Left Channel | Right Channel | Speed |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Forward** | `'F'` | LOW | HIGH | HIGH | LOW | FWD | FWD | 75% Duty Cycle |
| **Backward** | `'B'` | HIGH | LOW | LOW | HIGH | REV | REV | 75% Duty Cycle |
| **Skid Left** | `'L'` | HIGH | LOW | HIGH | LOW | REV | FWD | 75% Duty Cycle |
| **Skid Right** | `'R'` | LOW | HIGH | LOW | HIGH | FWD | REV | 75% Duty Cycle |
| **Hard Stop** | `'S'` | LOW | LOW | LOW | LOW | STOP | STOP | 0% |

---

## 6. Water Pump & 1-Channel Relay Interfacing

* **Relay Type:** Optocoupler-isolated 5V 1-Channel Relay (Active-LOW).
* **Connections:**
  * Relay `VCC` -> Breadboard Red `+5V`
  * Relay `GND` -> Breadboard Blue `GND`
  * Relay `IN` -> Arduino Nano Pin `D12`
* **Load Circuit:**
  * Breadboard Red `5V` Rail `(+)` -> Relay `COM` (Common terminal)
  * Relay `NO` (Normally Open) -> 5V Submersible Pump `(+)` Red Wire
  * 5V Submersible Pump `(-)` Black Wire -> Common `GND`
* **Software Safety:** The firmware initializes pin `D12` to `HIGH` before declaring it `OUTPUT` to prevent momentary relay clicks during boot.

---

## 7. Servos Interfacing (Plough & Seed Dispenser)

| Servo Function | Model | Control Pin | Power (VCC) | Ground | Calibrated Motion |
| :--- | :--- | :---: | :--- | :--- | :--- |
| **Plough Lifter** | TowerPro SG90 | Pin `D10` | Breadboard `+5V` rail | Common `GND` | Retracted: $72^\circ$ \| Deployed: $120^\circ$ |
| **Seed Dispenser** | TowerPro SG90 | Pin `D9` | Breadboard `+5V` rail | Common `GND` | Closed: $73^\circ$ \| Agitation: $73^\circ \leftrightarrow 123^\circ$ |
