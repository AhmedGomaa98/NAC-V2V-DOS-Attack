# Hierarchical Cyber-Physical IDS for Smart City V2X Networks

Welcome to the official repository for our two-stage hierarchical intrusion detection system (IDS) designed for Vehicle-to-Everything (V2X) networks. This project implements a context-aware defense mechanism validated under realistic urban traffic and signal conditions, modeled specifically after the high-rise topography surrounding the Iconic Tower in Egypt's New Administrative Capital (NAC).

Instead of treating network security in a vacuum, this framework links cyber-network telemetry with real-time vehicle kinematics to catch stealthy exploits that standard, network-only models miss.

---

## Design & System Architecture

The core of our approach is to break down the heavy computational load of edge computing into an event-triggered, two-stage pipeline:

1. **Cyber-Physical Feature Coupling:** We fuse raw network packet frequencies with vehicle dynamics (speed, mass, and location telemetry). This step prevents the system from overfitting on clean digital patterns and forces it to validate data against physical reality.
2. **Stage 1 (Perimeter Guard):** A highly regularized, low-depth Extra Trees classifier (`max_depth=4`). It acts as a fast firewall at the vehicle’s On-Board Unit (OBU), filtering out nominal traffic with speed and achieving a zero false-alarm profile.
3. **Realistic Data Footprint:** We rejected artificially balanced datasets. The pipeline is tested against a true-to-life $3.07\%$ anomaly ratio, surrounded by over a million rows of background urban traffic.
4. **Stage 2 (Forensic Core):** Triggered only when Stage 1 flags a threat. Running at `max_depth=6`, this engine steps in to isolate complex multi-class attacks even when the V2X channel suffers from an intense $1.8\%$ dynamic noise and signal shadowing layer.

---

## Quick Results & Performance

Our benchmarks prove that you can achieve high diagnostic depth without causing processing fatigue at the edge:

* **Stage 1 (Binary Triage):** **99.45% Accuracy** with absolute **zero false positives (0% FPR)** out of 218,737 baseline operational samples.
* **Stage 2 (Multi-class Identification):** **98.34% Global Accuracy** under severe multi-path fading:
  * *DDoS Flooding:* **100% Precision**
  * *Coordinate Location Spoofing:* **97% Precision**
  * *Kinematic Data Manipulation:* **96% Precision**

---

## Repository Structure

Below is the roadmap of the files included in this repository to ensure full reproducibility:

- **Simulation & Map Files (SUMO):**
  - `capital.net.xml`: Urban road network for the NAC Iconic Tower scenario.
  - `capital.rou.xml`: Vehicle traffic flows and routes.
  - `capital.sumocfg`: SUMO environment simulation config.
  - `cbd_small.osm`: OpenStreetMap data file for the target area.

- **Python Core Scripts:**
  - `Train__Binary_Classifier_Phase_1.py`: Training script for Stage 1 detector.
  - `Train__Binary_Classifier_Phase_2.py`: Training script for Stage 2 classifier.
  - `run_benchmarking_comparison.py`: Execution script for model evaluation.
  - `plot_confusion_matrices.py`: Script to generate confusion matrix figures.
  - `plot_dataset_comparison.py`: Script for visual dataset comparison.

- **Trained Models & Evaluation Results:**
  - `vanet_phase1_detector.pkl`: Pre-trained weights for Stage 1.
  - `vanet_phase2_classifier.pkl`: Pre-trained weights for Stage 2.
  - `*.png`: Generated evaluation plots and matrices.
