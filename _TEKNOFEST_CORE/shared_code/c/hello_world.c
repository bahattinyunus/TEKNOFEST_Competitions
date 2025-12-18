/*
 * TEKNOFEST C Örneği - Hello World
 * Embedded sistemler ve düşük seviye programlama için
 */

#include <stdio.h>

int main() {
    printf("🚀 TEKNOFEST'e Hoş Geldiniz!\n");
    printf("C ile embedded sistemler ve performans kritik uygulamalar geliştirebilirsiniz.\n");
    
    // Basit hesaplama
    int takim_sayisi = 10;
    int yarisma_sayisi = 5;
    int toplam_katilim = takim_sayisi * yarisma_sayisi;
    
    printf("\n📊 İstatistikler:\n");
    printf("Takım Sayısı: %d\n", takim_sayisi);
    printf("Yarışma Sayısı: %d\n", yarisma_sayisi);
    printf("Toplam Katılım: %d\n", toplam_katilim);
    
    return 0;
}

