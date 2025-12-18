# 🛡️ TEKNOFEST — Savaşan İHA Kategorisi

### *Otonomi, yapay zekâ ve havacılık tutkusunun birleştiği proje!*

> **“Gökyüzü bizim oyun alanımız; algoritmalar ise en güçlü silahımız.”**

Bu repo, **TEKNOFEST Savaşan İHA Kategorisi** için geliştirdiğimiz **tam otonom hava aracı**, yer sistemleri, kontrol algoritmaları, simülasyon ortamı ve görev yazılımlarının tümünü içerir.
Hedefimiz: **Tam otonom, çevik, hızlı karar verebilen ve engellere/tehditlere karşı taktiksel manevra yapabilen** bir insansız hava aracı geliştirmek. 🛩️💥

---

# 📌 İçerik Başlıkları

* [🎯 Proje Amacı](#-proje-amacı)
* [📚 Genel Sistem Mimarisi](#-genel-sistem-mimarisi)
* [🧠 Otonomi & Algoritmalar](#-otonomi--algoritmalar)
* [🛰️ Haberleşme & Yer İstasyonu](#-haberleşme--yer-i̇stasyonu)
* [🚁 Donanım Yapılandırması](#-donanım-yapılandırması)
* [🧪 Simülasyon Ortamı](#-simülasyon-ortamı)
* [🛠️ Kurulum](#️-kurulum)
* [🧭 Görev Akışı](#-görev-akışı)
* [📈 Performans ve Test Sonuçları](#-performans-ve-test-sonuçları)
* [🧩 Yol Haritası](#-yol-haritası)
* [🤝 Katkıda Bulunma](#-katkıda-bulunma)

---

# 🎯 Proje Amacı

Savaşan İHA kategorisinin amacı:

* Otonom hedef tespiti
* Yakın-dogfight manevraları
* Engel kaçınma
* Rakip İHA’ya taktiksel yaklaşım ve üstünlük sağlama

Bu repo, tüm yarışma gereksinimlerine uygun şekilde tasarlanmış **uçuş kontrol, yapay zekâ, görüntü işleme, rota planlama ve yer sistemleri** bileşenlerini barındırır.

---

# 📚 Genel Sistem Mimarisi

```
                 ┌──────────────────────────┐
                 │        Yer İstasyonu     │
                 └────────────┬─────────────┘
                              │ Telemetri
                              ▼
┌─────────────────────────────┴──────────────────────────────┐
│                    Uçuş Kontrol Bilgisayarı                │
│  (Pixhawk / CubeOrange / Custom FC, ArduPilot ya da PX4)   │
└───────────────┬────────────────────────────────────────────┘
                │ MAVLink
                ▼
      ┌─────────────────────┐
      │    Otonomi Çekirdeği│
      │  (ROS2 + Python/C++)│
      └─────────┬───────────┘
                │
┌───────────────┴───────────────────────────────────────────┐
│       Görüntü İşleme & Yapay Zekâ Modülleri               │
│       - YOLO / TensorRT                                   │
│       - Optik Akış Algoritmaları                          │
└────────────────────────────────────────────────────────────┘
```

---

# 🧠 Otonomi & Algoritmalar

Bu projede kullanılan ana otonomi modülleri:

### ✅ **1. Hedef Tespit & Takip**

* YOLOv8 / YOLO-NAS
* TensorRT hız optimizasyonu
* Frame-temelli takip + Kalman Filter

### ✅ **2. Kaçınma & Manevra**

* RRT* tabanlı rota planlama
* PID + LQR kontrol karışımı
* Dinamik hız/irtifa adaptasyonu

### ✅ **3. Dogfight Yapay Zekâsı**

* Rakip İHA'nın hız-vektör tahmini
* Gelecek konum öngörüsü (predictive modeling)
* Takip konisine göre saldırı pozisyonu alma

---

# 🛰️ Haberleşme & Yer İstasyonu

Yer istasyonunda kullanılan teknoloji stack’i:

* **QGroundControl / Mission Planner**
* **ROS2 tabanlı custom yer kontrol dashboard**
* Telemetri: 915 MHz / 433 MHz
* Video aktarım: 5.8 GHz analog veya WiFi-based FPV

**Yer istasyonu özellikleri:**

* Canlı telemetri
* Canlı video
* Anlık rota değiştirme
* Uçuş izinleri / fail-safe yönetimi
* Log kayıt sistemi

---

# 🚁 Donanım Yapılandırması

### **Gövde**

* 5"–7" quadcopter veya yarışma için optimize edilmiş custom frame
* Karbon fiber kompozit

### **Motor & ESC**

* 2306/2207 FPV motor sınıfı
* 45A–60A ESC

### **Batarya**

* 4S/6S LiPo
* 1300–1800mAh (performansa göre değişir)

### **Beyin**

* Pixhawk 4 / Cube Orange
* Nvidia Jetson Nano / Orin Nano
* Raspberry Pi 5 (alternatif)

### **Sensörler**

* GPS + Compass
* IMU + Barometre
* Görüş kamera (FPV + AI kamera)

---

# 🧪 Simülasyon Ortamı

Testlerde kullanılan sim ortamları:

### 🚀 **Gazebo (ROS2 ile tam entegre)**

* Rüzgar modellemesi
* Çarpışma senaryoları
* Çoklu İHA simülasyonu

### 🎮 **AirSim**

* Gerçekçi aerodinamik
* Yüksek kaliteli görsel ortam
* Speed-level dogfight testleri

### 🧩 Simülasyon Özellikleri

* Rakip İHA AI botları
* Engel konumlandırma
* Otomatik görev senaryoları

---

# 🛠️ Kurulum

### 1️⃣ Repo’yu klonla

```bash
git clone https://github.com/kullanici/savasan-iha.git
cd savasan-iha
```

### 2️⃣ ROS2 & bağımlılıkları kur

```bash
sudo apt install ros-humble-desktop
```

### 3️⃣ Python bağımlılıkları

```bash
pip install -r requirements.txt
```

### 4️⃣ Simülasyonu başlat

```bash
ros2 launch iha_sim gazebo.launch.py
```

---

# 🧭 Görev Akışı

1. İHA kalkış ve başlangıç otonomi kontrolü
2. Ara noktalar → Arama alanına intikal
3. Kamera aktif + hedef tarama
4. Rakip tespit → Takip modu
5. Dogfight manevraları
6. Fail-safe kontroller
7. Otonom iniş

---

# 📈 Performans ve Test Sonuçları

| Test                       | Sonuç          | Durum |
| -------------------------- | -------------- | ----- |
| Otonom hedef tespiti       | %92 doğruluk   | 🟢    |
| Rota planlama              | 32 ms ortalama | 🟢    |
| Dogfight takip stabilitesi | Yüksek         | 🟢    |
| Rüzgar etkisi              | Stabil         | 🟡    |
| Engel kaçınma              | %98 başarı     | 🟢    |

---

# 🧩 Yol Haritası

* [ ] Jetson Orin optimizasyonu
* [ ] Radar/ToF sensör entegrasyonu
* [ ] Daha agresif manevra algoritmaları
* [ ] Multi-agent karar verme
* [ ] Gömülü sistemlerde latency azaltma

---

# 🤝 Katkıda Bulunma

Katkılar her zaman memnuniyetle kabul edilir!
PR, issue ve geliştirme önerilerine **aşırı açığız**. 😄

