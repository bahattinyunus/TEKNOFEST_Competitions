
<div align="center">

# 🏆 [TAKIM ADI] - ROBOLIG 2025
### "Kodun Sahaya İndiği Yer: Tam Otonom, Yüksek Performans"

![Logo](https://via.placeholder.com/800x200?text=TAKIM+LOGO+BANNER+BURAYA)

[![Teknofest](https://img.shields.io/badge/Teknofest-2025-red?style=for-the-badge&logo=rocket)](https://www.teknofest.org/)
[![ROS 2](https://img.shields.io/badge/ROS2-Humble-green?style=for-the-badge&logo=ros)](https://docs.ros.org/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/Computer_Vision-OpenCV-orange?style=for-the-badge&logo=opencv)](https://opencv.org/)
[![License](https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge)](LICENSE)

<br/>

[Web Sitemiz](#) • [Demo Videosu](#) • [Teknik Rapor](#)

</div>

---

## ⚽ Proje Hakkında

**[TAKIM ADI]**, Teknofest Robolig yarışması için tasarlanmış, stratejik yapay zeka algoritmalarıyla donatılmış tam otonom bir futbol robotudur. Hedefimiz sadece topa vurmak değil; **sahayı okumak, rakibi analiz etmek ve en optimize rotayı çizerek skora gitmektir.**

Bu repo, robotun **gözü (kamera sistemleri)**, **beyni (karar mekanizmaları)** ve **kasları (motor sürücüleri)** arasındaki tüm yazılım mimarisini içerir.

### 🔥 Temel Özellikler

* 🤖 **Yüksek Seviye Otonomi:** İnsan müdahalesi olmadan tam maç performansı.
* 👁️ **Gelişmiş Görüntü İşleme:** YOLOv8 tabanlı top ve kale tespiti (5ms latency).
* 🗺️ **Dinamik Yol Planlama:** A* ve DWA (Dynamic Window Approach) hibrit kullanımı.
* ⚡ **Omni-Directional Hareket:** 360 derece serbest hareket kabiliyeti.
* 📡 **Takım İçi Haberleşme:** UDP üzerinden robotlar arası anlık veri transferi.

---

## 🛠️ Sistem Mimarisi ve Teknoloji Yığını

Robotumuzun başarısı, donanım ve yazılımın kusursuz senkronizasyonuna dayanır.

| Alan | Teknolojiler / Donanımlar |
| :--- | :--- |
| **Yazılım Dili** | Python, C++ |
| **Middleware** | ROS 2 (Robot Operating System) |
| **Görüntü İşleme** | OpenCV, PyTorch, YOLOv8 |
| **Ana Bilgisayar** | NVIDIA Jetson Orin Nano / Raspberry Pi 5 |
| **Mikrodenetleyici**| STM32F4 / ESP32 |
| **Simülasyon** | Gazebo, Rviz |

### 🧠 Kontrol Algoritması (PID)

Robotun hedefe hassas bir şekilde kilitlenmesi ve sarsıntısız duruşu için gelişmiş bir PID (Proportional-Integral-Derivative) kontrolcüsü kullanıyoruz. Matematiksel modelimiz:

$$u(t) = K_p e(t) + K_i \int_{0}^{t} e(\tau) d\tau + K_d \frac{de(t)}{dt}$$

Burada:
* $e(t)$: Hedef açı ile mevcut açı arasındaki hata.
* $K_p, K_i, K_d$: Dinamik olarak ayarlanan katsayılar.

---

## 📸 Galeri ve Demo

| Top Takibi | Rviz Haritalama | Gol Vuruşu |
| :---: | :---: | :---: |
| ![Tracking](https://via.placeholder.com/250x150?text=GIF+1) | ![Mapping](https://via.placeholder.com/250x150?text=GIF+2) | ![Goal](https://via.placeholder.com/250x150?text=GIF+3) |

---

## 🚀 Kurulum ve Çalıştırma

Projeyi yerel ortamınızda çalıştırmak için aşağıdaki adımları izleyin.

### Gereksinimler
* Ubuntu 22.04 LTS
* ROS 2 Humble
* CUDA (Eğer NVIDIA Jetson kullanılıyorsa)

### 1. Repoyu Klonlayın
```bash
git clone [https://github.com/kullaniciadi/robolig-projesi.git](https://github.com/kullaniciadi/robolig-projesi.git)
cd robolig-projesi
````

### 2\. Bağımlılıkları Yükleyin

```bash
pip install -r requirements.txt
rosdep install --from-paths src --ignore-src -r -y
```

### 3\. Projeyi Derleyin

```bash
colcon build --symlink-install
source install/setup.bash
```

### 4\. Başlatın 🏁

```bash
# Ana otonom sürüş düğümünü başlatır
ros2 launch robolig_bringup main_match.launch.py
```

-----

## 👥 Takım Kadrosu

Bu proje, uykusuz geceler ve litrelerce kahve eşliğinde geliştirildi.

  * 👑 **[Adın Soyadın]** - *Takım Kaptanı & Yapay Zeka Lideri*
  * 💻 **[Üye Adı]** - *Gömülü Sistemler Mimarı*
  * ⚙️ **[Üye Adı]** - *Mekanik Tasarım & Üretim*
  * 🔌 **[Üye Adı]** - *Elektronik Devre Tasarımı*

-----

## 🤝 Sponsorlarımıza Teşekkürler

Bize inanan ve destekleyen kurumlar:

\<div align="center"\>
\<img src="https://www.google.com/search?q=https://via.placeholder.com/100x50%3Ftext%3DSponsor1" width="100" /\>
\<img src="https://www.google.com/search?q=https://via.placeholder.com/100x50%3Ftext%3DSponsor2" width="100" /\>
\<img src="https://www.google.com/search?q=https://via.placeholder.com/100x50%3Ftext%3DSponsor3" width="100" /\>
\</div\>

-----

\<div align="center"\>

### Bu projeyi beğendiniz mi?

Lütfen sağ üst köşedeki ⭐ **Star** butonuna basarak bize destek olun\!

2025 © [TAKIM ADI] - Tüm Hakları Saklıdır.

\</div\>

```
