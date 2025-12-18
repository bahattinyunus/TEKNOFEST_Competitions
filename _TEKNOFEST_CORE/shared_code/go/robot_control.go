package main

/*
 * TEKNOFEST Go Robot Kontrol Örneği
 * Concurrent robot kontrol sistemi
 */

import "fmt"

type Direction int

const (
	Kuzey Direction = iota
	Doğu
	Güney
	Batı
)

type Robot struct {
	name      string
	x, y      int
	direction Direction
}

func NewRobot(name string) *Robot {
	return &Robot{
		name:      name,
		x:         0,
		y:         0,
		direction: Kuzey,
	}
}

func (r *Robot) MoveForward(distance int) {
	switch r.direction {
	case Kuzey:
		r.y += distance
	case Güney:
		r.y -= distance
	case Doğu:
		r.x += distance
	case Batı:
		r.x -= distance
	}
	fmt.Printf("%s %d birim ileri gitti. Konum: (%d, %d)\n", 
		r.name, distance, r.x, r.y)
}

func (r *Robot) TurnRight() {
	r.direction = (r.direction + 1) % 4
	directions := []string{"Kuzey", "Doğu", "Güney", "Batı"}
	fmt.Printf("%s sağa döndü. Yön: %s\n", r.name, directions[r.direction])
}

func (r *Robot) GetPosition() (int, int, Direction) {
	return r.x, r.y, r.direction
}

func main() {
	fmt.Println("🤖 TEKNOFEST Robot Kontrol Sistemi\n")
	
	robot := NewRobot("TEKNOFEST-Bot")
	
	robot.MoveForward(3)
	robot.TurnRight()
	robot.MoveForward(2)
	robot.TurnRight()
	robot.MoveForward(1)
	
	x, y, dir := robot.GetPosition()
	fmt.Printf("\n📍 Final Konum: (%d, %d) Yön: %d\n", x, y, dir)
}

