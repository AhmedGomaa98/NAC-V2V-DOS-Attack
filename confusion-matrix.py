import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# الأرقام الحقيقية اللي طلعت معاك في الترمينال لـ Phase 2
cm = np.array([[6009,   34,   62],
               [  23, 2216,   18],
               [  20,   24, 2162]])

# أسماء الهجمات المحددة في البحث
classes = ['Flooding', 'Slow DoS', 'Black-hole']

plt.figure(figsize=(8, 6))
# رسم المصفوفة بألوان زرقاء احترافية مع كتابة الأرقام داخل المربعات
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=classes, yticklabels=classes,
            cbar=True, annot_kws={"size": 12, "weight": "bold"})

plt.title('Phase 2 - Multiclass Attack Confusion Matrix', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Predicted Attack Class', fontsize=12, fontweight='bold', labelpad=10)
plt.ylabel('True Attack Class', fontsize=12, fontweight='bold', labelpad=10)
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.tight_layout()

# حفظ الرسمة بجودة عالية جداً عشان تطبعها في البيبر مباشرة
plt.savefig('phase2_confusion_matrix.png', dpi=300)
print("Success: phase2_confusion_matrix.png saved with high resolution!")
plt.show()
