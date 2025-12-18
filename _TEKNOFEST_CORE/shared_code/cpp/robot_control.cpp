/*
 * TEKNOFEST C++ Robot Kontrol Örneği
 * OOP kullanarak robot kontrol sistemi
 */

#include <iostream>
#include <string>

class Robot {
private:
    std::string name;
    int x, y;
    std::string direction;
    
public:
    Robot(const std::string& robotName) : name(robotName), x(0), y(0), direction("Kuzey") {}
    
    void moveForward(int distance = 1) {
        if (direction == "Kuzey") y += distance;
        else if (direction == "Güney") y -= distance;
        else if (direction == "Doğu") x += distance;
        else if (direction == "Batı") x -= distance;
        
        std::cout << name << " " << distance << " birim ileri gitti. Konum: (" 
                  << x << ", " << y << ")" << std::endl;
    }
    
    void turnRight() {
        std::string directions[] = {"Kuzey", "Doğu", "Güney", "Batı"};
        int current = 0;
        for (int i = 0; i < 4; i++) {
            if (directions[i] == direction) {
                current = i;
                break;
            }
        }
        direction = directions[(current + 1) % 4];
        std::cout << name << " sağa döndü. Yön: " << direction << std::endl;
    }
    
    void printPosition() {
        std::cout << "📍 Konum: (" << x << ", " << y << ") Yön: " << direction << std::endl;
    }
};

int main() {
    std::cout << "🤖 TEKNOFEST Robot Kontrol Sistemi\n" << std::endl;
    
    Robot robot("TEKNOFEST-Bot");
    
    robot.moveForward(3);
    robot.turnRight();
    robot.moveForward(2);
    robot.turnRight();
    robot.moveForward(1);
    
    std::cout << "\n";
    robot.printPosition();
    
    return 0;
}

