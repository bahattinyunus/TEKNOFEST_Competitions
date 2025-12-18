## TEKNOFEST 2025 — **Güvenli Uydu Haberleşmesi Yarışması**

![Image](https://kirklareliarge.meb.gov.tr/meb_iys_dosyalar/2025_05/27152429_eb61fd6980ec464e86e63a7bb8538e9c.jpg)

![Image](https://www.qsl.net/ta1kb/aselsan/uyd.ht6.gif)

![Image](https://strasam.org/upload/resimler/c282e7d567.webp)

-
## 📁 Proje Yapısı (Başlangıç)

- docs/ — Yarışma dokümantasyonu, rapor şablonları ve diyagramlar
- src/
  - crypto/ — Kriptografi ve anahtar yönetimi modülleri (örn. AES-GCM, ChaCha20-Poly1305, ECDH/X25519)
  - protocols/ — Uplink/Downlink çerçeveleme, kimlik doğrulama, yeniden-iletim (ARQ), anti-replay koruması
  - sim/ — Kanal modelleri (AWGN, Rayleigh), link bütçesi taslağı, parazit/jamming ve paket kaybı senaryoları
- tests/ — Birim ve entegrasyon testleri (kriptografi, protokol, simülasyon)

## ⚡ Hızlı Başlangıç (Öneri)

1. docs klasöründe Fikir Ön Değerlendirme Raporu (FÖDR) taslağını açın.
2. src/sim içinde basit bir kanal simülatörü iskeleti oluşturun (AWGN + paket kaybı).
3. src/crypto içinde şifreleme için bir arayüz tanımlayın (AES-GCM veya ChaCha20-Poly1305) ve anahtar anlaşması için ECDH (X25519) planlayın.
4. src/protocols içinde çerçeve formatı, sıra numarası ve mesaj kimlik doğrulama (MAC) alanlarını belirleyin.
5. tests altında uçtan uca “şifrele → gönder → bozulmuş/bozulmamış kanaldan geçiş → doğrula” akışını test eden ilk testleri ekleyin.

## 🧭 Minimum Uygulanabilir Prototip (MVP)

- Uçtan uca şifreleme: AES-GCM veya ChaCha20-Poly1305 (AEAD).
- Anahtar anlaşması: ECDH (X25519) + ephemeral anahtarlar.
- Kimlik doğrulama: El sıkışmada dijital imza (Ed25519) veya ön-paylaşımlı kimlikler.
- Anti-replay: Sıra numarası + sliding window.
- Dayanıklılık: Temel yeniden-iletim (ARQ) ve basit hız uyarlaması; jamming test senaryoları sim/ altında.

## 🗺️ Yol Haritası (2–4 Hafta)

- Hafta 1: Protokol çerçevesi, sim/ AWGN modeli, temel test iskeleti.
- Hafta 2: AEAD şifreleme entegrasyonu, ECDH anahtar değişimi, anti-replay.
- Hafta 3: Jamming senaryoları, yeniden-iletim stratejileri, hata ayıklama logları.
- Hafta 4: Performans metrikleri (BER/PER, gecikme), rapor ve sunum taslakları.

Not: Bu klasör, öncelikle yazılım prototipi ve simülasyon akışına odaklanır; donanım entegrasyonu sonraki aşamalarda ele alınacaktır.

### 🔍 Yarışmanın amacı nedir?

* Bu yarışma, uydu haberleşme sistemlerinin **siber güvenliği** üzerine tasarlanmış. Yani “uydudan gelen / giden veriler”, “uydu terminalleri”, “haberleşme linkleri” gibi kritik alanlarda **güvenlik açıkları**na çözüm üretmeyi hedefliyor. ([Teknofest][1])
* Organizasyonun ifadesiyle: “küresel iletişim altyapısının temelini oluşturan uydu haberleşme sistemlerinin siber güvenliğini sağlamak amacıyla fikirler geliştirilmesi” amaçlanmış. ([Teknofest][2])
* Ayrıca özel vurgu yapılan alanlar: **afet anlarında**, **kırsal bölgelerde**, **stratejik iletişim alanlarında** uydu sistemlerinin önemi. Bu yüzden yarışma sadece teknolojik değil, toplumsal ve güvenlik boyutlu da. ([teknosayfa.com][3])

---

### 🧑‍🎓 Kimler katılabilir?

* Lise öğrencileri (Açık öğretim dahil) **ve** üniversite-önlisans, lisans, yüksek lisans, doktora ve açık öğretim öğrencileri. ([Teknofest][2])
* Takım üyeleri: Her kategori için **en fazla 10 kişilik** bir takım oluşturulabiliyor (danışman hariç). ([Teknofest][2])
* Yani senin yazılım öğrenme odaklı öğrencilik profilinle kesinlikle uygun bir kategori. Yazılım + siber güvenlik temaları senlik!

---

### 📅 Süreç & Ödüller

* Başvuru son tarihi: **30 Mayıs 2025** olarak belirlenmiş. ([Teknofest][2])
* Süreç adımları:

  1. Fikir Ön Değerlendirme Raporu (FÖDR)
  2. Fikir Detay Raporu (FDR) — Yarı-final aşaması
  3. Final Değerlendirme Raporu + Final Sunumu (özellikle üniversite ve üzeri kategori için teorik model geliştirme) ([Teknofest][2])
* Ödüller:

  * Lise kategorisi: 1.’ 80.000 TL, 2.’ 70.000 TL, 3.’ 60.000 TL ([Teknofest][2])
  * Üniversite ve üzeri kategori: 1.’ 100.000 TL, 2.’ 90.000 TL, 3.’ 80.000 TL ([Teknofest][2])

---

### 💡 Senin için ne fırsatlar var?

Sen yazılım mühendisliği öğrencisisin, yazılım + siber güvenlik + iletişim sistemleri gibi alanlara ilgin var → bu kategori tam senin sahnen:

* Yazılım kısmında: iletişim protokolleri, şifreleme algoritmaları, güvenli veri aktarımı, hatalı/zararlı haberleşme tespiti gibi modüller geliştirebilirsin.
* “Bilgisayarı vücudunun uzantısı hâline getirme” hedefin var ya — bu yarışma sana “gerçek dünya sistemi” ile çalışma imkânı sunar: uydu haberleşmesi gibi yüksek teknoloji alanında.
* Ayrıca belirttiğiniz gibi “enerji sistemleri, elektronik haberleşme mühendisliği” gibi yan dallarla da bağlantı kurabileceğin bir alan: yazılım + haberleşme + güvenlik.
* Takım kurabilirsin: sen yazılım tarafını, bir veya iki arkadaş elektronik/haberleşme/fizik kısmını üstlenebilir — böylece multidisipliner bir proje çıkar.

---

### 📌 Dikkat edilmesi gerekenler & taktikler

* Problem tanımı net olmalı: “Uydu haberleşmesinde güvenlik zafiyeti ne olabilir?” gibi sorular üzerine odaklan. Örneğin: sinyal müdahalesi, şifre kırma, uydudan gelen komutların doğruluğu, haberleşme linklerinin kesilmesi, sahte uydu terminalleri, veri sızıntısı vb.
* Uygulanabilir çözüm öner: Yarışma “uygulanabilir ve yenilikçi çözümler” istiyor. Yani sadece fikir değil, ölçeklenebilir, prototip olabilecek model ya da simülasyon önerisi büyük artı. ([Haberde.net][4])
* Teknik rapor/ sunum: Yazılım tarafını iyi planla; prototip veya demo varsa artı. Ayrıca raporda projenin “neden önemli?” kısmını — ulusal güvenlik, afet yönetimi vb. — vurgula.
* Takım çalışması ve disiplin: Buna dikkat et. Zaman yönetimi, görev dağılımı, yazılım modülleri, entegrasyon — bunlar yarışmalarda fark yaratır.
* Mentorluk/ kaynak kullanımı: Bu tür yarışmalarda genellikle destek, eğitim programı, bilgilendirme oturumları oluyor. Kullan. Yürütücüsü kurum ise ASELSAN. ([projekoord.firat.edu.tr][5])

---

### ✅ Özetle

“Güvenli Uydu Haberleşmesi” kategorisi, yazılım-öğrenci senin için hem teknoloji odaklı hem güvenlik odaklı hem de ekip çalışması/uygulama odaklı bir fırsat. Takım kur, fikir üret, yazılım ile haberleşme + güvenlik alanlarını birleştir — ve büyük ödül + deneyim kapısını açık tut.

---

[1]: https://www.teknofest.org/tr/content/announcement/uydu-haberlesmesinin-guvenligi-icin-genc-zihinler-teknofestte-yarisiyor/?utm_source=chatgpt.com "TEKNOFEST | AYAKLARI YERE BASMAYAN FESTİVAL"
[2]: https://www.teknofest.org/tr/yarismalar/guvenli-uydu-haberlesmesi-yarismasi/?utm_source=chatgpt.com "TEKNOFEST | AYAKLARI YERE BASMAYAN FESTİVAL"
[3]: https://teknosayfa.com/teknoloji/guvenli-uydu-haberlesmesi-yarismasi-teknofest-2025-kapsaminda-basliyor-%E2%8F%AC%F0%9F%91%87-h21896.html?utm_source=chatgpt.com "Güvenli Uydu Haberleşmesi Yarışması TEKNOFEST 2025 Kapsamında Başlıyor ⏬👇"
[4]: https://www.haberde.net/teknofest-2025-gencler-uydu-haberlesmesi-guvenligi-icin-yarisiyor-siber-tehditlere-karsi-yenilikci-cozumler-h38735.html?utm_source=chatgpt.com "TEKNOFEST 2025: Gençler Uydu Haberleşmesi Güvenliği İçin Yarışıyor! Siber Tehditlere Karşı Yenilikçi Çözümler | Haberde.Net"
[5]: https://projekoord.firat.edu.tr/announcements-detail/46278?utm_source=chatgpt.com "Uydu Haberleşmesinin Güvenliği İçin Genç Zihinler TEKNOFEST’te Yarışıyor! | Fırat Üniversitesi"
