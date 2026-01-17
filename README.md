# Falcon-EW – Jammer Types Training Simulator

Falcon-EW is a lightweight educational simulation project that models  
how different electronic jamming strategies affect a radar system.

The project does **not** focus on signal-level physics or real EW hardware.  
Instead, it demonstrates **conceptual electronic warfare awareness** using  
simple, rule-based logic suitable for undergraduate-level study.

---

## Project Goals

- Introduce basic electronic warfare (EW) concepts  
- Compare different jammer strategies and their effects  
- Model system degradation instead of immediate failure  
- Practice modular Python design and simulation logic  

---

## Jammer Types Modeled

The simulator includes three simplified jammer categories:

- **Noise Jammer**  
  Wide-band interference that gradually reduces overall signal quality.

- **Spot Jammer**  
  Narrow-band interference that achieves stronger degradation with less power.

- **Deceptive Jammer**  
  Does not primarily destroy the signal, but introduces suspicious behavior
  that affects system interpretation rather than raw quality.

---

## System Logic

- The radar maintains a signal quality value (0–100).
- Each jammer reduces signal quality based on its type and parameters.
- Interference is classified using predefined thresholds.
- The system continues operating in a **degraded but controlled state**
  rather than immediately aborting the mission.

This approach reflects realistic EW training principles, where systems must
adapt to interference instead of assuming total failure.

---

## Example Output
--- Falcon-EW Jammer Training Simulation ---
Initial Radar Signal Quality: 100%

⚠️ Jammer Activated: Noise Jammer
Radar Signal Quality: 73.0%
Classification: Normal Operation
System Status: Degraded but Operational

⚠️ Jammer Activated: Spot Jammer
Radar Signal Quality: 65.0%
Classification: Possible Noise Jamming
System Status: Degraded but Operational

⚠️ Jammer Activated: Deceptive Jammer
Radar Signal Quality: 59.0%
Classification: Suspicious Signal Behavior
System Status: Degraded but Operational

---

## Project Structure
Falcon-Ew/
├── jammer.py # Jammer models and interference logic
├── radar.py # Radar signal evaluation and classification
├── simulator.py # EW interaction simulation
├── main.py # Scenario execution
└── README.md


---

## Educational Scope

This project is designed for **learning and experimentation only**.

- No real RF modeling
- No machine learning
- No flight or hardware control

The focus is on **decision logic, system behavior, and resilience concepts**
commonly discussed in electronic warfare and autonomous systems courses.

---

## Disclaimer

⚠️ This project is a **simulation prototype** and **not** a real EW system  
or flight controller.

It should not be used for operational or real-world applications.

