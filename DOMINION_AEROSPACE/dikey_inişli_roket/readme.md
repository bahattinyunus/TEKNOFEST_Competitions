

# Ne bu yarışma, kısaca?

TEKNOFEST çatısı altında TÜBİTAK SAGE yürütücülüğünde düzenlenen “Dikey İnişli Roket Yarışması”; takımlar yerçekimli dünyada **dikey ve kontrollü iniş** yapan roketler tasarlayıp uçuruyor — hedef, roket itkili iniş teknolojilerini öğrencilere öğretmek ve uygulamalar geliştirmek. Yarışma üç aşamalı rapor (ön tasarım, kritik tasarım, atış-hazırlık) ve test/atış serileri içeriyor. ([teknofest.org][1])

# Önemli kurallar / teknik kısıtlar (özeti)

* Roketler **yarışma komitesinin sağladığı Havada Askıda Tutma Sistemi** (ör. vinç/askı) ile uyumlu olmalı — yani sistemle entegrasyon düşünülmeli. ([teknofest.org][1])
* İniş için çoğu takım **soğuk gaz/itme sistemi (cold gas) veya küçük itki üniteleri** kullanıyor; atış-hazırlık raporunda iniş sistemi, güvenlik ve uçuş prosedürlerini açıklamak gerekiyor. ([TÜBİTAK][2])
* Değerlendirme: tasarım raporları + yer testleri + gerçek atış performansı (hedefe dik iniş, yumuşak iniş, kontrol hassasiyeti). Finalde dereceye girenlere ciddi ödüller (ör. 1.’ye ~250.000 TL, 2.’ye ~200.000 TL, 3.’ye ~150.000 TL gibi son yıllarda açıklanan miktarlar). ([TÜBİTAK][3])

# Yarışma süreci (pratik akış)

1. **Takım & rol belirle** (aşağıda öneri)
2. **Ön tasarım raporu** — fiziksel tasarım konsepti, itki tipi, güvenlik konsepti, temel aerodinamik/ketter. ([teknofest.org][4])
3. **Kritik tasarım raporu** — ayrıntılı yapısal hesaplar, tahrik/itki sistemi çizimleri, GNC (guidance, navigation, control) stratejisi.
4. **Atış-hazırlık raporu & test planı** — test standları, ayrıntılı uçuş profili, acil kesme (abort) prosedürleri. Ardından TÜBİTAK SAGE Lalahan’da yer testleri / atış izinleri. ([TÜBİTAK][2])

# Takım yapısı — kim ne yapar (2–8 kişilik ideal)

* Takım lideri / proje yöneticisi (takvim, raporlar, iletişim)
* Yapısal & mekanik mühendis (gövde, motor mount, itki mekanikleri)
* İtki & propulsyon uzmanı (soğuk gaz/mini-motor tasarımı, tedarik)
* GNC & kontrol mühendisi (sensör füzyonu, kontrol algoritmaları)
* Aviyonik & yazılım geliştirici (telemetri, uçuş yazılımı, ground-station) — burada sen parlayabilirsin.
* Test & güvenlik sorumlusu (yer testleri, risk değerlendirme)

# Teknik bileşenler & tavsiyeler (yüksek fayda / düşük maliyet taktikleri)

* **İtki:** yarışma şartlarına göre cold-gas itki veya küçük sıvı/katı itki kullanımı; for landing, cold-gas iticiler daha yönetilebilir ve güvenlik açısından avantajlı. (yarışma dokümanlarında cold-gas vurgusu var). ([TÜBİTAK][2])
* **GNC (guidance/navigation/control):** IMU + GNSS (GPS/GLONASS) + barometre + LIDAR/ultrasonik veya radar altimetre (iniş yüksekliğini hassas tutmak için). Kontrol: PID başlangıç, kritik aşamalarda Model Predictive Control (MPC) veya adaptive kontrol.
* **Aviyonik & yazılım:** gerçek zamanlı uçuş yazılımı (RTOS tercih edilir), fail-safe katman, telemetri + ground control GUI (websocket / MQTT). Testler için HIL (hardware in the loop) simülasyonu şart.
* **Yapı & malzeme:** kompozit/AL yapı karışımı; iniş ayakları darbeyi absorbe edecek şekilde tasarlanmalı (crumple zones veya darbeyi yayacak piston/uzun mesafe amortisörler).
* **Simülasyon:** OpenRocket/ROCKSIM veya benzeri ile aero hesapları; Python/Simulink ile dinamik simülasyon; Gazebo veya custom simülasyon ile kontrol algoritmalarını test et.
* **Güvenlik:** uçuş izinleri, no-fly zone kontrolleri, ‘flight termination’ (RF kill / pyrotechnic or mechanical kill) prosedürleri mutlaka raporda yazılmalı.

# Test planı — hızlı ama güvenli döngü

1. Parça-parça yer testleri (itki tüp testi, soğuk-gaz nozzle testleri)
2. Aviyonik HIL testi (IMU/GPS sinyal simülasyonu)
3. Mini-scale uçuşlar (1/3 ölçek) — benzetim ile karşılaştırma
4. Tam boy test atışları ve iniş denemeleri, önce kontrollü ortamda (askı sistemiyle), sonra serbest atış. (TÜBİTAK Lalahan test tarihleri/izinleri takip edilir). ([TÜBİTAK][2])

# Kontrol algoritması önerisi (uygulaması hızlı)

* Yüksek seviye: yol noktası planlama + durum makinesi (ascent → coast → deorbit/burn → terminal descent → touchdown)
* Terminal descent: altimetre tabanlı hız kontrolü + yatay konum için gövde-itki vektörleştirme
* Basit başlangıç: cascaded PID (attitude & thrust) → geliştirme: LQR veya MPC

# Riskler & nasıl kırarsın

* Motor/itki arızası → flight-termination + acil paraşüt geri çekme (eğer yarışma izin veriyorsa)
* GNSS kaybı → IMU dead-reckoning + görsel odometri (kamera tabanlı) fallback
* Yapısal kırılma → yeniden tasarım, malzeme testleri ve safety-factor’ları arttır

# Kaynaklar / resmi dokümanlar (önemli referanslar)

* Yarışma sayfası ve teknik dokümanlar (kurallar, askı sistemi bilgisi). ([teknofest.org][1])
* TÜBİTAK duyuruları: atış-hazırlık raporu ve Lalahan testleri hakkındaki resmi açıklamalar. ([TÜBİTAK][2])
* Yarışma ödülleri ve final sonuçları duyuruları. ([TÜBİTAK][3])

---


[1]: https://www.teknofest.org/tr/yarismalar/dikey-inisli-roket-yarismasi/?utm_source=chatgpt.com "Dikey İnişli Roket Yarışması"
[2]: https://tubitak.gov.tr/en/announcement/vertical-landing-rocket-competition-launch-preparation-report-results-announced?utm_source=chatgpt.com "Vertical Landing Rocket Competition Launch Preparation ..."
[3]: https://tubitak.gov.tr/tr/haber/dikey-inisli-roket-yarismasi-sona-erdi?utm_source=chatgpt.com "Dikey İnişli Roket Yarışması Sona Erdi"
[4]: https://www.teknofest.org/en/content/announcement/teknofest-2025-vertical-landing-rocket-competition-preliminary-design-report-results-announced/?utm_source=chatgpt.com "Announcements"
