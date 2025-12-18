/**
 * TEKNOFEST JavaScript Robot Kontrol Örneği
 * Web tabanlı robot simülasyonu
 */

class Robot {
    constructor(name) {
        this.name = name;
        this.x = 0;
        this.y = 0;
        this.direction = "Kuzey";
    }
    
    moveForward(distance = 1) {
        const directions = {
            "Kuzey": () => this.y += distance,
            "Güney": () => this.y -= distance,
            "Doğu": () => this.x += distance,
            "Batı": () => this.x -= distance
        };
        
        directions[this.direction]();
        console.log(`${this.name} ${distance} birim ileri gitti. Konum: (${this.x}, ${this.y})`);
    }
    
    turnRight() {
        const directions = ["Kuzey", "Doğu", "Güney", "Batı"];
        const currentIndex = directions.indexOf(this.direction);
        this.direction = directions[(currentIndex + 1) % 4];
        console.log(`${this.name} sağa döndü. Yön: ${this.direction}`);
    }
    
    getPosition() {
        return { x: this.x, y: this.y, direction: this.direction };
    }
}

// Ana fonksiyon
function main() {
    console.log("🤖 TEKNOFEST Robot Kontrol Sistemi\n");
    
    const robot = new Robot("TEKNOFEST-Bot");
    
    robot.moveForward(3);
    robot.turnRight();
    robot.moveForward(2);
    robot.turnRight();
    robot.moveForward(1);
    
    console.log(`\n📍 Final Konum:`, robot.getPosition());
}

main();

