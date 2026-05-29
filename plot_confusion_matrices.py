import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# --- 1. PHASE 1 CONFUSION MATRIX DATA ---
# Numbers taken directly from your Phase 1 terminal output
cm_p1 = np.array([[218737,      0],
                  [  1240,   5762]])
classes_p1 = ['Normal', 'Under Attack']

# Plotting Phase 1
plt.figure(figsize=(7, 5.5))
sns.heatmap(cm_p1, annot=True, fmt='d', cmap='Reds', 
            xticklabels=classes_p1, yticklabels=classes_p1,
            cbar=True, annot_kws={"size": 13, "weight": "bold"})

plt.title('Phase 1 - Binary Perimeter Confusion Matrix', fontsize=13, fontweight='bold', pad=15)
plt.xlabel('Predicted Label', fontsize=11, fontweight='bold', labelpad=10)
plt.ylabel('True Label', fontsize=11, fontweight='bold', labelpad=10)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10, rotation=0)
plt.tight_layout()

# Save Phase 1 figure in high resolution
plt.savefig('phase1_confusion_matrix.png', dpi=300)
print("Saved: phase1_confusion_matrix.png")
plt.close()


# --- 2. PHASE 2 CONFUSION MATRIX DATA ---
# Numbers taken directly from your Phase 2 terminal output
cm_p2 = np.array([[4051,   38,   31],
                  [  10, 1596,   15],
                  [   7,   14, 1180]])
classes_p2 = ['DDoS', 'Spoofing', 'Data Manipulation']

# Plotting Phase 2
plt.figure(figsize=(8, 6.5))
sns.heatmap(cm_p2, annot=True, fmt='d', cmap='Blues', 
            xticklabels=classes_p2, yticklabels=classes_p2,
            cbar=True, annot_kws={"size": 12, "weight": "bold"})

plt.title('Phase 2 - Multiclass Attack Confusion Matrix', fontsize=13, fontweight='bold', pad=15)
plt.xlabel('Predicted Attack Type', fontsize=11, fontweight='bold', labelpad=10)
plt.ylabel('True Attack Type', fontsize=11, fontweight='bold', labelpad=10)
plt.xticks(fontsize=10, rotation=45)
plt.yticks(fontsize=10, rotation=0)
plt.tight_layout()

# Save Phase 2 figure in high resolution
plt.savefig('phase2_confusion_matrix.png', dpi=300)
print("Saved: phase2_confusion_matrix.png")
plt.close()

print("\nAll figures generated successfully! Check your current folder.")
