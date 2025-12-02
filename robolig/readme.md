
# 🦾 Teknofest **RoboLig** – Proje README

Aşağıdaki metin copy-paste yapılınca GitHub’da tam uyumlu görünür.

---

# 🦾 Teknofest RoboLig – Otonom Robot Projesi

![banner](https://upload.wikimedia.org/wikipedia/commons/5/53/Teknofest_logo.png)

<div align="center">

[![Status](https://img.shields.io/badge/Status-In%20Development-blue)]()
[![Platform](https://img.shields.io/badge/Platform-Embedded%20Systems-red)]()
[![Category](https://img.shields.io/badge/Category-RoboLig-yellow)]()
[![License](https://img.shields.io/badge/License-MIT-green)]()

</div>

---

## 🔥 Proje Özeti

Bu proje, Teknofest **RoboLig** kategorisinde yarışmak üzere geliştirilen tam otonom bir mobil robot içerir.
Robot; sensör verilerini gerçek zamanlı işleyen, engellerden kaçınan, hedefleri algılayan ve görevleri stratejik şekilde tamamlayan bir yapıya sahiptir.

> **Kısaca:** “Sahaya bir bırakıyoruz, görevleri tokatlar.”

---

## 📌 İçindekiler

* [Kategori Hakkında](#kategori-hakkında)
* [Robot Tasarımı](#robot-tasarımı)
* [Elektronik Yapı](#elektronik-yapı)
* [Yazılım Mimarisi](#yazılım-mimarisi)
* [Görevler ve Saha](#görevler-ve-saha)
* [Kurulum](#kurulum)
* [Takım](#takım)
* [Lisans](#lisans)

---

## 🧭 Kategori Hakkında

**RoboLig**, otonom robotların zaman, doğruluk ve stabilite odaklı görevleri yerine getirdiği rekabetçi bir kategoridir.

Robotlardan beklenenler:

* Çizgiyi takip etmek
* Engellerden kaçmak
* Renk/nesne tespiti yapmak
* Hedefe konumlanmak
* Görevleri zaman kaybetmeden tamamlamak

---

## 🦿 Robot Tasarımı

### ⚙️ Mekanik Bileşenler

* 3D yazıcıdan üretilmiş kompakt şasi
* 2 veya 4 tekerlekli diferansiyel sürüş sistemi
* Modüler sensör yerleşimi
* Ağırlık merkezi optimizasyonu

### 📐 Boyut ve Limitler

* **Boyut:** Teknik şartnameye göre 20–40 cm arası
* **Ağırlık:** 1–4 kg arası
* **Enerji:** Li-Po / Li-ion pil

---

## 🔌 Elektronik Yapı

| Bileşen                   | Görev                                     |
| ------------------------- | ----------------------------------------- |
| **Mikrodenetleyici**      | Arduino / STM32 / Raspberry Pi            |
| **Motor Sürücü**          | L298N / TB6612FNG                         |
| **Sensörler**             | Çizgi, ToF, ultrasonik, IMU, renk sensörü |
| **Görüntü İşleme (Ops.)** | Raspberry Pi + OpenCV                     |
| **Güç Dağıtımı**          | 2S/3S Li-Po + voltaj regülatörleri        |

Kablolama düzeni, yarışma güvenlik kurallarına %100 uyumludur.

---

## 🧠 Yazılım Mimarisi

### Genel Yapı

```
/src
  ├── sensors/
  ├── motor_control/
  ├── navigation/
  ├── pid/
  ├── strategy/
  └── main.cpp
```

### Yapay Zeka & Kontrol

* PID ile hassas çizgi takip
* Durum makinesi (FSM) ile görev geçişleri
* Sensör füzyonu
* Engel kaçınma algoritması
* Renk/çağrı işareti algılama
* (Ops.) OpenCV tabanlı görüntü işleme

---

## 🏟️ Görevler ve Saha

Saha içerisinde robotun tamamlaması gereken tipik görevler:

* ⚫ **Çizgi Takip:** Zemin üzerindeki yolu takip eder
* 🟢 **Renk Algılama:** Belirli hedef renkleri bulur
* 🟦 **Nesne Bırak/Topla:** Belirli bölgelerde görev tamamlar
* 🟥 **Engel Kaçma:** Engellerden otonom şekilde uzaklaşır
* 🟡 **Hedefe Konumlanma:** Son bölgeye hızlı ve doğru varır

> Not: Görevler Teknofest tarafından her yıl güncellenebilir.

---

## 🛠️ Kurulum

### 🔧 Gerekli Yazılımlar

* Arduino IDE / STM32CubeIDE / PlatformIO
* Python 3 (OpenCV kullanılıyorsa)
* Git

### 📥 Projeyi İndir

```bash
git clone https://github.com/kullaniciadi/robolig-robot.git
cd robolig-robot
```

### ⚙️ Derleme ve Yükleme

Arduino için:

```bash
arduino-cli compile --fqbn arduino:avr:uno ./src
arduino-cli upload -p /dev/ttyUSB0 --fqbn arduino:avr:uno
```

---

## 👥 Takım

| Rol           | Kişi |
| ------------- | ---- |
| Takım Lideri  | …    |
| Yazılım       | …    |
| Mekanik       | …    |
| Elektronik    | …    |
| Strateji      | …    |
| Dokümantasyon | …    |

---

## 📜 Lisans

Bu proje **MIT License** ile lisanslanmıştır.

---

## ⭐ Katkıda Bulunun

Projeye katkı yapmak isterseniz PR gönderebilirsiniz — open source bizde yaşam tarzı 😎

