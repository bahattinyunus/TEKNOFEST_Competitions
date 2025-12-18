Simülasyon Kurulumu (ROS/CARLA/Gazebo)

## Önkoşullar
- Ubuntu 22.04 önerilir (Windows için WSL2)
- Python 3.10+
- Diskte en az 20 GB boş alan

## ROS2 Kurulumu (Humble)
1) Kaynaklar ve anahtarlar ekleyin (Ubuntu için):
   https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html
2) Kurulum ve ortam değişkenleri:
   `sudo apt install ros-humble-desktop`
   `echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc`

## Gazebo (Fortress/Ignition)
- Kurulum: https://gazebosim.org/docs
- ROS2 entegrasyonu için `ros-gz` paketlerini ekleyin.

## CARLA Kurulumu
1) Bağımlılıklar: `sudo apt install clang cmake ninja-build` (detaylar için carla.org)
2) Release indirin veya kaynak koddan derleyin: https://carla.org/
3) Python API için `easy_install`/`pip` paketlerini ekleyin.

## Doğrulama
- RViz açın, sanal lidar/kamera yayınlarını görüntüleyin.
- CARLA’da örnek kasabayı (Town) açıp bir ego aracı sürdürün.

## İpuçları
- Düşük donanımda Gazebo daha hafif olabilir.
- Sensör gecikmelerini loglayın (rosbag) ve senaryolarda tekrar oynatın.

