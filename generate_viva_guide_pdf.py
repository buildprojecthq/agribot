#!/usr/bin/env python3
"""
Generates the comprehensive Smart Agri-Robot Components Guide & Viva Reference PDF.
Uses Google Chrome headless mode for crisp typography, page breaks, and styling.
"""

import os
import subprocess

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Smart Agri-Robot - Components Guide & Viva Reference Manual</title>
<style>
    @page {
        size: A4;
        margin: 18mm 16mm 18mm 16mm;
        @bottom-right {
            content: counter(page);
        }
    }
    body {
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        color: #1e293b;
        background: #ffffff;
        line-height: 1.55;
        font-size: 10pt;
    }
    h1, h2, h3, h4 {
        color: #0f172a;
        font-weight: 700;
        margin-top: 0;
    }
    .cover {
        text-align: center;
        padding: 30px 10px 20px 10px;
        border-bottom: 2px solid #059669;
        margin-bottom: 25px;
    }
    .cover h1 {
        font-size: 24pt;
        color: #065f46;
        margin-bottom: 6px;
        letter-spacing: -0.5px;
    }
    .cover .subtitle {
        font-size: 12pt;
        color: #475569;
        margin-bottom: 15px;
    }
    .cover .meta {
        display: inline-block;
        background: #f0fdf4;
        border: 1px solid #bbf7d0;
        padding: 6px 16px;
        border-radius: 20px;
        font-size: 9.5pt;
        color: #166534;
        font-weight: 600;
    }
    .section-title {
        font-size: 15pt;
        color: #065f46;
        border-bottom: 2px solid #e2e8f0;
        padding-bottom: 5px;
        margin-top: 25px;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
    }
    .component-card {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-left: 4px solid #10b981;
        border-radius: 6px;
        padding: 12px 14px;
        margin-bottom: 14px;
        page-break-inside: avoid;
    }
    .component-card.accent-blue {
        border-left-color: #3b82f6;
    }
    .component-card.accent-amber {
        border-left-color: #f59e0b;
    }
    .component-card.accent-purple {
        border-left-color: #8b5cf6;
    }
    .comp-header {
        display: flex;
        justify-content: space-between;
        align-items: baseline;
        margin-bottom: 6px;
    }
    .comp-name {
        font-size: 12pt;
        font-weight: 700;
        color: #0f172a;
    }
    .comp-tag {
        font-size: 8pt;
        background: #e2e8f0;
        color: #334155;
        padding: 2px 8px;
        border-radius: 12px;
        font-weight: 600;
        text-transform: uppercase;
    }
    .comp-row {
        margin-bottom: 4px;
    }
    .comp-label {
        font-weight: 700;
        color: #334155;
        font-size: 9pt;
        display: inline-block;
        width: 140px;
    }
    .features-list {
        margin: 6px 0 0 0;
        padding-left: 18px;
        font-size: 9pt;
        color: #475569;
    }
    .features-list li {
        margin-bottom: 2px;
    }
    .qna-card {
        background: #ffffff;
        border: 1px solid #cbd5e1;
        border-radius: 6px;
        padding: 12px 14px;
        margin-bottom: 12px;
        page-break-inside: avoid;
    }
    .qna-question {
        font-size: 10.5pt;
        font-weight: 700;
        color: #1e3a8a;
        margin-bottom: 6px;
    }
    .qna-answer {
        font-size: 9.5pt;
        color: #334155;
        line-height: 1.5;
    }
    .highlight {
        background: #fef08a;
        padding: 1px 4px;
        border-radius: 3px;
        font-weight: 600;
    }
    .page-break {
        page-break-before: always;
    }
    .footer-note {
        text-align: center;
        margin-top: 30px;
        font-size: 8.5pt;
        color: #64748b;
        border-top: 1px solid #e2e8f0;
        padding-top: 10px;
    }
</style>
</head>
<body>

<div class="cover">
    <h1>Smart Ploughing & Cultivation Agriculture Robot</h1>
    <div class="subtitle">Complete Hardware Components Guide & Teacher Viva Reference Manual</div>
    <div class="meta">Project Portfolio & Examination Ready Reference • Built by buildproject.in</div>
</div>

<h2 class="section-title">Part 1: Detailed Component Knowledge Base</h2>
<p style="font-size: 9pt; color: #64748b; margin-top:-5px; margin-bottom: 15px;">
    An exhaustive breakdown of every module, actuator, power source, and software tool used in the robot, phrased in crisp professional English with layman explanations.
