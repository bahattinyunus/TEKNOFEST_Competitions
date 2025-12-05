

````markdown
# 🛡️ TEKNOFEST — Savaşan İHA (Fighter UAV)

![ROS2](https://img.shields.io/badge/ROS2-Humble-22314E?style=for-the-badge&logo=ros&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![C++](https://img.shields.io/badge/C%2B%2B-17-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white)
![YOLOv8](https://img.shields.io/badge/YOLO-v8-00FFFF?style=for-the-badge&logo=yolo&logoColor=black)
![PX4](https://img.shields.io/badge/PX4-Autopilot-333333?style=for-the-badge&logo=px4&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

> **"Gökyüzü bizim oyun alanımız; algoritmalar ise en güçlü silahımız."** 🚀

Bu repo, **TEKNOFEST Savaşan İHA Kategorisi** için geliştirdiğimiz tam otonom hava aracı, yer sistemleri, kontrol algoritmaları, simülasyon ortamı ve görev yazılımlarının tümünü içerir.

Hedefimiz: Tam otonom, çevik, hızlı karar verebilen ve engellere/tehditlere karşı taktiksel manevra yapabilen bir insansız hava aracı geliştirmek. 🛩️💥

---

## 📌 İçerik Başlıkları

- [🎯 Proje Amacı](#-proje-amacı)
- [📚 Genel Sistem Mimarisi](#-genel-sistem-mimarisi)
- [🧠 Otonomi & Algoritmalar](#-otonomi--algoritmalar)
- [📂 Proje Yapısı](#-proje-yapısı)
- [🚁 Donanım Yapılandırması](#-donanım-yapılandırması)
- [🧪 Simülasyon Ortamı](#-simülasyon-ortamı)
- [🛠️ Kurulum](#-kurulum)
- [📈 Performans ve Test Sonuçları](#-performans-ve-test-sonuçları)
- [🤝 Katkıda Bulunma](#-katkıda-bulunma)

---

## 🎯 Proje Amacı

Savaşan İHA kategorisinin temel hedefleri doğrultusunda sistemimiz şunları sağlar:

* 🤖 **Tam Otonomi:** Kalkıştan inişe insan müdahalesiz uçuş.
* 🎯 **Hedef Tespiti:** Rakip İHA'ların görüntü işleme ile kilitlenmesi.
* ⚔️ **Dogfight:** Yakın hava muharebesi manevraları ve takip.
* 🚧 **Engel Kaçınma:** Dinamik ve statik engellere karşı reaktif planlama.

---

## 📚 Genel Sistem Mimarisi

```mermaid
graph TD;
    GCS[Yer İstasyonu] -->|Telemetri 915MHz| FC[Uçuş Kontrolcüsü];
    FC -->|MAVLink| O[Otonomi Çekirdeği ROS2];
    O -->|Kontrol Komutları| FC;
    CAM[Kamera] -->|Video Akışı| AI[Yapay Zeka Modülü];
    AI -->|Hedef Koordinatları| O;
    O -->|Durum Bilgisi| GCS;
````

*Alternatif ASCII Görünümü:*

```text
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

-----

## 🧠 Otonomi & Algoritmalar

Bu projede kullanılan ana otonomi modülleri:

### ✅ 1. Hedef Tespit & Takip

  * **Model:** YOLOv8 / YOLO-NAS
  * **Optimizasyon:** TensorRT ile Jetson üzerinde gerçek zamanlı çıkarım.
  * **Takip:** Frame-temelli takip + Kalman Filter.

### ✅ 2. Kaçınma & Manevra

  * **Planlama:** RRT\* (Rapidly-exploring Random Tree) tabanlı.
  * **Kontrol:** PID + LQR hibrit kontrolcü.
  * **Adaptasyon:** Dinamik hız ve irtifa yönetimi.

### ✅ 3. Dogfight Yapay Zekâsı

  * **Tahmin:** Rakip İHA'nın hız-vektör tahmini.
  * **Öngörü:** Predictive modeling ile gelecek konum hesaplama.
  * **Taktik:** Takip konisine göre en uygun saldırı pozisyonunu alma.

-----

## 📂 Proje Yapısı

```bash
savasan-iha/
├── docs/               # Dokümantasyon ve şemalar
├── firmware/           # PX4/ArduPilot özel parametreleri
├── hardware/           # 3D baskı dosyaları (.stl) ve PCB şemaları
├── ros2_ws/            # ROS2 Çalışma Alanı
│   ├── src/
│   │   ├── autonomy/   # Otonom uçuş algoritmaları
│   │   ├── perception/ # Görüntü işleme ve YOLO düğümleri
│   │   └── simulation/ # Gazebo dünyaları ve modelleri
├── scripts/            # Kurulum ve yardımcı scriptler
└── README.md           # Şu an buradasınız
```

-----

## 🚁 Donanım Yapılandırması

| Bileşen | Detaylar |
| :--- | :--- |
| **Gövde** | 5"–7" Karbon Fiber Custom Frame |
| **Motor & ESC** | 2306/2207 FPV Serisi / 45A–60A ESC |
| **Otopilot** | Pixhawk 4 / Cube Orange |
| **Companion PC** | Nvidia Jetson Orin Nano / Xavier NX |
| **Kamera** | Global Shutter AI Camera + FPV Cam |
| **Sensörler** | Lidar (Opsiyonel), Optik Akış, GPS, Barometre |

-----

## 🧪 Simülasyon Ortamı

Gerçek uçuş öncesi kodlarımızı sanal ortamda zorluyoruz:

  * 🚀 **Gazebo:** ROS2 ile tam entegre fizik motoru.
  * 🌬️ **Çevresel Etkiler:** Rüzgar modellemesi ve türbülans.
  * 🎮 **AirSim:** Fotogerçekçi görüntü işleme testleri için.

-----

## 🛠️ Kurulum

Geliştirme ortamını kurmak için aşağıdaki adımları izleyin:

1.  **Repo’yu klonlayın:**

    ```bash
    git clone [https://github.com/kullanici/savasan-iha.git](https://github.com/kullanici/savasan-iha.git)
    cd savasan-iha
    ```

2.  **ROS2 & Bağımlılıkları kurun (Ubuntu 22.04):**

    ```bash
    sudo apt install ros-humble-desktop
    ```

3.  **Python gereksinimleri:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Simülasyonu başlatın:**

    ```bash
    ros2 launch iha_sim gazebo.launch.py
    ```

-----

## 📈 Performans ve Test Sonuçları

| Test | Sonuç | Durum |
| :--- | :--- | :---: |
| **Otonom Hedef Tespiti** | %92 Doğruluk | 🟢 |
| **Rota Planlama** | 32 ms ortalama | 🟢 |
| **Dogfight Takip** | Yüksek Stabilite | 🟢 |
| **Rüzgar Direnci** | 12 m/s'ye kadar stabil | 🟡 |
| **Engel Kaçınma** | %98 Başarı | 🟢 |

-----

## 🧩 Yol Haritası

  - [x] Temel Otonom Uçuş
  - [x] YOLO Entegrasyonu
  - [ ] Radar/ToF Sensör Füzyonu
  - [ ] Multi-Agent (Sürü) Karar Verme
  - [ ] Jetson Orin İçin Derin Optimizasyon

-----

## 🤝 Katkıda Bulunma

Açık kaynak ruhunu seviyoruz\! \<3

1.  Fork'layın.
2.  `feature/yeni-ozellik` dalı oluşturun.
3.  Değişikliklerinizi commit'leyin.
4.  Push'layın ve bir **Pull Request** açın.

-----

\<p align="center"\>
\<sub\>Bu proje TEKNOFEST ruhuyla 🇹🇷 geliştirilmiştir.\</sub\>
\</p\>

