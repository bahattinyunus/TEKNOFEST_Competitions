
<div align="center">


# 🏆 Teknofest Robolig: Otonom Futbolun Zirvesi

> **Özet:** Robolig; sadece robotik bir montaj değil, sahadaki dinamikleri anlık okuyan, strateji kuran ve rakibi alt eden bir **Yapay Zeka** mücadelesidir. Global arenadaki *RoboCup Small Size League (SSL)* standartlarını esas alır.

---

## ⚽ 1. Yarışma Formatı ve Saha Dinamiği

Oyun, insan müdahalesi olmadan tamamen otonom akar.

* **👥 Format:** Genellikle **3v3** veya **4v4** (Yıllık şartnameye bağlı).
* **🕹️ Otonomi:** Başlama düdüğünden itibaren kumanda/joystick yasaktır.
* **⛳ Saha:** Yeşil halı zemin, beyaz çizgiler.
* **🟠 Top:** Görüntü işlemede kolay ayrışması için genellikle **turuncu golf topu**.
* **📡 Hakem:** *Referee Box* yazılımı üzerinden yönetilir. Hakem kararları (Başla, Dur, Faul) kablosuz ağ ile robotlara sinyal olarak gider.

---

## 👁️ 2. Çalışma Prensibi: Global Vision Sistemi

Robolig'de robotlar genellikle "Tanrı Bakış Açısı" (God's Eye View) ile yönetilir.

| Adım | İşlem | Detay |
| :--- | :--- | :--- |
| **1. Göz** | **Tepe Kamera** | Sahayı kuş bakışı gören kamera, tüm görüntüyü alır. |
| **2. Algı** | **SSL-Vision** | Görüntüden robotların $X, Y$ koordinatlarını ve yönelim açılarını ($\theta$) çıkarır. |
| **3. Beyin** | **Yapay Zeka** | Ana bilgisayar veriyi işler: *"Top bende mi? Şut mu çekmeliyim?"* kararını verir. |
| **4. İletim** | **Haberleşme** | Hesaplanan hız vektörleri ($V_x, V_y, \omega$) telsiz (NRF/WiFi) ile robotlara yollanır. |

---

## 🛠️ 3. Robot Donanımı (Anatomi)

Bir Robolig robotu, standart bir robottan çok daha çevik ve karmaşıktır.

### 🔩 Mekanik ve Elektromekanik Bileşenler

* **🔄 Hareket (Omni-Drive):** Robot gövdesini döndürmeden her yöne gidebilmelidir. Genellikle **3 veya 4 adet Omni tekerlek** kullanılır.
* **🔨 Vuruş (Kicker):** Solenoid bobinler ve yüksek voltajlı kapasitörler kullanılır. Anlık deşarj ile topa sert bir darbe uygulanır.
* **🌀 Top Tutma (Dribbler):** Robotun önündeki dönen silikon rulo, topa ters spin vererek robot hareket halindeyken topun "ayağa yapışmasını" sağlar.

### ⚡ Elektronik Altyapı

* **Motorlar:** Maxon, Faulhaber veya yüksek kaliteli fırçasız (BLDC) motorlar.
* **İşlemci:** Düşük seviye kontrol (Motor sürme, sensör okuma) için **STM32 (F4/F7)** serisi.

---

## 💻 4. Yazılım Katmanları (Sihrin Gerçekleştiği Yer)

Robolig'i kazandıran donanım değil, **koddur**.

### 🧠 Kritik Algoritmalar

1.  **Yol Planlama (Path Planning):**
    * *Amaç:* A'dan B'ye giderken rakibe çarpma.
    * *Yöntem:* **RRT (Rapidly-exploring Random Tree)** veya **A* (A-Star)**.

2.  **Oyun Stratejisi (State Machine):**
    * `Durum: DEFANS` $\rightarrow$ Kaleyi kapat.
    * `Durum: ATAK` $\rightarrow$ Boşluk bul ve şut çek.
    * `Durum: DESTEK` $\rightarrow$ Pas kanalı oluştur.

3.  **Kontrol Teorisi (PID):**
    * Robotun istenilen konuma milimetrik oturması için **PID** kontrolcüsü şarttır.
    * Matematiksel Model: $u(t) = K_p e(t) + K_d \frac{de}{dt} + K_i \int e(\tau)d\tau$

---

## 📅 5. Hazırlık Yol Haritası

1.  **📜 Şartnameyi Ezberle:** Kurallar (boyut, ağırlık) her şeydir.
2.  **virtual Simülasyon:** Robotu üretmeden kodunu yaz. (**GrSim**, **Webots**, **Gazebo**).
3.  **📦 Tedarik:** Omni tekerlek ve motorlar yurt dışından gelebilir, erken sipariş ver.
4.  **⚙️ Tuning (İnce Ayar):** Mekanik bittikten sonra PID katsayılarını ayarlamak günler sürer.

---

> ### 💡 Jüri İçin Altın İpucu
>
> Teknik raporda ve sunumda sadece "Yaptık" demeyin. **Mühendislik kararlarınızı** savunun:
> * *"Neden 4 tekerlekli omni yerine 3 tekerlekli seçtik?"*
> * *"Neden A* algoritması yerine RRT kullandık?"*
>
> **Trade-off (Ödünleşim) analizi yapan takımlar her zaman öne geçer.**

---

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
