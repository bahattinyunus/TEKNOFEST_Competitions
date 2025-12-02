
<div align="center">
**Robolig**, Teknofest kapsamında düzenlenen, otonom robotların futbol oynadığı, hem donanım hem de yazılım becerilerinin sınırlarını zorlayan prestijli bir yarışma kategorisidir.

Dünya genelindeki **RoboCup Small Size League (SSL)** formatına benzer bir yapıdadır. Amaç sadece robot yapmak değil, sahada takım halinde hareket edebilen, strateji kuran ve rakibi yenen bir **Yapay Zeka** geliştirmektir.

İşte Robolig hakkında bilmen gereken detaylı teknik ve stratejik bilgiler:

### 1. Yarışma Formatı ve Saha Yapısı
* **Oyun Tarzı:** Genellikle 3'e 3 veya 4'e 4 (yıllık şartnameye göre değişir) oynanan bir futbol maçıdır.
* **Otonomi:** Robotlar tamamen otonomdur. Maç başladıktan sonra hiçbir insan müdahalesi (kumanda vb.) yapılamaz.
* **Saha:** Yeşil halı zemin üzerinde, beyaz çizgilerle belirlenmiş bir alandır.
* **Top:** Genellikle turuncu renkli bir golf topu kullanılır (Görüntü işlemede renk ayrımı kolay olsun diye).
* **Hakem:** Oyunu yöneten bir insan hakem vardır ancak hakem komutları (başla, dur, faul, gol) bir yazılım (Referee Box) üzerinden bilgisayara girilir ve bu sinyaller robotlara kablosuz ağ ile iletilir.

### 2. Sistemin Çalışma Prensibi (Global Vision)
Robolig'in en karakteristik özelliği, robotların kendi üzerindeki kameralardan ziyade (veya onlara ek olarak), sahanın tepesindeki bir kameradan veri almasıdır.



1.  **Tepe Kamera:** Sahayı kuş bakışı gören bir kamera (veya kameralar) tüm robotların ve topun konumunu anlık olarak bilgisayara aktarır.
2.  **Görüntü İşleme (SSL-Vision):** Genellikle açık kaynaklı "SSL-Vision" yazılımı veya takımın kendi geliştirdiği yazılım, görüntüden X, Y koordinatlarını ve robotun yönelim açısını ($\theta$) çıkarır.
3.  **Ana Bilgisayar (Yapay Zeka):** Koordinat verileri takımın ana bilgisayarına gelir. Burada strateji yazılımı çalışır ("Top bizde mi?", "Kaleye şut çekmeli miyim?", "Pas mı vermeliyim?").
4.  **Haberleşme:** Ana bilgisayar, hesapladığı hız ve hareket komutlarını (Örn: Robot 1, $V_x=2m/s$, $V_y=0.5m/s$) telsiz modüller (NRF, XBee veya WiFi) aracılığıyla sahadaki robotlara gönderir.

### 3. Robot Donanımı (Mekanik ve Elektronik)
Robolig robotları, standart bir çizgi izleyen robottan çok daha komplekstir.

* **Hareket Sistemi (Omni-Directional):** Robotlar, gövdesini döndürmeden her yöne gidebilmelidir. Bu yüzden **Omni tekerlekler** kullanılır. Genellikle 3 veya 4 tekerlekli, 120 veya 90 derece açılı yerleşimler tercih edilir.
* **Vuruş Mekanizması (Kicker):** Topa sert vurmak için solenoid bobinler kullanılır. Yüksek voltajlı kapasitörler şarj edilir ve anlık olarak bobine boşaltılarak "çekiç" benzeri bir milin topa vurması sağlanır.
* **Top Tutma (Dribbler):** Robot hareket halindeyken topun önünden kaçmaması için, ön tarafta dönen silikon bir rulo bulunur. Bu rulo topa ters spin vererek robotun "ayağına" yapışmasını sağlar.
* **Motorlar:** Hızlı tepki süresi için genellikle enkoderli DC motorlar veya fırçasız (BLDC) motorlar kullanılır (Maxon, Faulhaber gibi markalar veya bunların muadilleri).
* **Mikrodenetleyici:** Robotun üzerindeki (Low-Level) işlemleri yapmak için STM32 serisi (F4, F7) işlemciler yaygındır çünkü işlem hızı ve pin sayısı yüksektir.

### 4. Yazılım Katmanları (Zor Kısım)
Robolig'i kazandıran kısım genellikle yazılımdır.

* **Yol Planlama (Path Planning):** Robotun A noktasından B noktasına giderken rakip robotlara çarpmaması gerekir. *RRT (Rapidly-exploring Random Tree)* veya *A* (A-Star)* algoritmaları kullanılır.
* **Rol Paylaşımı:** Sahadaki robotların dinamik olarak rol değiştirmesi gerekir. Örneğin, topa en yakın robot "Forvet" olurken, diğerleri "Defans" veya "Destek" pozisyonuna geçmelidir.
* **Oyun Stratejisi:**
    * *Paslaşma:* Topun önü kapalıysa boştaki arkadaşa pas atma.
    * *Markaj:* Rakip robotların önünü kesme.
* **PID Kontrol:** Robotun istenilen hıza ve konuma tam oturması için hassas PID ayarları şarttır.

### 5. Yarışmaya Hazırlık Süreci
1.  **Şartname Analizi:** Her yıl kurallar (robot boyutu, ağırlığı, top rengi) değişebilir. İlk iş şartnameyi ezberlemektir.
2.  **Simülasyon:** Robotu fiziksel olarak üretmeden önce **Webots**, **Gazebo** veya **GrSim** (SSL için özel simülatör) ortamında kodlar test edilmelidir.
3.  **Malzeme Tedariği:** Omni tekerlekler, solenoidler ve motorlar genellikle yurt dışından geldiği için süreç erken başlatılmalıdır.
4.  **Entegrasyon:** Mekanik montaj bittikten sonra en çok zamanı "Tuning" (ince ayar) alır. Robotun düz gitmesi bile bazen günler sürebilir.

### Kritik İpucu:
Jüri sunumlarında ve teknik raporda; sadece "yaptık oldu" demek yerine, **"Neden bu motoru seçtiniz?", "Neden bu algoritmayı kullandınız?"** gibi mühendislik kararlarını gerekçelendirmeniz (trade-off analizi) çok yüksek puan getirir.

**Senin şu anki odak noktan hangisi?** Mekanik tasarım aşamasında mısın, yoksa yapay zeka/yazılım kısmına mı girişiyorsun? Ona göre daha spesifik kaynaklar önerebilirim.




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