</p>

<!-- 1. Arduino Nano -->
<div class="component-card">
    <div class="comp-header">
        <span class="comp-name">1. Arduino Nano R3 Microcontroller Board</span>
        <span class="comp-tag">Central Brain / MCU</span>
    </div>
    <div class="comp-row"><span class="comp-label">General Description:</span> A compact, breadboard-friendly microcontroller board based on the 8-bit ATmega328P chip running at 16 MHz.</div>
    <div class="comp-row"><span class="comp-label">Use in this Project:</span> Acts as the master brain of the robot, receiving Bluetooth commands from the smartphone, executing locomotion logic, driving tool servos, and switching the water pump relay.</div>
    <div class="comp-row"><span class="comp-label">Layman Features:</span>
        <ul class="features-list">
            <li>Small miniature computer that reads inputs and controls motors/switches in milliseconds.</li>
            <li>Plugs directly into a plastic breadboard, which completely prevents short circuits against the metal robot frame.</li>
            <li>Contains 14 digital input/output pins, 8 analog inputs, and a Mini-USB port for instant code uploading.</li>
        </ul>
    </div>
</div>

<!-- 2. HC-05 Bluetooth Module -->
<div class="component-card accent-blue">
    <div class="comp-header">
        <span class="comp-name">2. HC-05 Wireless Bluetooth SPP Module</span>
        <span class="comp-tag">Wireless Telemetry</span>
    </div>
    <div class="comp-row"><span class="comp-label">General Description:</span> A standard Bluetooth 2.0 + EDR wireless module that converts wireless radio data into Serial (UART) data using the Serial Port Profile (SPP).</div>
    <div class="comp-row"><span class="comp-label">Use in this Project:</span> Receives real-time single-byte control commands ('F', 'B', 'L', 'R', 'P', 'D', 'W') sent from the companion Android app and forwards them to Arduino Nano pins D2/D3.</div>
    <div class="comp-row"><span class="comp-label">Layman Features:</span>
        <ul class="features-list">
            <li>Invisible wireless bridge that connects your smartphone to the robot up to 10 meters away.</li>
            <li>Requires no Internet or Wi-Fi router; connects directly phone-to-robot like Bluetooth headphones.</li>
            <li>Operates at a fast 9600 baud rate with an onboard LED indicating connection status.</li>
        </ul>
    </div>
</div>

<!-- 3. L298N Motor Driver Module -->
<div class="component-card accent-amber">
    <div class="comp-header">
        <span class="comp-name">3. L298N Dual H-Bridge Motor Driver Module</span>
        <span class="comp-tag">High-Current Motor Controller</span>
    </div>
    <div class="comp-row"><span class="comp-label">General Description:</span> A high-voltage, high-current dual full-bridge motor driver capable of controlling the speed and rotational direction of DC motors.</div>
    <div class="comp-row"><span class="comp-label">Use in this Project:</span> Takes low-power logic signals from the Arduino (pins D4-D7) and switches 12V high-current battery power to drive the 4 chassis wheels in differential drive.</div>
    <div class="comp-row"><span class="comp-label">Layman Features:</span>
        <ul class="features-list">
            <li>Acts as an electrical muscle: microcontrollers only give weak signals (20mA), but wheels need high current (up to 2 Amps).</li>
            <li>Allows motors to spin forwards, spin backwards, or stop on command using internal transistor switches.</li>
            <li>Equipped with a finned black aluminum heatsink to dissipate heat during heavy field operation.</li>
        </ul>
    </div>
</div>

<!-- 4. 4WD DC Geared Motors -->
<div class="component-card">
    <div class="comp-header">
        <span class="comp-name">4. DC Geared Motors (BO Motors) & High-Traction Wheels</span>
        <span class="comp-tag">Locomotion Actuators</span>
    </div>
    <div class="comp-row"><span class="comp-label">General Description:</span> Low-cost direct-current electric motors paired with internal internal reduction gearboxes and rubber tread tires.</div>
    <div class="comp-row"><span class="comp-label">Use in this Project:</span> Mounted under the chassis in two parallel pairs (left pair and right pair) to push the robot through agricultural soil using skid-steer navigation.</div>
    <div class="comp-row"><span class="comp-label">Layman Features:</span>
        <ul class="features-list">
            <li>The internal plastic/metal gearbox converts high motor speed into strong turning force (torque) needed to pull through soil.</li>
            <li>Thick rubber tires with deep ridges provide grip on dusty, uneven farmland without slipping.</li>
            <li>4-wheel drive ensures the robot continues moving even if one wheel hits a pit or obstacle.</li>
        </ul>
    </div>
