

# 🛰️ TEKNOFEST Model Uydu (CanSat) Yarışması Proje Dokümantasyonu

Bu repository, **TEKNOFEST [YIL] Model Uydu Yarışması** kapsamında **[TAKIM İSMİ]** tarafından geliştirilen model uydunun yazılım, elektronik ve mekanik tasarım dosyalarını, görev algoritmalarını ve yer istasyonu arayüzlerini içermektedir.

Projemiz, gerçek bir uydunun fırlatma, yörüngeye yerleşme, veri toplama ve veri aktarma süreçlerini simüle eden otonom bir sistem geliştirmeyi hedefler.

-----

## 📋 İçindekiler

1.  [Proje Hakkında](https://www.google.com/search?q=%23-proje-hakk%C4%B1nda)
2.  [Sistem Mimarisi](https://www.google.com/search?q=%23-sistem-mimarisi)
3.  [Görev Senaryosu ve Uçuş Profili](https://www.google.com/search?q=%23-g%C3%B6rev-senaryosu-ve-u%C3%A7u%C5%9F-profili)
4.  [Donanım Bileşenleri](https://www.google.com/search?q=%23-donan%C4%B1m-bile%C5%9Fenleri)
5.  [Yazılım Mimarisi](https://www.google.com/search?q=%23-yaz%C4%B1l%C4%B1m-mimarisi)
6.  [Kurulum ve Kullanım](https://www.google.com/search?q=%23-kurulum-ve-kullan%C4%B1m)
7.  [Klasör Yapısı](https://www.google.com/search?q=%23-klas%C3%B6r-yap%C4%B1s%C4%B1)
8.  [Yol Haritası (Timeline)](https://www.google.com/search?q=%23-yol-haritas%C4%B1-timeline)
9.  [Katkıda Bulunanlar](https://www.google.com/search?q=%23-katk%C4%B1da-bulunanlar)

-----

## 📝 Proje Hakkında

Model Uydu (CanSat) yarışması, bir uydunun/uzay aracının tasarlanması, üretilmesi ve görev sonrası raporlanması süreçlerini kapsar. Bu projede hedefimiz; belirlenen irtifaya roket ile taşınan model uydunun, roketten ayrıldıktan sonra **pasif iniş sistemi** ile kontrollü bir şekilde alçalması, bu sırada sensör verilerini (basınç, irtifa, sıcaklık, GPS konumu vb.) toplayıp **Yer İstasyonu**'na (Ground Station) aktarması ve görev yükünün taşıyıcıdan ayrılarak otonom iniş gerçekleştirmesidir.

### Temel Hedefler:

  * **Telemetri Aktarımı:** 1 Hz frekansında kesintisiz veri paketi gönderimi.
  * **Otonom Ayrılma:** Belirlenen irtifada (örn. 400m) taşıyıcı ve görev yükünün birbirinden ayrılması.
  * **Video Aktarımı:** Uçuş esnasında anlık görüntü aktarımı ve SD karta kayıt.
  * **İniş Kontrolü:** Paraşüt veya döner kanat sistemi ile hasarsız iniş (Max 14 m/s).

-----

## 🏗 Sistem Mimarisi

Sistemimiz üç ana modülden oluşmaktadır:

1.  **Uzay Segmenti (Flight Segment):** Uydunun kendisi (Taşıyıcı + Görev Yükü).
2.  **Yer Segmenti (Ground Segment):** Verileri alan anten sistemi ve arayüz yazılımı.
3.  **Haberleşme Linki:** LoRa modülleri üzerinden sağlanan RF haberleşme hattı.

-----

## 🚀 Görev Senaryosu ve Uçuş Profili

Uçuş yazılımımız aşağıdaki durum makinelerini (State Machine) yönetmek üzere tasarlanmıştır:

1.  **BEKLEME (IDLE):** Sistem açılır, sensör kalibrasyonları yapılır, GPS fix beklenir. Yer istasyonundan "BAŞLA" komutu beklenir.
2.  **YÜKSELME (ASCENT):** Roket ateşlenir. İvme sensörleri dikey hareketi algılar. Basınç azalır.
3.  **TEPE NOKTASI (APOGEE):** Roket en yüksek irtifaya ulaşır ve model uydu serbest kalır.
4.  **SÜRÜKLENME (DESCENT 1):** Taşıyıcı ve görev yükü birlikte paraşüt ile alçalır.
5.  **AYRILMA (SEPARATION):** 400 metre irtifada servo motorlar tetiklenir, görev yükü taşıyıcıdan ayrılır.
6.  **GÖREV YÜKÜ İNİŞİ (DESCENT 2):** Görev yükü kendi askı sistemiyle süzülür.
7.  **KURTARMA (LANDING):** Yere temas algılanır, buzzer ötmeye başlar, veri aktarımı durdurulur (veya paket formatı değişir).

-----

## 🛠 Donanım Bileşenleri

Sistemin kararlılığı için endüstriyel standartlara yakın bileşenler tercih edilmiştir.

### 🧠 Uçuş Bilgisayarı (Flight Controller)

  * **Mikrodenetleyici:** STM32F4 Serisi / Teensy 4.1 (Yüksek işlem gücü için)
  * **Sensörler:**
      * *IMU:* BNO055 / MPU6050 (Eksen eğikliği ve ivme verisi)
      * *Barometre:* BMP388 / MS5611 (Yüksek hassasiyetli irtifa verisi)
      * *GPS:* NEO-M8N (Konum takibi)
  * **Güç Yönetimi:** Li-Po Batarya (2S/3S) ve Voltaj Regülatörleri (Buck Converter).

### 📡 Haberleşme Sistemi

  * **Modül:** Ebyte E32-433T30D LoRa Modülü
  * **Anten:** 433 MHz Yagi Anten (Yer), 3dBi Dipole (Uydu)
  * **Frekans:** 433 MHz (ISM Bandı)

### ⚙️ Mekanik Tasarım

  * **Gövde:** PLA+ ve PETG filament ile 3D baskı parçalar.
  * **Ayrılma Mekanizması:** Mikro Servo Motor ve misina yakma/mekanik kilit sistemi.

[Image of model satellite exploded view CAD design]

-----

## 💻 Yazılım Mimarisi

### 1\. Gömülü Yazılım (Embedded)

STM32/Arduino tabanlı C++ kodu. `FreeRTOS` kullanılarak görevler önceliklendirilmiştir.

  * `Task_ReadSensors`: Sensör verilerini okur ve filtreler (Kalman Filtresi).
  * `Task_Telemetry`: Verileri paketler (CSV formatında) ve UART üzerinden LoRa'ya gönderir.
  * `Task_Decision`: İrtifa ve ivme verilerine göre uçuş aşamasına (State) karar verir.

### 2\. Yer İstasyonu (Ground Station)

C\# (WPF) veya Python (PyQt5) ile geliştirilmiş masaüstü uygulamasıdır.

  * **Özellikler:** Canlı grafik çizimi, 3D uydu oryantasyon görselleştirme (GL), harita üzerinde konum takibi, komut gönderme paneli.
  * **Veri Kaydı:** Gelen tüm paketleri `.csv` ve `.txt` olarak yedekler.

-----

## 📥 Kurulum ve Kullanım

Projeyi yerel makinenize klonlamak için:

```bash
git clone https://github.com/KULLANICI_ADI/PROJE_ADI.git
cd PROJE_ADI
```

### Gömülü Yazılımı Yükleme

1.  PlatformIO veya STM32CubeIDE kurun.
2.  `src/flight_software` klasörünü açın.
3.  Gerekli kütüphaneleri yükleyin (bkz: `library.json`).
4.  Kodu derleyin ve karta yükleyin.

### Yer İstasyonunu Çalıştırma (Python Örneği)

```bash
cd src/ground_station
pip install -r requirements.txt
python main.py
```

-----

## 📂 Klasör Yapısı

```
.
├── 📂 cad_files            # SolidWorks/Fusion360 tasarım dosyaları (.step, .stl)
├── 📂 circuit_design       # Altium/KiCad PCB şematikleri ve Gerber dosyaları
├── 📂 docs                 # Raporlar (PDR, CDR), teknik çizimler ve datasheetler
├── 📂 src
│   ├── 📂 flight_software  # STM32/Arduino gömülü yazılım kodları
│   └── 📂 ground_station   # Yer istasyonu arayüz kodları (GUI)
├── 📂 tests                # Birim testleri ve simülasyon verileri
├── .gitignore
├── LICENSE
└── README.md
```

-----

## 📅 Yol Haritası (Timeline)

  - [x] **Takım Kurulumu ve Literatür Taraması:** Tamamlandı.
  - [x] **Ön Tasarım Raporu (PDR):** Tamamlandı.
  - [ ] **Mekanik Üretim ve Prototipleme:** Devam Ediyor.
  - [ ] **Kritik Tasarım Raporu (CDR):** Bekleniyor.
  - [ ] **Sistem Entegrasyonu ve Test Uçuşları:** Planlanıyor.
  - [ ] **Uçuşa Hazırlık Raporu (QR):** Planlanıyor.
  - [ ] **Büyük Gün: Yarışma Finali\!**

-----

## 👥 Katkıda Bulunanlar

Bu proje **[TAKIM İSMİ]** üyeleri tarafından geliştirilmiştir.

  * **[İsim Soyisim]** - *Takım Kaptanı / Yazılım Lideri*
  * **[İsim Soyisim]** - *Mekanik Tasarım*
  * **[İsim Soyisim]** - *Elektronik ve Aviyonik*
  * **[İsim Soyisim]** - *Yer İstasyonu ve İletişim*

-----

> ⚠️ **Yasal Uyarı:** Bu proje eğitim ve yarışma amaçlıdır. RF haberleşme sistemleri yerel regülasyonlara (BTK) uygun kullanılmalıdır.

-----

### 🔗 Faydalı Bağlantılar

  - [TEKNOFEST Resmi Web Sitesi](https://www.teknofest.org/)
  - [Model Uydu Yarışması Şartnamesi](https://www.teknofest.org/tr/yarismalar/model-uydu-yarismasi/)

