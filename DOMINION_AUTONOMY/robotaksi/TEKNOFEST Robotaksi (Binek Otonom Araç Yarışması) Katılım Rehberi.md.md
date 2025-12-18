🚗💡 TEKNOFEST Robotaksi (Binek Otonom Araç Yarışması) Katılım Rehberi

Hazırlayan: GPT-5 x Bahattin Yunus Çetin  
Amaç: Robotaksi yarışmasına katılmak isteyen öğrencilere teknik, idari ve stratejik bir yol haritası sunmak.  
Seviye: Başlangıç – Orta – İleri

## İçindekiler
- [🎯 Yarışmanın Amacı ve Felsefesi](#-yarışmanın-amacı-ve-felsefesi)
- [⚙️ Kategoriler: Özgün vs. Hazır Araç](#️-kategoriler-özgün-vs-hazır-araç)
- [👥 Takım Kurulumu](#-takım-kurulumu)
- [📝 Başvuru Süreci ve Belgeler](#-başvuru-süreci-ve-belgeler)
- [🧠 Araç Geliştirme Süreci (Teknik)](#-araç-geliştirme-süreci-teknik)
- [🧩 Simülasyon ve Test Süreci](#-simülasyon-ve-test-süreci)
- [💰 Sponsorluk ve Finans Yönetimi](#-sponsorluk-ve-finans-yönetimi)
- [🧾 Raporlama ve Sunum Teknikleri](#-raporlama-ve-sunum-teknikleri)
- [🏁 Final (Pistte Yarışma)](#-final-pistte-yarışma)
- [🧩 Yarışma Sonrası – Kazanımlar](#-yarışma-sonrası--kazanımlar)
- [🗓️ Örnek Katılım Takvimi](#️-örnek-katılım-takvimi)
- [💬 Kapanış – Deneyim Tavsiyeleri](#-kapanış--deneyim-tavsiyeleri)

## 1. 🎯 Yarışmanın Amacı ve Felsefesi
TEKNOFEST Robotaksi Yarışması, Türkiye’nin otonom sürüş teknolojilerinde bağımsızlık hedefini destekleyen en kapsamlı öğrenci yarışmasıdır.

Amaçlar:
- Yapay zekâ, sensör füzyonu ve otomotiv elektroniği alanlarında yetkin gençler yetiştirmek
- Takımların gerçek dünyada çalışan otonom sistemler geliştirmesini sağlamak
- Takım kültürü, proje yönetimi ve mühendislik pratiği kazandırmak

Felsefe: “Hazır sistemleri sadece kullanan değil, kendi akıllı araçlarını geliştiren bir gençlik!” — yani sadece bir yarışma değil, bir mühendislik okulu.

## 2. ⚙️ Kategoriler: Özgün vs. Hazır Araç

| Özellik | Özgün Araç Kategorisi | Hazır Araç Kategorisi |
|---|---|---|
| Zorluk | Yüksek | Orta |
| Araç | Takım kendi aracını üretir. | TEKNOFEST sağladığı platformu kullanır. |
| Donanım | Şasi, motor, fren, sensörler takıma ait. | Sensörler ve mekanik sistem hazır gelir. |
| Odak Noktası | Tüm sistem entegrasyonu (donanım + yazılım) | Yazılım, sensör verisi işleme, rota planlama |
| Yeni Başlayanlar İçin | ⚠️ Zor ama öğretici | ✅ Başlamak için ideal |
| Örnek | KTÜ KATOT | OİB Autonomous, Kapsül RacLab |

## 3. 👥 Takım Kurulumu
Roller:
- Takım Kaptanı: Genel koordinasyon, zaman yönetimi, rapor takibi
- Yazılım Ekibi: ROS, Python/C++, sensör verisi işleme, karar algoritmaları
- Donanım Ekibi: Motor kontrolü, elektronik bağlantılar, güç sistemi
- Mekanik Ekibi: Şasi tasarımı, fren ve süspansiyon sistemleri
- Algoritma/AI Ekibi: Görüntü işleme, obje tespiti, rota planlama
- Finans & Sponsorluk: Sponsorluk dosyası, bütçe, sunumlar
- Tanıtım & Sosyal Medya: Logo, video, basın, görseller

Notlar:
- İdeal takım büyüklüğü: 6–10 kişi
- Üniversite danışmanı (öğretim üyesi) zorunludur

## 4. 📝 Başvuru Süreci ve Belgeler
1) Kayıt: [teknofest.org](https://teknofest.org) adresinden başvuru yapılır. Takım bilgileri, danışman, kategori ve iletişim detayları doldurulur.
2) Teknik Yeterlilik Formu (TYF): Araç konsepti, ekip yapısı, başlangıç planı, elektronik altyapı, kontrol şeması, yazılım planı. Amaç: “Bu takım yarışabilecek mi?”
3) Kritik Tasarım Raporu (KTR): Sistem mimarisi, test planı, devre şemaları, sensör yerleşimi. Profesyonel görünüm önemlidir (ör. Canva, LaTeX, SolidWorks render).
4) Video & Simülasyon: Yazılımın sanal ortam testi ve video sunumu; trafik işaretleri ve engellere uygun tepki.
5) Final Onayı: TÜBİTAK değerlendirmesinden geçip finalist listesinde yer aldıktan sonra pistte yarışma hakkı.

## 5. 🧠 Araç Geliştirme Süreci (Teknik)
Temel Bileşenler:
- Algılama (Perception): Kamera, LiDAR, radar, GPS, IMU; OpenCV, YOLO, TensorFlow, ROS
- Karar Verme (Decision): Rota planlama, engel kaçınma, dur-kalk; PID, durum makineleri, NN tabanlı kararlar
- Kontrol (Actuation): Motor, fren, direksiyon; CAN-Bus veya UART haberleşmesi
- Yazılım Çatısı: ROS/ROS2, Gazebo veya CARLA, Python/C++

Donanım Önerileri:

| Donanım | Açıklama |
|---|---|
| NVIDIA Jetson Xavier / Nano | Görüntü işleme için güçlü GPU |
| Raspberry Pi 4 | Kontrol ve küçük hesaplamalar |
| Hokuyo / Velodyne LiDAR | 2D/3D haritalama |
| Intel RealSense D435 | Derinlik kamerası |
| ZED Stereo Camera | Geniş görüş alanlı stereo görme |
| Arduino / STM32 | Sensör veri toplama ve aktüasyon kontrolü |
| GPS + IMU Modülü | Navigasyon verisi sağlamak için |

## 6. 🧩 Simülasyon ve Test Süreci
- CARLA Simulator: Gerçekçi şehir ortamında test
- Gazebo + ROS: Fiziksel sensör modellemesi
- RViz: Gerçek zamanlı veri görselleştirme
- Python Unit Test / rosbag record: Log analizi

Tavsiye: Her sürüş testinde verileri .bag olarak kaydet ve hataları analiz et (ör. “Lidar delay > 100ms → perception lag → PID offset”).

## 7. 💰 Sponsorluk ve Finans Yönetimi
Sponsorluk dosyası içeriği:
- Takım tanıtımı, geçmiş başarılar (yoksa hedefler)
- Sosyal medya hesapları, logolar, üniversite desteği
- Talep edilen destek kalemleri (sensör, batarya, yazılım lisansı)

İpuçları:
- LinkedIn/Instagram üzerinden markalara ulaş
- Kurumsal e-posta aç: katot.trabzon@ktu.edu.tr gibi
- TÜBİTAK ulaşım/konaklama desteği, Üniversite BAP fonu

## 8. 🧾 Raporlama ve Sunum Teknikleri
- Raporları sade ama teknik tut; “Neden böyle tasarladık?” sorusunu cevapla
- Sunumda demo video, şema, grafik, algoritma akışı kullan
- Yazı tipi: Roboto/Lato; Renk paleti: sade (beyaz-mavi-gri)

## 9. 🏁 Final (Pistte Yarışma)
Hazırlık:
- Araç taşıma planı (kargo/karayolu)
- Yedek batarya, kablo, lehim kiti, laptop, SD kart, internet paylaşımı
- Yazılım için “failsafe mode” başlangıcı

Pist Görevleri:
- Start çizgisinden otonom kalkış
- Trafik levhalarına göre dur-kalk
- Park etme
- Engelden kaçma
- Dönüş manevraları
- Bitirme çizgisine güvenli ulaşım

Pro tip: Her testte `rosbag record` çalıştır; sonrasında log analizi yap.

## 10. 🧩 Yarışma Sonrası – Kazanımlar
- CV’de “TEKNOFEST Robotaksi Yarışmacısı” ifadesi büyük artıdır
- Ekip üyeleri ASELSAN, HAVELSAN, Togg, Bilişim Vadisi, Ford Otosan vb. yerlerde staj/iş fırsatı bulabilir
- Proje devamı: TÜBİTAK 2209-A/1512, start-up, üniversite labları

## 🗓️ Örnek Katılım Takvimi

| Ay | Görev |
|---|---|
| Aralık–Ocak | Takım kurulumu, kategori seçimi |
| Şubat | TEKNOFEST başvurusu, TYF hazırlığı |
| Mart–Nisan | KTR ve ilk simülasyon denemeleri |
| Mayıs–Haziran | Araç üretimi / testleri |
| Temmuz | Video gönderimi, finale hazırlık |
| Ağustos | Bilişim Vadisi’nde final |
| Eylül | Sonuçlar, ödül töreni, değerlendirme raporu |

## 💬 Kapanış – Deneyim Tavsiyeleri
- Başlangıçta her şey karmaşık görünebilir; uzmanlaşma ile işler hızlanır
- “Bir kişi her şeyi bilsin” değil, “herkes bir konuda iyi olsun” yaklaşımı
- Sürüm kontrolü (GitHub/GitLab) şart
- Her adımı belgeleyin; rapor zamanı loglar ve ekran görüntüleri kurtarıcıdır
- Takım ruhunu koruyun: TEKNOFEST bir yarışmadan fazlası, büyük bir mühendislik festivalidir