</div>

<div class="page-break"></div>

<!-- 5. TowerPro SG90 / MG90S Micro Servo (Seed) -->
<div class="component-card accent-purple">
    <div class="comp-header">
        <span class="comp-name">5. TowerPro SG90 / MG90S Micro Servo (Seed Dispenser)</span>
        <span class="comp-tag">Precision Angular Actuator</span>
    </div>
    <div class="comp-row"><span class="comp-label">General Description:</span> A miniature rotary actuator that allows for precise angular positioning between 0 and 180 degrees using Pulse Width Modulation (PWM).</div>
    <div class="comp-row"><span class="comp-label">Use in this Project:</span> Mounted directly next to the seed hopper; smoothly agitates back and forth (73° to 123°) to prevent seed clogging and dispense seeds at a uniform rate.</div>
    <div class="comp-row"><span class="comp-label">Layman Features:</span>
        <ul class="features-list">
            <li>Unlike normal spinning motors, a servo moves to an exact angle and holds its position tightly.</li>
            <li>Contains its own internal motor, gears, feedback potentiometer, and control circuit in a tiny 9g plastic case.</li>
            <li>Automatically shakes the seed gate like a salt shaker so seeds never jam in the funnel hole.</li>
        </ul>
    </div>
</div>

<!-- 6. TowerPro SG90 / MG996R Servo (Plough) -->
<div class="component-card accent-purple">
    <div class="comp-header">
        <span class="comp-name">6. Tool Servo (Plough Lifter Blade)</span>
        <span class="comp-tag">Mechanical Tool Lifter</span>
    </div>
    <div class="comp-row"><span class="comp-label">General Description:</span> An angular position servo designed to lift and lower mechanical linkages against mechanical resistance.</div>
    <div class="comp-row"><span class="comp-label">Use in this Project:</span> Connected to the front tillage bracket (Pin D10) to lower the plough blade to 120° for soil furrowing and raise it to 72° for transit.</div>
    <div class="comp-row"><span class="comp-label">Layman Features:</span>
        <ul class="features-list">
            <li>Acts as the mechanical arm of a tractor that drops the plough into the dirt when working and lifts it up when driving on the road.</li>
            <li>Software automatically turns off (detaches) the motor power once it reaches the angle, saving battery and preventing overheating.</li>
        </ul>
    </div>
</div>

<!-- 7. 1-Channel 5V Relay Module -->
<div class="component-card accent-blue">
    <div class="comp-header">
        <span class="comp-name">7. 1-Channel 5V Optocoupled Relay Module (Active-LOW)</span>
        <span class="comp-tag">Electrically Isolated Switch</span>
    </div>
    <div class="comp-row"><span class="comp-label">General Description:</span> An electrically operated mechanical switch triggered by a 5V logic signal, featuring an optical isolator (optocoupler) for circuit safety.</div>
    <div class="comp-row"><span class="comp-label">Use in this Project:</span> Connected to Arduino Pin D12; safely turns the 12V high-power water pump ON and OFF without allowing motor noise to reach the Arduino.</div>
    <div class="comp-row"><span class="comp-label">Layman Features:</span>
        <ul class="features-list">
            <li>A light-beam (optocoupler) separates the fragile Arduino brain from the noisy 12V water pump so electricity can never surge backwards.</li>
            <li>Makes a satisfying "click" sound when an internal magnetic coil closes the physical contact points.</li>
            <li>Active-LOW design: activates when the Arduino pin outputs 0V (Ground) and deactivates on 5V.</li>
        </ul>
    </div>
</div>

