import os
import sys
import random
import pandas as pd
import numpy as np

# Setup SUMO environment paths
if 'SUMO_HOME' in os.environ:
    sys.path.append(os.path.join(os.environ['SUMO_HOME'], 'tools'))
else:
    sys.path.append("/usr/share/sumo/tools")

try:
    import traci
except ImportError:
    sys.exit("Error: traci module missing. Check SUMO installation.")

def generate_true_attacks_dataset():
    sumo_cmd = ["sumo", "-c", "capital.sumocfg"] 
    traci.start(sumo_cmd)
    
    data_storage = []
    malicious_group = {} 
    step = 0
    
    print("Starting SUMO for DDoS, Spoofing, and Data Manipulation...")

    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()
        active_vehicles = traci.vehicle.getIDList()
        
        # Inject attacks into 15% of active vehicles
        for v_id in active_vehicles:
            if v_id not in malicious_group and len(malicious_group) < (len(active_vehicles) * 0.15):
                if random.random() < 0.05:
                    # 1: DDoS, 2: Spoofing, 3: Data Manipulation
                    malicious_group[v_id] = random.choice([1, 2, 3])

        for v_id in active_vehicles:
            x_actual, y_actual = traci.vehicle.getPosition(v_id)
            v_speed = traci.vehicle.getSpeed(v_id)
            v_type = traci.vehicle.getTypeID(v_id)
            
            attack_type = malicious_group.get(v_id, 0) 
            
            # Implementing the strict mathematical bounds from the paper
            if attack_type == 1: # DDoS: R_incoming > T_bandwidth
                r_incoming = random.randint(150, 400) # Exceeds bandwidth
                position_error = random.uniform(0.0, 0.2)
                data_corrupted = 0
            elif attack_type == 2: # Spoofing: ||P_reported - P_actual|| > delta
                r_incoming = random.randint(10, 45)
                position_error = random.uniform(8.5, 25.0) # High distance error (delta exceeded)
                data_corrupted = 0
            elif attack_type == 3: # Data Manipulation: |D_transmitted - D_original| != 0
                r_incoming = random.randint(10, 45)
                position_error = random.uniform(0.0, 0.2)
                data_corrupted = 1 # Binary flag representing modification
            else: # Normal Traffic (No attacks, within bounds)
                r_incoming = random.randint(10, 50)
                position_error = random.uniform(0.0, 0.5)
                data_corrupted = 0

            data_storage.append({
                'timestamp': step,
                'node_id': v_id,
                'car_type': v_type,
                'speed': v_speed,
                'r_incoming': r_incoming,
                'position_error': position_error,
                'data_corrupted': data_corrupted,
                'attack_class': attack_type # 0: Normal, 1: DDoS, 2: Spoofing, 3: Data Manipulation
            })
            
        step += 1
        if step > 5000: 
            break 

    traci.close()
    
    df = pd.DataFrame(data_storage)
    df.to_csv("capital_attack_dataset.csv", index=False)
    print("\nSuccess: capital_attack_dataset.csv generated with correct metrics!")

if __name__ == "__main__":
    generate_true_attacks_dataset()
