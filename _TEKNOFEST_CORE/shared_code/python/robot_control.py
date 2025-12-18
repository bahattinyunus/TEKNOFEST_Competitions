#!/usr/bin/env python3
"""
TEKNOFEST Robot Kontrol Örneği
Basit bir robot kontrol sistemi simülasyonu
"""

class Robot:
    """Basit bir robot sınıfı"""
    
    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.direction = "Kuzey"
    
    def move_forward(self, distance=1):
        """Robotu ileri hareket ettir"""
        if self.direction == "Kuzey":
            self.y += distance
        elif self.direction == "Güney":
            self.y -= distance
        elif self.direction == "Doğu":
            self.x += distance
        elif self.direction == "Batı":
            self.x -= distance
        print(f"{self.name} {distance} birim ileri gitti. Konum: ({self.x}, {self.y})")
    
    def turn_right(self):
        """Sağa dön"""
        directions = ["Kuzey", "Doğu", "Güney", "Batı"]
        current_index = directions.index(self.direction)
        self.direction = directions[(current_index + 1) % 4]
        print(f"{self.name} sağa döndü. Yön: {self.direction}")
    
    def get_position(self):
        """Mevcut konumu döndür"""
        return (self.x, self.y, self.direction)

def main():
    """Ana fonksiyon"""
    print("🤖 TEKNOFEST Robot Kontrol Sistemi\n")
    
    # Robot oluştur
    robot = Robot("TEKNOFEST-Bot")
    
    # Hareket komutları
    robot.move_forward(3)
    robot.turn_right()
    robot.move_forward(2)
    robot.turn_right()
    robot.move_forward(1)
    
    # Final konum
    print(f"\n📍 Final Konum: {robot.get_position()}")

if __name__ == "__main__":
    main()