<!-- 8. DC Submersible Mini Water Pump -->
<div class="component-card">
    <div class="comp-header">
        <span class="comp-name">8. Submersible DC Mini Water Pump & Sprayer Tubing</span>
        <span class="comp-tag">Irrigation & Pesticide Spraying</span>
    </div>
    <div class="comp-row"><span class="comp-label">General Description:</span> A compact centrifugal pump with a sealed, waterproof motor housing intended for submerging in liquids.</div>
    <div class="comp-row"><span class="comp-label">Use in this Project:</span> Submerged in the clear liquid reservoir; pumps water or liquid pesticide through flexible silicone tubing to spray cultivated soil rows.</div>
    <div class="comp-row"><span class="comp-label">Layman Features:</span>
        <ul class="features-list">
            <li>Mini electric fountain pump that pulls water from the bottom of the container and pushes it out through spray nozzles.</li>
            <li>Completely safe inside water because all electrical windings are hermetically sealed in waterproof resin.</li>
            <li>Delivers high flow rate with low power draw from the 12V battery pack.</li>
        </ul>
    </div>
</div>

<!-- 9. 3S 18650 Li-ion Battery Pack -->
<div class="component-card accent-amber">
    <div class="comp-header">
        <span class="comp-name">9. 3S 18650 Li-ion Battery Pack (11.1V – 12.6V)</span>
        <span class="comp-tag">High-Current Drive Power</span>
    </div>
    <div class="comp-row"><span class="comp-label">General Description:</span> A battery pack consisting of three rechargeable 3.7V cylindrical Lithium-ion cells wired in series.</div>
    <div class="comp-row"><span class="comp-label">Use in this Project:</span> Supplies dedicated high-current 11.1V–12.6V direct power to the L298N motor driver terminal to power all 4 wheel motors and the water pump.</div>
    <div class="comp-row"><span class="comp-label">Layman Features:</span>
        <ul class="features-list">
            <li>High-energy rechargeable batteries identical to the ones used inside laptops and electric vehicles.</li>
            <li>Provides the high current burst needed when all 4 wheels push against thick soil or steep inclines.</li>
            <li>Kept completely separated from the Arduino to guarantee that motor voltage dips never reset the computer.</li>
        </ul>
    </div>
</div>

<!-- 10. Single 18650 Blue Battery & SM5401 Module -->
<div class="component-card accent-amber">
    <div class="comp-header">
        <span class="comp-name">10. Single 18650 Battery + SM5401 5V Boost Converter</span>
        <span class="comp-tag">Clean Logic Power Supply (Method 2)</span>
    </div>
    <div class="comp-row"><span class="comp-label">General Description:</span> A dedicated 3.7V Li-ion battery paired with an SM5401 synchronous boost regulator that outputs a stable 5.0V.</div>
    <div class="comp-row"><span class="comp-label">Use in this Project:</span> Powers the clean 5V logic bus: feeds the Arduino Nano 5V pin, HC-05 Bluetooth module, servo logic, and relay coil.</div>
    <div class="comp-row"><span class="comp-label">Layman Features:</span>
        <ul class="features-list">
            <li>Works like a mini mobile power bank dedicated solely to keeping the Arduino brain alive and happy.</li>
            <li>Prevents "Brownout": even when the wheel motors draw heavy power, this clean battery remains steady at 5.0V.</li>
            <li>Includes built-in Micro-USB charging circuitry for convenient recharging.</li>
        </ul>
    </div>
</div>

<div class="page-break"></div>

<!-- 11. Solderless Breadboard & Voltage Divider -->
<div class="component-card">
    <div class="comp-header">
        <span class="comp-name">11. Half-Size Solderless Breadboard & 1kΩ / 2kΩ Divider</span>
        <span class="comp-tag">Prototyping & Level Shifter</span>
    </div>
    <div class="comp-row"><span class="comp-label">General Description:</span> A reusable plug-and-play prototyping board with spring clip sockets, paired with precision metal film resistors.</div>
    <div class="comp-row"><span class="comp-label">Use in this Project:</span> Mounts the Arduino Nano securely to isolate solder points from the metal chassis, distributes power rails, and steps down 5V TX to 3.3V for the HC-05 RX pin.</div>
    <div class="comp-row"><span class="comp-label">Layman Features:</span>
        <ul class="features-list">
            <li>Eliminates messy soldering while allowing easy wire adjustments and circuit testing.</li>
            <li>The 1kΩ and 2kΩ resistors act as a voltage step-down valve so the Arduino does not burn out the sensitive 3.3V Bluetooth chip.</li>
            <li>Connects all module ground wires together into a single unified reference highway (Common Ground).</li>
        </ul>
    </div>
</div>

