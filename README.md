# Final-Project

## Sentiment Analysis

## Yapılacaklar
### - YouTube API ile yorumları çekme

### Anlamlı Kelimelerin Çıkarılması:

**1. Metin Temizleme:**
Gereksiz karakterleri ve noktalama işaretlerini kaldırın.
Büyük-küçük harf dönüşümü yapın.

**2. Stop Words:**
Türkçe'de yaygın olarak kullanılan "stop words" adı verilen, anlam taşımayan kelimeleri çıkarın. (NLTK)

**3. Tokenization:**
Metni kelimelere ayırın.

**4. Kök Çıkarma (Stemming) veya Lematizasyon:**
Kelimelerin köklerini çıkarmak veya lematize etmek, benzer anlamlı kelimeleri birleştirmenize yardımcı olabilir.

### - Sentiment Analizi yapmak için önceden eğitilmiş bir model

Sentiment analizi için önceden eğitilmiş bir model kullanabilirsiniz. Bu modeller, genellikle pozitif, negatif veya nötr olarak duygu durumunu tahmin eder. (Henüz modele karar verilmedi) (huggingface vb.)

### Duygu Durumu Analizi:

**1. Veri Seti Hazırlığı:**
Temizlenmiş ve işlenmiş yorumları içeren veri setinizi kullanarak, eğitim ve test veri setlerinizi oluşturun.

**2. Makine Öğrenmesi Modeli Seçimi:**
Projenize uygun bir makine öğrenmesi modeli seçin. Bu duygu analizi için sıkça kullanılan modeller arasında Destek Vektör Makineleri (SVM), Naive Bayes modeller kullanılabilir.

**3. Model Eğitimi:**
Seçtiğiniz modeli eğitmek için veri setinizi kullanın. Eğitim süreci, metin verileri üzerinde duygu durumunu tahmin etmek için modelinizi öğrenmesini içerir.

**4. Model Doğrulama:**
Eğitim veri setini kullanarak eğitilen modelinizi test veri seti üzerinde doğrulayın. Modelinizin performansını değerlendirin ve gerekirse hiperparametreleri ayarlayarak iyileştirme yapın.

**5. Duygu Analizi Uygulaması:**
Eğitilen modelinizi kullanarak YouTube API ile çektiğiniz yorumları analiz edin. Her yorumun pozitif, negatif veya nötr bir duygu durumu içerip içermediğini belirleyin.

**6. Sonuçları Görselleştirme:**
Duygu analizi sonuçlarını kullanıcı dostu bir şekilde görselleştirin. Grafikler veya raporlar kullanarak projenizin kullanıcılarına anlamlı bilgiler sunun.


pip install requirements.txt
- pip install pandas
- pip install google-api-python-client
