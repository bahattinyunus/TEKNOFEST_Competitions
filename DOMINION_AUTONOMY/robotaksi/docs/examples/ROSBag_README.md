Örnek: rosbag Kullanımı ve Log Yapısı

## Klasör Yapısı
```
docs/
  examples/
    logs/
      2025-08-10_run01/
        sensors.bag
        notes.md
```

## Kayıt Alma
```bash
ros2 bag record -o sensors /camera/image_raw /lidar/points /imu/data
```

## Tekrar Oynatma
```bash
ros2 bag play sensors
```

## Analiz İpuçları
- Zaman damgalarını hizalayın (TF, IMU drift kontrolü)
- Gecikme > 100ms ise perception/pipeline ayarlarını gözden geçirin
- Kötü hava/ışık senaryoları içeren kayıtlar saklanmalı
