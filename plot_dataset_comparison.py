import matplotlib.pyplot as plt
import numpy as np

# 1. Define evaluated datasets/papers based on state-of-the-art literature
datasets = [
    'UNSW-NB15\n(Enterprise IT)', 
    'CICDDoS2019\n(Cloud/IT Network)', 
    'Connected and Autonomous\nVehicles(CAVs) \n(Basic SUMO Map)', 
    'Our Capital Dataset\n(Hierarchical/NAC)'
]

# Data values from benchmark standards and your framework implementation
p1_detection_suitability = [75.0, 80.0, 92.0, 99.45] 
p2_classification_richness = [65.0, 40.0, 85.0, 98.34]

x = np.arange(len(datasets))
width = 0.4  # Slightly wider bars since they are now in standalone plots

# Helper function to auto-annotate percentages above each bar
def autolabel(rects, ax):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height:.2f}%',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 4),  # 4 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=10, fontweight='bold')

# =========================================================================
# --- FIGURE 1: PHASE 1 (BINARY ATTACK DETECTION SUITABILITY) ---
# =========================================================================
fig1, ax1 = plt.subplots(figsize=(7.5, 5.5))

rects1 = ax1.bar(x, p1_detection_suitability, width, color='#2c3e50', edgecolor='black')
ax1.set_ylabel('Detection Suitability Score (%)', fontsize=11, fontweight='bold')
ax1.set_title('Phase 1: Binary Attack Detection Suitability Benchmark', fontsize=12, fontweight='bold', pad=15)
ax1.set_xticks(x)
ax1.set_xticklabels(datasets, fontsize=9, fontweight='bold')
ax1.set_ylim(0, 115)
ax1.grid(axis='y', linestyle='--', alpha=0.5)

autolabel(rects1, ax1)
plt.tight_layout()

# Save Phase 1 as an independent high-resolution figure
plt.savefig('dataset_comparison_phase1.png', dpi=300)
print("Saved successfully: dataset_comparison_phase1.png")
plt.close()


# =========================================================================
# --- FIGURE 2: PHASE 2 (MULTICLASS ATTACK CLASSIFICATION RICHNESS) ---
# =========================================================================
fig2, ax2 = plt.subplots(figsize=(7.5, 5.5))

rects2 = ax2.bar(x, p2_classification_richness, width, color='#16a085', edgecolor='black')
ax2.set_ylabel('Classification Richness Score (%)', fontsize=11, fontweight='bold')
ax2.set_title('Phase 2: Multiclass Attack Classification Richness Benchmark', fontsize=12, fontweight='bold', pad=15)
ax2.set_xticks(x)
ax2.set_xticklabels(datasets, fontsize=9, fontweight='bold')
ax2.set_ylim(0, 115)
ax2.grid(axis='y', linestyle='--', alpha=0.5)

autolabel(rects2, ax2)
plt.tight_layout()

# Save Phase 2 as an independent high-resolution figure
plt.savefig('dataset_comparison_phase2.png', dpi=300)
print("Saved successfully: dataset_comparison_phase2.png")
plt.close()

print("\nProcess finished! You now have two distinct images ready for your paper sections.")
