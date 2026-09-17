def hesap_makinesi():
    print("---deneme hesap makinesi---")
    print("İşlemler: + (Toplama), - (Çıkarma), * (Çarpma), / (Bölme)")
    print("Çıkış yapmak için 'q' tuşuna basabilirsiniz.")

    while True:
        islem = input("\nYapmak istediğiniz işlemi seçin (+, -, *, /): ")

        if islem.lower() == 'q':
            print("Hesap makinesi kapatılıyor. İyi çalışmalar!")
            break

        if islem in ('+', '-', '*', '/'):
            try:
                sayi1 = float(input("Birinci sayıyı girin: "))
                sayi2 = float(input("İkinci sayıyı girin: "))
            except ValueError:
                print("Hata: Lütfen geçerli bir sayı girin!")
                continue

            if islem == '+':
                sonuc = sayi1 + sayi2
                print(f"Sonuç: {sayi1} + {sayi2} = {sonuc}")
            elif islem == '-':
                sonuc = sayi1 - sayi2
                print(f"Sonuç: {sayi1} - {sayi2} = {sonuc}")
            elif islem == '*':
                sonuc = sayi1 * sayi2
                print(f"Sonuç: {sayi1} * {sayi2} = {sonuc}")
            elif islem == '/':
                if sayi2 == 0:
                    print("Hata: Bir sayı sıfıra bölünemez!")
                else:
                    sonuc = sayi1 / sayi2
                    print(f"Sonuç: {sayi1} / {sayi2} = {sonuc}")
        else:
            print("Geçersiz işlem! Lütfen +, -, *, / veya q tuşlayın.")

if __name__ == "__main__":
    hesap_makinesi()