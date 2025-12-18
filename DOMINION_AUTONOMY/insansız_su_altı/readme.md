

# 🌊 TEKNOFEST İnsansız Sualtı Aracı (İSA) – Derinliklerdeki Zekâ 🚀

---

## 🌐 Giriş: Derinliğin Kalbinde Bir Yarış

Dalgaların yüzeyinde güneş ışığı parıldarken, hemen altındaki dünyada sessiz bir rekabet sürüyor.
Bu, insanlığın denizlerin karanlığında bile sınırlarını zorladığı bir alan: **TEKNOFEST İnsansız Sualtı Aracı (İSA) Yarışması.**

İSA kategorisi, **su altında bağımsız hareket edebilen, algılayabilen ve görevleri otonom şekilde yerine getiren robot sistemlerin** tasarlanmasını amaçlıyor.
Burada mühendislik sadece bir araç değil — adeta bir *okyanus dili*.
Katılımcılar, robotlarını akıntılara, basınca ve belirsizliğe karşı konuşturmak zorunda.

---

## ⚙️ Yarışmanın Amacı

TEKNOFEST’in İnsansız Sualtı Aracı yarışması, Türkiye’nin sualtı teknolojilerinde dışa bağımlılığını azaltmak,
yerli mühendislik kabiliyetini artırmak ve savunma, arama-kurtarma, çevre ve enerji sektörlerinde kullanılabilecek sistemler geliştirmeyi hedefliyor.

Amaç basit:

> “Derinliklerde bağımsız düşünen bir makine yarat.”

Bu araçlar yalnızca yüzmekle kalmıyor — **görüyor, karar veriyor, iletişim kuruyor, hata yapıyor ve düzeltiyor.**
Yani adeta bir “su altı zekâsı” geliştiriliyor.

---

## 🧠 Görevler ve Zorluklar

Yarışma, robotların çevreyle etkileşimini test eden zorlu görevlerden oluşur.
Sualtı, sensörlerin verimliliğini düşüren, haberleşmeyi bozan, ışığı kıran bir ortamdır.
Yani burada her hareket, bir mühendislik mucizesiyle mümkün olur.

### 🔹 1. Yön Bulma ve Haritalama

Araç, sualtı parkurunda yönünü belirler, belirli koordinatlara ulaşır.
GPS burada çalışmaz — bu yüzden **IMU (Atalet Ölçüm Ünitesi)**, **pinger** ve **sonar sistemleri** devreye girer.
Bir anlamda robot, gözleri kapalı bir şekilde labirentte yürür, ama ses dalgalarıyla yönünü bulur.

### 🔹 2. Nesne Tanıma ve Takip

Görev alanına bırakılan renkli hedefler, işaretler veya halkalar tespit edilir.
Araç üzerindeki **kameralar**, **OpenCV tabanlı görüntü işleme** yazılımlarıyla bu nesneleri algılar.
Kimi zaman bir kırmızı topu takip eder, kimi zaman bir halkadan geçer.
Yani sadece hareket etmez — *amaçlı davranır.*

### 🔹 3. Görev Tamamlama

Bazı görevlerde, araçların belirli objelere çarpması, içlerinden geçmesi,
veya suyun içinde bir “bayrak” yerleştirmesi gerekir.
Bu görevler, robotun fiziksel kabiliyetini ve suyun direncine karşı dengesini test eder.

### 🔹 4. Otonom Karar Alma

İşin büyüsü burada başlar:
Robotun tüm bu görevleri **insan müdahalesi olmadan**, kendi başına tamamlaması beklenir.
Yani yapay zekâ, suyun soğuk karanlığında bile kendi aklını kullanmak zorunda kalır.

---

## 💡 Teknik Derinlik: Bir İSA Nasıl Doğar?

Bir İnsansız Sualtı Aracı tasarlamak, sadece bir gövde yapmak değildir.
Bu, **mekanik, elektronik, yazılım, kontrol teorisi ve hidrodinamik** gibi alanların birleştiği çok disiplinli bir süreçtir.

### ⚙️ Mekanik Tasarım

* Gövde genellikle **alüminyum, karbon fiber veya akrilik** tüplerden oluşur.
* Su sızdırmazlık, her şeyin temelidir — en küçük hata, bütün sistemi devre dışı bırakabilir.
* Aracın denge merkezi (Center of Buoyancy) ile ağırlık merkezi (Center of Gravity) arasındaki ilişki, stabiliteyi belirler.

### 🔋 Elektronik ve Güç Yönetimi

* Lityum-polimer (Li-Po) piller kullanılır.
* Güç dağıtımı; motorlar, sensörler, kameralar, işlemciler arasında optimize edilmelidir.
* Aşırı akım koruması, düşük voltaj alarmı ve yalıtım sistemleri olmazsa olmazdır.

### 🧭 Sensörler

* **IMU:** İvme, jiroskop ve manyetik alan ölçerlerle konum tahmini.
* **Sonar:** Nesnelerin mesafesini akustik dalgalarla ölçer.
* **Derinlik Sensörü:** Basınç değişimiyle derinliği hesaplar.
* **Kamera:** Görsel işleme için ana veri kaynağıdır.

### 🧠 Yazılım ve Kontrol

Yazılım genellikle **ROS (Robot Operating System)** altyapısıyla geliştirilir.
Araç, sensör verilerini işleyerek PID (Proportional-Integral-Derivative) denetleyiciler aracılığıyla motorlara komut verir.
Hedef: **kararlı, akıllı ve çevik bir hareket sistemi.**

