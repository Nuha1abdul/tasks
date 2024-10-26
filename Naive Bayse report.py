import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report

# تحميل البيانات
file_path = 'C:/Users/Nasee/Downloads/diabetes_prediction_dataset.csv'
df = pd.read_csv(file_path)

# إعداد البيانات
X = df.drop('diabetes', axis=1)
y = df['diabetes']

# تحويل البيانات الفئوية إلى عددية
X = pd.get_dummies(X, drop_first=True)

# تقسيم البيانات إلى مجموعة تدريب واختبار
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# تدريب النموذج
model = GaussianNB()
model.fit(X_train, y_train)

# التنبؤ
y_pred = model.predict(X_test)

# حساب الدقة
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

# حفظ النتائج في ملف نصي
with open('classification_report.txt', 'w') as f:
    f.write(f"Accuracy: {accuracy}\n")
    f.write("Classification Report:\n")
    f.write(report)

print("تم حفظ التقرير في ملف classification_report.txt")