<!-- 12. Smart Agri Robot Android Companion App -->
<div class="component-card accent-blue">
    <div class="comp-header">
        <span class="comp-name">12. Smart Agri Robot Android Companion Application</span>
        <span class="comp-tag">Human-Machine Interface (HMI)</span>
    </div>
    <div class="comp-row"><span class="comp-label">General Description:</span> A native Android application written in Kotlin utilizing Android Bluetooth SPP RFCOMM sockets.</div>
    <div class="comp-row"><span class="comp-label">Use in this Project:</span> Runs on the farmer's smartphone; automatically connects to HC-05 on launch, provides D-pad touch steering, and toggles tools with haptic feedback.</div>
    <div class="comp-row"><span class="comp-label">Layman Features:</span>
        <ul class="features-list">
            <li>Custom modern dark-mode mobile remote control created specifically for this agricultural machine.</li>
            <li>Zero hassle: turning on the app automatically detects and connects to the robot without manual pairing menus.</li>
            <li>Touch-and-hold driving: car moves when you press the arrow and instantly stops when you lift your finger.</li>
            <li>Features a direct link in the footer to visit <span class="highlight">https://buildproject.in/</span> with a single tap.</li>
        </ul>
    </div>
</div>

<h2 class="section-title">Part 2: Teacher & Viva Voce Examination Questions & Answers</h2>
<p style="font-size: 9pt; color: #64748b; margin-top:-5px; margin-bottom: 15px;">
    Frequently asked examination questions with technically rigorous, impressive answers designed to score top marks in project evaluation and viva defense.
</p>

<!-- Q1 -->
<div class="qna-card">
    <div class="qna-question">Q1: Why did you use two separate battery sources instead of running everything from one 12V battery?</div>
    <div class="qna-answer">
        <strong>Examiner Insight:</strong> Tests your understanding of electrical noise, voltage sag, and microcontroller reliability.<br>
        <strong>Model Answer:</strong> "DC motors and water pumps are heavy inductive loads. When all 4 motors start simultaneously under soil resistance, they draw sudden current surges of several amps, which causes a momentary voltage drop (sag) on the battery rail. If the Arduino shares that same power rail, the voltage dips below 4.3V, causing an internal <em>Brownout Reset (BOR)</em> that reboots the microcontroller. By adopting our <strong>dual-isolated architecture (Method 2)</strong>, the 3S 12V pack exclusively powers motors and the pump, while a separate blue 18650 cell boosted to 5V powers the Arduino and logic. This completely eliminates back-EMF spikes and resets."
    </div>
</div>

<!-- Q2 -->
<div class="qna-card">
    <div class="qna-question">Q2: Why is a Common Ground necessary between the 12V battery, the 5V power supply, and the Arduino?</div>
    <div class="qna-answer">
        <strong>Examiner Insight:</strong> Tests fundamental circuit theory regarding signal reference voltages.<br>
        <strong>Model Answer:</strong> "Voltage is defined as the electrical potential difference between two points. When the Arduino Nano outputs a HIGH signal (5V) to the L298N driver's IN1 pin, the driver must compare that incoming signal against a reference point (0V). Without a common ground linking the Arduino GND and the L298N GND, the two circuits have floating references. The driver cannot determine whether the signal is HIGH or LOW, resulting in erratic motor behavior, electrical buzzing, or complete communication failure."
    </div>
</div>

<!-- Q3 -->
<div class="qna-card">
    <div class="qna-question">Q3: Why did you choose an Arduino Nano on a breadboard over the traditional Arduino Uno?</div>
    <div class="qna-answer">
        <strong>Examiner Insight:</strong> Tests real-world prototyping experience and hardware troubleshooting.<br>
        <strong>Model Answer:</strong> "The Arduino Uno has through-hole solder pins protruding from the bottom of its PCB. When mounted directly on a metal robot chassis, chassis mounting screws and metal plates cause dead short-circuits across 5V and GND traces, which can destroy the ATmega328P. The Arduino Nano has a compact form factor that plugs directly into a solderless breadboard. The plastic breadboard body acts as a 100% non-conductive electrical insulator, completely preventing chassis shorts while providing organized 5V and GND distribution buses."
    </div>
</div>

