/**
 * TEKNOFEST Java Robot Kontrol Örneği
 * OOP ile robot kontrol sistemi
 */

public class RobotControl {
    
    static class Robot {
        private String name;
        private int x, y;
        private String direction;
        
        public Robot(String name) {
            this.name = name;
            this.x = 0;
            this.y = 0;
            this.direction = "Kuzey";
        }
        
        public void moveForward(int distance) {
            switch (direction) {
                case "Kuzey": y += distance; break;
                case "Güney": y -= distance; break;
                case "Doğu": x += distance; break;
                case "Batı": x -= distance; break;
            }
            System.out.println(name + " " + distance + " birim ileri gitti. Konum: (" + x + ", " + y + ")");
        }
        
        public void turnRight() {
            String[] directions = {"Kuzey", "Doğu", "Güney", "Batı"};
            int current = 0;
            for (int i = 0; i < directions.length; i++) {
                if (directions[i].equals(direction)) {
                    current = i;
                    break;
                }
            }
            direction = directions[(current + 1) % 4];
            System.out.println(name + " sağa döndü. Yön: " + direction);
        }
        
        public void printPosition() {
            System.out.println("📍 Konum: (" + x + ", " + y + ") Yön: " + direction);
        }
    }
    
    public static void main(String[] args) {
        System.out.println("🤖 TEKNOFEST Robot Kontrol Sistemi\n");
        
        Robot robot = new Robot("TEKNOFEST-Bot");
        
        robot.moveForward(3);
        robot.turnRight();
        robot.moveForward(2);
        robot.turnRight();
        robot.moveForward(1);
        
        System.out.println();
        robot.printPosition();
    }
}

