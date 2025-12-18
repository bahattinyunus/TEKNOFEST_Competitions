package main

/*
 * TEKNOFEST Go Örneği - Hello World
 * Concurrent ve scalable uygulamalar için
 */

import "fmt"

func main() {
	fmt.Println("🚀 TEKNOFEST'e Hoş Geldiniz!")
	fmt.Println("Go ile concurrent ve scalable sistemler geliştirebilirsiniz.")
	
	// Basit hesaplama
	takimSayisi := 10
	yarismaSayisi := 5
	toplamKatilim := takimSayisi * yarismaSayisi
	
	fmt.Println("\n📊 İstatistikler:")
	fmt.Printf("Takım Sayısı: %d\n", takimSayisi)
	fmt.Printf("Yarışma Sayısı: %d\n", yarismaSayisi)
	fmt.Printf("Toplam Katılım: %d\n", toplamKatilim)
}

