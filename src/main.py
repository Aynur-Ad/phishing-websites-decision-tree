import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from scipy.io import arff

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)


# 1. Veri setini oku
data, meta = arff.loadarff("data/Training Dataset.arff")
df = pd.DataFrame(data)


# 2. Byte -> String -> Integer dönüşümü
for col in df.columns:
    df[col] = df[col].str.decode("utf-8")
    df[col] = df[col].astype(int)


# 3. Veri setini incele
print("İlk 5 satır:")
print(df.head())

print("\nVeri boyutu:")
print(df.shape)

print("\nEksik veri sayısı:")
print(df.isnull().sum().sum())

print("\nSınıf dağılımı:")
print(df["Result"].value_counts())

print("\nVeri tipleri:")
print(df.dtypes)


# 4. Özellikler ve hedef değişken
X = df.drop("Result", axis=1)
y = df["Result"]

print("\nX boyutu:", X.shape)
print("y boyutu:", y.shape)


# 5. Eğitim-Test ayrımı
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nEğitim veri boyutu:")
print(X_train.shape)

print("\nTest veri boyutu:")
print(X_test.shape)


# 6. Decision Tree modelini oluştur ve eğit
model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=5,
    random_state=42
)

model.fit(X_train, y_train)


# 7. Test verisi üzerinde tahmin yap
y_pred = model.predict(X_test)


# 8. Performans metriklerini hesapla
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, pos_label=1)
recall = recall_score(y_test, y_pred, pos_label=1)
f1 = f1_score(y_test, y_pred, pos_label=1)

cm = confusion_matrix(y_test, y_pred)

tn, fp, fn, tp = cm.ravel()
specificity = tn / (tn + fp)


# 9. Sonuçları ekrana yazdır
print("\nAccuracy:")
print(accuracy)

print("\nPrecision:")
print(precision)

print("\nRecall (Sensitivity):")
print(recall)

print("\nSpecificity:")
print(specificity)

print("\nF1 Score:")
print(f1)

print("\nConfusion Matrix:")
print(cm)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# 10. Confusion Matrix grafiği
plt.figure(figsize=(6, 5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues"
)

plt.title("Confusion Matrix")
plt.xlabel("Tahmin")
plt.ylabel("Gerçek")

plt.savefig("outputs/confusion_matrix.png")
plt.show()


# 11. Feature Importance grafiği
importance = pd.Series(
    model.feature_importances_,
    index=X.columns
)

importance = importance.sort_values(ascending=False)

plt.figure(figsize=(12, 8))

sns.barplot(
    x=importance.head(10).values,
    y=importance.head(10).index
)

plt.title("En Önemli 10 Özellik")
plt.xlabel("Önem Değeri")
plt.ylabel("Özellikler")

plt.tight_layout()

plt.savefig("outputs/feature_importance.png", bbox_inches="tight")
plt.show()


# 12. Decision Tree görseli
plt.figure(figsize=(20, 10))

plot_tree(
    model,
    feature_names=X.columns,
    class_names=["Legitimate", "Phishing"],
    filled=True,
    rounded=True,
    fontsize=8
)

plt.savefig("outputs/decision_tree.png")
plt.show()