<!-- Q4 -->
<div class="qna-card">
    <div class="qna-question">Q4: How does the L298N H-Bridge control the direction of the DC motors?</div>
    <div class="qna-answer">
        <strong>Examiner Insight:</strong> Tests motor driver electronics and transistor switching topology.<br>
        <strong>Model Answer:</strong> "An H-bridge consists of four switching transistors (typically BJTs or MOSFETs) arranged in the shape of the letter 'H' with the motor across the center. By turning on diagonally opposite transistors (Q1 and Q4), current flows through the motor from left to right, spinning it forward. Turning on the other diagonal pair (Q2 and Q3) reverses the current flow from right to left, reversing rotation. If all switches are turned OFF (LOW), the motor coasts to a stop."
    </div>
</div>

<div class="page-break"></div>

<!-- Q5 -->
<div class="qna-card">
    <div class="qna-question">Q5: How did you reduce the motor speed by 25% without changing any hardware wiring on the L298N?</div>
    <div class="qna-answer">
        <strong>Examiner Insight:</strong> Tests embedded software capabilities versus hardware PWM pin constraints.<br>
        <strong>Model Answer:</strong> "On the L298N, speed is typically controlled by applying PWM to the ENA/ENB enable pins. However, our ENA/ENB jumpers were bridged to 5V, and the Arduino Nano's hardware PWM Timer 1 was dedicated to the Servo library. To solve this without adding extra wires, we implemented a <strong>50 Hz software duty-cycle algorithm</strong> inside the non-blocking <code>loop()</code>. In every 20 millisecond window, the motors are energized for 15 ms (75% power) and coasted for 5 ms (25% off). Because DC gearboxes possess mechanical inertia, the wheels experience a smooth, seamless 25% reduction in speed without noticeable vibration."
    </div>
</div>

<!-- Q6 -->
<div class="qna-card">
    <div class="qna-question">Q6: Why does the seed dispenser servo oscillate continuously instead of simply opening a gate?</div>
    <div class="qna-answer">
        <strong>Examiner Insight:</strong> Tests practical agricultural mechanics and seed flow dynamics.<br>
        <strong>Model Answer:</strong> "Agricultural seeds (like wheat, mustard, or pulses) stored in a funnel hopper have high surface friction and moisture. If a hopper gate is simply held open statically, seeds form a mechanical arch or bridge, leading to immediate clogging; or conversely, an uncontrolled avalanche of seeds pours out in one spot. By programming the SG90 micro servo to oscillate smoothly between 73° and 123° using a state machine, the agitator continuously breaks seed bridges, metering out seeds uniformly at spaced intervals along the furrow."
    </div>
</div>

<!-- Q7 -->
<div class="qna-card">
    <div class="qna-question">Q7: Why do you call <code>servo.detach()</code> after moving the plough servo to its position?</div>
    <div class="qna-answer">
        <strong>Examiner Insight:</strong> Tests power optimization and servo thermal management.<br>
        <strong>Model Answer:</strong> "Standard analog servos use a closed-loop internal control circuit. If a servo is held at an angle under external mechanical load (such as the plough resting on the ground), the internal H-bridge continuously pumps current into the motor to fight the resistance. This creates a continuous stall current of 500mA to 1.2A, draining the battery and overheating the servo windings. By calling <code>servo.detach()</code> 800ms after commanding the move, the PWM control signal is stopped. The mechanical gearbox holds the tool in place while current drops to zero."
    </div>
</div>

<!-- Q8 -->
<div class="qna-card">
    <div class="qna-question">Q8: Why is a voltage divider needed between Arduino pin D3 and HC-05 RXD?</div>
    <div class="qna-answer">
        <strong>Examiner Insight:</strong> Tests logic level translation and semiconductor protection.<br>
        <strong>Model Answer:</strong> "The ATmega328P operates at 5.0V TTL logic levels, meaning its digital HIGH output is 5.0V. However, the core Bluetooth processor on the HC-05 operates strictly at 3.3V CMOS logic. Injecting 5.0V directly into the HC-05 RXD pin will exceed the silicon breakdown voltage and permanently damage the receiver. A voltage divider consisting of R1 = 1 kΩ and R2 = 2 kΩ steps the voltage down: <code>Vout = 5V * (2k / (1k + 2k)) = 3.33V</code>, providing a safe, clean logic level."
    </div>
</div>

