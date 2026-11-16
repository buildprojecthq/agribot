# Academic Mini-Project Report & Viva Voce Guide
## Smart Ploughing and Cultivation Agriculture Robot
**Department of Electronics and Communication Engineering (ECE)**

---

## 1. Project Synopsis

### Abstract
The **Smart Ploughing and Cultivation Agriculture Robot** is an integrated electromechanical mobile platform designed to automate primary and secondary field operations: tillage (ploughing), precision seed metering, and crop irrigation/pesticide spraying. Controlled wirelessly via a custom Native Android mobile application over a Bluetooth Serial Port Profile (SPP) link, the robot coordinates four functional subsystems through an ATmega328P microcontroller (Arduino Nano V3.0) with a deterministic, non-blocking asynchronous state machine architecture and a dual-isolated power distribution scheme (Method 2).

### Primary Objectives
1. Implement a 4-wheel differential (skid-steer) locomotion chassis capable of high-torque traversal over uneven soil surfaces using 12V DC high-torque geared motors and agricultural rubber wheels.
2. Develop a motorized tillage unit using a TowerPro SG90 micro servo mechanism for automated furrow creation.
3. Design an active agitator seed dispensing mechanism using a TowerPro SG90 micro servo to prevent grain bridging and achieve uniform volumetric sowing.
4. Integrate a low-latency wireless command interface with a 2000 ms failsafe communication watchdog to prevent runaway hazards.
5. Implement a clean, electrically isolated power bus (Method 2) separating high-power motor transients from sensitive microcontroller digital logic.

---

## 2. Hardware Architecture & Itemized Bill of Materials (BOM)

### 2.1 Master Hardware Components
| Component Description | Qty | Role in Robot |
| :--- | :---: | :--- |
| **Arduino Nano V3.0 (ATmega328P 16MHz) Microcontroller** | 1 | Master embedded controller running non-blocking firmware |
| **HC-05 Bluetooth 2.0 Serial Pass-Through Module** | 1 | Wireless telemetry link receiving SPP commands @ 9600 bps |
| **L298N Dual H-Bridge High-Power Motor Driver Module** | 1 | Dual H-bridge driver switching 12V power to wheel motors |
| **4WD Mobile Robot Chassis Frame** | 1 | Structural chassis supporting tools, tanks, and electronics |
| **12V DC High-Torque Geared Motors** | 4 | Drive motors for 4WD differential skid-steer locomotion |
| **Agricultural High-Traction Robot Rubber Wheels** | 4 | Deep-tread rubber tires providing grip on loose agricultural soil |
| **TowerPro SG90 Micro Servos (Tillage & Seed Dispenser)** | 2 | Precision actuators for soil tillage blade and seed hopper agitator |
| **1-Channel 5V Optocoupled Relay Isolation Module** | 1 | Opto-isolated Active-LOW switch driving the 12V water pump |
| **12V DC Submersible Mini Water Pump** | 1 | Submersible liquid pump spraying water/pesticide from reservoir |
| **3S 18650 11.1V–12.6V High-Drain Li-ion Battery Pack (Motor Bus)** | 1 | High-current power pack feeding L298N 12V and pump |
| **Single 18650 Cell + SM5401 5V Step-Up Boost Module (Logic Bus)** | 1 | Clean, isolated 5.0V power source for Nano, HC-05, and servos |

### 2.2 Microcontroller: ATmega328P (Arduino Nano V3.0)
* **Clock Frequency:** 16 MHz external crystal oscillator.
* **Operating Logic:** 5.0 V TTL.
* **Execution Paradigm:** Pure non-blocking architecture using `millis()` differential time checking (`currentMillis - previousMillis >= interval`). Blocking routines like `delay()` are strictly avoided in `loop()` to ensure zero packet loss during serial reception.
* **Breadboard Mounting:** Sits in a half-size solderless breadboard, insulating solder joints from the metal chassis.

### 2.3 Power Architecture: Dual-Isolated Buses (Method 2)
* **High-Current Drive Bus:** 3S Li-ion Battery pack (3x 3.7V 18650 cells in series, nominal $11.1\text{V}$, full charge $12.6\text{V}$) directly powering the L298N `+12V` terminal for the 4 geared motors and the water pump.
* **Clean Logic Bus:** Single blue 18650 cell stepped up to 5.0V regulated via an SM5401 synchronous boost module, powering the Nano, HC-05, servos, and relay coil.
* **Common Ground Bus:** Unifies 12V Battery (-), SM5401 (-), Arduino GND, and L298N GND to establish a common 0V voltage reference.
* **L298N Jumper:** Onboard 5V-EN jumper cap is **removed** to isolate 12V motor voltage from the 5V logic bus.

