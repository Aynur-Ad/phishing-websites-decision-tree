# Phishing Web Sitelerinin Decision Tree Algoritması ile Sınıflandırılması

## Proje Hakkında

Bu proje, Bursa Teknik Üniversitesi Bilgisayar Mühendisliği Bölümü **BLM0463 Veri Madenciliğine Giriş** dersi kapsamında hazırlanmıştır.

Projenin amacı, UCI Machine Learning Repository üzerinde bulunan **Phishing Websites** veri setini kullanarak web sitelerinin phishing (oltalama amaçlı sahte site) veya legitimate (güvenli site) olarak sınıflandırılmasını sağlamaktır.

Bu amaçla makine öğrenmesi yöntemlerinden **Decision Tree (Karar Ağacı)** algoritması kullanılmıştır.

---

## Veri Seti

**Veri Seti Adı:** Phishing Websites

**Kaynak:** UCI Machine Learning Repository

**Toplam Kayıt Sayısı:** 11055

**Özellik Sayısı:** 30

**Hedef Değişken:** Result

### Sınıf Dağılımı

| Sınıf | Açıklama            |
| ----- | ------------------- |
| 1     | Phishing Web Sitesi |
| -1    | Güvenli Web Sitesi  |

---

## Kullanılan Teknolojiler

* Python 3.12
* Pandas
* Scikit-Learn
* Matplotlib
* Seaborn
* SciPy

---

## Proje Yapısı

```text
phishing-decision-tree
│
├── data
│   └── Training Dataset.arff
│
├── outputs
│   ├── confusion_matrix.png
│   ├── feature_importance.png
│   └── decision_tree.png
│
├── src
│   └── main.py
│
├── README.md
└── requirements.txt
```

---

## Veri Ön İşleme

Projede aşağıdaki veri ön işleme adımları uygulanmıştır:

* ARFF veri setinin okunması
* Byte formatındaki verilerin integer formata dönüştürülmesi
* Eksik veri kontrolü
* Özellik ve hedef değişkenlerin ayrılması
* Eğitim ve test kümelerinin oluşturulması

Veri setinde eksik veri bulunmamaktadır.

---

## Kullanılan Makine Öğrenmesi Algoritması

Bu projede aşağıdaki parametrelerle oluşturulan Decision Tree modeli kullanılmıştır:

```python
DecisionTreeClassifier(
    criterion="gini",
    max_depth=5,
    random_state=42
)
```

Veri seti:

* %80 Eğitim Verisi
* %20 Test Verisi

olarak ayrılmıştır.

---

## Elde Edilen Sonuçlar

| Performans Ölçütü    | Sonuç  |
| -------------------- | ------ |
| Accuracy             | %92.67 |
| Precision            | %91.15 |
| Recall (Sensitivity) | %96.18 |
| Specificity          | %88.27 |
| F1-Score             | %93.60 |

### Confusion Matrix

|                 | Tahmin: Güvenli | Tahmin: Phishing |
| --------------- | --------------- | ---------------- |
| Gerçek Güvenli  | 865             | 115              |
| Gerçek Phishing | 47              | 1184             |

---

## Oluşturulan Grafikler

Program çalıştırıldığında aşağıdaki görseller oluşturulmaktadır:

* Confusion Matrix
* Feature Importance Grafiği
* Decision Tree Görselleştirmesi

Bu görseller `outputs` klasörüne kaydedilmektedir.

---

## Projeyi Çalıştırma

Gerekli kütüphaneleri yüklemek için:

```bash
pip install -r requirements.txt
```

Projeyi çalıştırmak için:

```bash
python src/main.py
```

---

## Sonuç

Bu çalışmada Decision Tree algoritması kullanılarak phishing web sitelerinin sınıflandırılması gerçekleştirilmiştir.

Elde edilen %92.67 doğruluk oranı, modelin phishing web sitelerini başarılı şekilde tespit edebildiğini göstermektedir. Özellikle %96.18 Recall değeri, phishing sitelerinin büyük çoğunluğunun doğru şekilde yakalandığını ortaya koymaktadır.

---

## Hazırlayan

**Aynur Adıbelli**

Bursa Teknik Üniversitesi

Bilgisayar Mühendisliği

2026