<!-- Q9 -->
<div class="qna-card">
    <div class="qna-question">Q9: What does 'Active-LOW' mean in your relay module, and why is it preferred?</div>
    <div class="qna-answer">
        <strong>Examiner Insight:</strong> Tests relay optocoupler input topology and micro-controller boot safety.<br>
        <strong>Model Answer:</strong> "In an Active-LOW relay module, the onboard optocoupler LED anode is connected to VCC (5V). To energize the relay coil, the input pin must be pulled to Ground (0V / LOW) to allow current to flow through the optocoupler diode. Applying 5V (HIGH) creates zero voltage difference, keeping the relay OFF. Active-LOW is preferred in embedded robotics because microcontrollers can sink more current to Ground through their internal low-side MOSFETs than they can source from high-side rails. Furthermore, in our firmware, we preset pin D12 to HIGH before defining it as OUTPUT to prevent any relay click upon microcontroller reboot."
    </div>
</div>

<!-- Q10 -->
<div class="qna-card">
    <div class="qna-question">Q10: What is the purpose of the 2000 ms software watchdog timer in the Arduino code?</div>
    <div class="qna-answer">
        <strong>Examiner Insight:</strong> Tests fail-safe robotics design and wireless communication safety.<br>
        <strong>Model Answer:</strong> "In mobile robotics, wireless link failure is an inherent risk. If the robot is driving forward ('F') and the user's phone goes out of Bluetooth range, runs out of battery, or the app crashes, the robot will continue driving blindly into walls, ditches, or water reservoirs. The software watchdog records a timestamp <code>millis()</code> on every valid incoming command. If the robot is moving and no new packet arrives for over 2000 milliseconds (2 seconds), <code>stopMotors()</code> is automatically triggered to halt the chassis."
    </div>
</div>

<!-- Q11 -->
<div class="qna-card">
    <div class="qna-question">Q11: Why did you use single-byte ASCII characters ('F', 'B', 'P', 'W') instead of full text strings?</div>
    <div class="qna-answer">
        <strong>Examiner Insight:</strong> Tests communication bandwidth efficiency and serial buffer latency.<br>
        <strong>Model Answer:</strong> "Sending multi-character strings like 'FORWARD\\n' requires serial parsing, delimiter checks, string buffer allocation, and multiple UART transmission cycles. At 9600 baud, sending 1 byte takes roughly 1 millisecond, whereas strings introduce parsing overhead and memory fragmentation on an ATmega328P with only 2KB of SRAM. Single-byte ASCII commands allow our parser to execute in a single <code>switch-case</code> statement in less than 5 microseconds with zero latency."
    </div>
</div>

<!-- Q12 -->
<div class="qna-card">
    <div class="qna-question">Q12: How would you scale this prototype for real-world agricultural fields?</div>
    <div class="qna-answer">
        <strong>Examiner Insight:</strong> Tests future scope, commercial viability, and engineering vision.<br>
        <strong>Model Answer:</strong> "To scale this prototype for full agricultural deployment:
        1. <strong>Locomotion:</strong> Replace BO motors with planetary-geared 24V brushless DC motors or continuous rubber tank tracks for muddy terrain.
        2. <strong>Autonomy:</strong> Integrate RTK-GPS (Real-Time Kinematic) and wheel encoders for centimeter-accuracy waypoint row following without manual remote control.
        3. <strong>Vision & AI:</strong> Mount an onboard camera running an edge-AI model (e.g., YOLO on Raspberry Pi or ESP32-CAM) to detect crop rows and selectively spray pesticide only on weeds rather than the whole field.
        4. <strong>Power:</strong> Add a 50W monocrystalline solar canopy on the robot roof for continuous field recharging."
    </div>
</div>

<div class="footer-note">
    Smart Ploughing & Cultivation Agriculture Robot • Technical Documentation & Viva Reference Manual<br>
    Visit official project repository & releases: <strong>https://buildproject.in/</strong> | GitHub: <strong>buildprojecthq/agribot</strong>
</div>

</body>
</html>
"""

html_path = "/tmp/smart_agri_robot_viva_guide.html"
pdf_path = "/home/yashas/Projects/miniproject_agriculture_bot/Smart_Agri_Robot_Viva_and_Components_Guide.pdf"

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated HTML at: {html_path}")

cmd = [
    "google-chrome",
    "--headless",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_path}",
    html_path
]

print(f"Executing: {' '.join(cmd)}")
res = subprocess.run(cmd, capture_output=True, text=True)
if res.returncode == 0:
    print(f"SUCCESS: Created PDF at {pdf_path}")
    print(f"File size: {os.path.getsize(pdf_path)} bytes")
else:
    print(f"ERROR: {res.stderr}")