### 2.4 Motor Driver & Skid-Steer Locomotion: L298N Dual H-Bridge
* **Configuration:** 4WD Skid-Steer Differential Drive.
  * Left-side pair (Front-Left + Rear-Left) wired in parallel to Channel A (`OUT1`, `OUT2`).
  * Right-side pair (Front-Right + Rear-Right) wired in parallel to Channel B (`OUT3`, `OUT4`).
* **Speed Modulation:** Software duty-cycle PWM ($50\text{ Hz}$, 75% power) provides a smooth, controlled 25% speed reduction for stable field traversal without needing extra wiring.

### 2.5 Wireless Telemetry: HC-05 Bluetooth Module
* **Protocol:** Bluetooth V2.0 + EDR, 2.4 GHz ISM band, GFSK modulation.
* **Profile:** Serial Port Profile (SPP) transparent UART bridge at 9600 bps.
* **Level Shifter:** Two-resistor voltage divider ($1\text{ k}\Omega$ and $2\text{ k}\Omega$) steps down 5V Arduino TX to 3.3V HC-05 RX.

### 2.6 Actuators & Tool Implements
1. **Mechanical Plough (TowerPro SG90 Micro Servo):**
   * Angular Travel: $72^\circ$ (retracted for transit) $\leftrightarrow 120^\circ$ (deployed into soil).
   * Energy Management: Auto-detaches PWM output once target angle is attained to eliminate continuous stall current.
2. **Seed Dispenser (TowerPro SG90 Micro Servo):**
   * Active mechanical agitator oscillating between $73^\circ$ and $123^\circ$ every $20\text{ ms}$ to prevent seed clumping and achieve uniform gravity discharge.
3. **Irrigation Sprayer (Submersible DC Pump + 1-Channel Relay on Pin D12):**
   * Optocoupler-isolated relay module configured in Active-LOW mode to safely isolate the digital logic from the inductive flyback of the 12V pump motor.

---

## 3. Comprehensive Viva Voce Questions & Answers

### Q1: Why did you use two separate battery sources (Method 2) instead of a single 12V battery with a regulator?
**Answer:** DC motors and water pumps are heavy inductive loads. Under soil resistance, the 4 motors can momentarily pull several amperes, causing a severe voltage drop (sag) on the battery rail. If the Arduino shares that same power rail, the voltage dips below its 4.3V brownout threshold, causing the microcontroller to reboot in an infinite loop. By adopting our **dual-isolated architecture (Method 2)**, the 3S 12V pack powers only the motors and pump, while a separate blue 18650 cell boosted to 5.0V powers the Arduino and logic. This guarantees 100% stability.

### Q2: Why is the voltage divider mandatory between the Arduino TX and HC-05 RX pin?
**Answer:** The HC-05 transceiver chipset runs on $3.3\text{V}$ logic levels. The Arduino outputs $5.0\text{V}$ TTL. Connecting the Arduino TX directly into HC-05 RX stresses the baseband input diodes and will permanently degrade the receiver. A voltage divider consisting of $R_1 = 1\text{ k}\Omega$ and $R_2 = 2\text{ k}\Omega$ produces:
$$V_{\text{RX}} = 5\text{V} \times \frac{2\text{k}\Omega}{1\text{k}\Omega + 2\text{k}\Omega} = 3.33\text{V}$$
Conversely, the HC-05 TX to Arduino RX requires no divider because the ATmega328P recognizes any voltage $\ge 3.0\text{V}$ as a valid logic HIGH.

### Q3: How does the software prevent robot runaway in case the smartphone disconnects or moves out of range?
**Answer:** In wireless robotics, signal loss is a serious hazard. If the robot is driving forward ('F') and the user's phone disconnects, goes out of range, or the app crashes, the robot would continue driving blindly into obstacles. Our software watchdog records a timestamp `millis()` on every valid incoming command. If the robot is moving and no new command arrives for 2000 milliseconds (2 seconds), it automatically invokes `stopMotors()` to bring the chassis to a complete halt.

### Q4: Why are TowerPro SG90 micro servos used for both tillage and seed agitation?
**Answer:** The TowerPro SG90 is a lightweight, low-power, high-reliability micro servo with sufficient angular holding torque ($\approx 1.8\text{ kg}\cdot\text{cm}$) to actuate the furrowing blade linkage and oscillate the seed metering gate. Using identical SG90 servos across both subsystems simplifies spare-part interchangeability, reduces weight on the chassis, and keeps peak current draw low enough to be safely powered from the regulated 5V bus without brownout risks.