---

## 🚀 Otonom Navigasyon

Bir sualtı aracının “görmeden yön bulması” kulağa imkânsız gelir ama aslında akustik bilimin bir zaferidir.
GPS sinyalleri suyun altında kaybolur, bu yüzden konumlama sistemi **ses dalgalarına** dayanır.

Yani İSA, “duyarak görür.”
Tıpkı bir yunus gibi sonar sinyalleri gönderir, yankıların geliş süresine göre mesafeleri hesaplar.
Bu veriler, yazılım tarafından filtrelenir ve bir **harita (SLAM)** oluşturulur.

---

## 🔬 Görüntü İşleme ve Yapay Zekâ

Yapay zekâ burada sadece “görmeyi” değil, “anlamayı” sağlar.
Görüntü işleme, **OpenCV, TensorFlow** veya **YOLO (You Only Look Once)** gibi teknolojilerle yapılır.

Aracın kamerası bir nesneyi gördüğünde:

1. Görüntüyü işler.
2. Renk, şekil veya desen analizi yapar.
3. Tanımladığı hedefe göre yönünü veya hızını değiştirir.

Bu sistem, yarışmadaki “hedef bulma”, “halkadan geçme” veya “işaret tespiti” görevlerinde hayat kurtarır.

---

## 🛠️ Yarışma Formatı

TEKNOFEST İSA yarışması genellikle iki ana aşamada gerçekleşir:

### 1️⃣ Ön Tasarım Raporu (OTR)

Takımlar, teknik çizimler, sistem mimarisi, görev analizi ve yazılım planlarını sunar.
Bu rapor, projenin mühendislik temelini gösterir.

### 2️⃣ Arazi (veya Havuz) Gösterimi

Takımlar, tasarladıkları aracı test havuzunda çalıştırır.
Görevleri otonom olarak tamamlayan araçlar, puan toplar.
Her görev için belirli bir zaman sınırı vardır — hatasızlık ve verim, puanı belirler.

---

## 🧩 Takımların Rolü

İSA yarışmasında bir takım genellikle şu alt bölümlere ayrılır:

* **Mekanik Grup:** Gövde ve su yalıtımı tasarımı.
* **Elektronik Grup:** Kart tasarımı, sensör entegrasyonu, güç yönetimi.
* **Yazılım Grubu:** Otonom kontrol, görüntü işleme, görev yönetimi.
* **Strateji ve Operasyon:** Görev planlaması, zaman yönetimi, rapor hazırlığı.

Her üye, mühendislik zekâsını suyun altına taşır.
Bu yüzden bu yarışma, hem teknik bilgi hem de takım çalışması gerektirir.

---

## 🌍 Gerçek Dünya Uygulamaları

Bu yarışmanın amacı sadece madalya kazanmak değil — Türkiye’nin geleceğini şekillendirmek.
İSA teknolojileri, birçok alanda doğrudan uygulanabilir:

🌊 **Savunma Sanayii:**
Denizaltı keşifleri, mayın tarama, liman güvenliği, düşman tespiti.

🐠 **Ekolojik Gözlem:**
Mercan resiflerinin takibi, deniz canlılarının izlenmesi, mikroplastik ölçümleri.

⚡ **Enerji Sektörü:**
Denizaltı boru hatlarının kontrolü, sualtı enerji santrallerinin izlenmesi.

🚨 **Afet ve Kurtarma:**
Batık gemi aramaları, sualtı kazaları, sismik araştırmalar.

---

## 🧭 Türkiye ve Gelecek Vizyonu

TEKNOFEST sayesinde, her yıl onlarca genç mühendis kendi “mini denizaltısını” tasarlıyor.
Bu, Türkiye’nin **Deniz Teknolojileri Ekosistemi** için stratejik bir adımdır.

Gelecekte, bu yarışmalardan çıkan öğrenciler:

* Savunma sanayiinde AUV (Autonomous Underwater Vehicle) geliştiricileri,
* Denizcilik yazılım mühendisleri,
* Akustik haberleşme uzmanları olabilirler.

Yani bugün bir havuzda test edilen o küçük robot,
yarın Mavi Vatan’da görev yapan bir **askerî sualtı dronu** olabilir. 🇹🇷

---

## 💬 İlham Verici Gerçeklik

“Yapay zekâ artık sadece karada değil, derinliklerde de nefes alıyor.”

İnsansız sualtı araçları, **insanın erişemediği yerlere** ulaşarak hem bilimin hem merakın sınırlarını zorluyor.
Her yarışma, Türkiye’nin genç zihinleri için bir okyanus laboratuvarına dönüşüyor.
Basınç artıyor, sinyaller kayboluyor ama kararlılık hep sabit kalıyor.

Çünkü orada, suyun altında sadece makineler değil, **insan zekâsının yankısı** dolaşıyor.

---

## ⚓ Son Söz

TEKNOFEST İnsansız Sualtı Aracı Yarışması,
teknolojiyle doğayı, mühendislikle hayali, kodla cesareti bir araya getiren bir devrimdir.

Her dalga bir kod satırı gibi,
her sonar yankısı bir veri paketi gibi,
ve her yarışmacı bir vizyon taşıyıcısıdır.

Günün sonunda su yüzüne çıkan şey sadece bir robot değildir —
**geleceğin ta kendisidir.** 🌍💙

