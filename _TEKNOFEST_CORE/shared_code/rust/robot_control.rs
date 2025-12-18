/*
 * TEKNOFEST Rust Robot Kontrol Örneği
 * Güvenli ve performanslı robot kontrol sistemi
 */

#[derive(Debug)]
enum Direction {
    Kuzey,
    Doğu,
    Güney,
    Batı,
}

struct Robot {
    name: String,
    x: i32,
    y: i32,
    direction: Direction,
}

impl Robot {
    fn new(name: String) -> Self {
        Robot {
            name,
            x: 0,
            y: 0,
            direction: Direction::Kuzey,
        }
    }
    
    fn move_forward(&mut self, distance: i32) {
        match self.direction {
            Direction::Kuzey => self.y += distance,
            Direction::Güney => self.y -= distance,
            Direction::Doğu => self.x += distance,
            Direction::Batı => self.x -= distance,
        }
        println!("{} {} birim ileri gitti. Konum: ({}, {})", 
                 self.name, distance, self.x, self.y);
    }
    
    fn turn_right(&mut self) {
        self.direction = match self.direction {
            Direction::Kuzey => Direction::Doğu,
            Direction::Doğu => Direction::Güney,
            Direction::Güney => Direction::Batı,
            Direction::Batı => Direction::Kuzey,
        };
        println!("{} sağa döndü. Yön: {:?}", self.name, self.direction);
    }
    
    fn get_position(&self) -> (i32, i32, &Direction) {
        (self.x, self.y, &self.direction)
    }
}

fn main() {
    println!("🤖 TEKNOFEST Robot Kontrol Sistemi\n");
    
    let mut robot = Robot::new("TEKNOFEST-Bot".to_string());
    
    robot.move_forward(3);
    robot.turn_right();
    robot.move_forward(2);
    robot.turn_right();
    robot.move_forward(1);
    
    println!("\n📍 Final Konum: {:?}", robot.get_position());
}

