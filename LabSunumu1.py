from colorama import Fore, Style, init

init(autoreset=True)

def print_menu():
    print(Fore.LIGHTRED_EX + "1. Seçenek - Listenin en küçük n. elemanını bulma")
    print(Fore.LIGHTWHITE_EX + "2. Seçenek - En Yakın Çifti Bulma")
    print(Fore.LIGHTRED_EX + "3. Seçenek - Bir Listenin Tekrar Eden Elemanlarını Bulma")
    print(Fore.LIGHTWHITE_EX + "4. Seçenek - Matris Çarpanı Bulma")
    print(Fore.LIGHTYELLOW_EX + "5. Seçenek - Bir Text Dosyasındaki Kelimelerin Frekansını Bulma")
    print(Fore.LIGHTBLUE_EX + "6. Seçenek - Liste İçinde En Küçük Değeri Bulma")
    print(Fore.LIGHTGREEN_EX + "7. Seçenek - Karekök Fonksiyonu")
    print(Fore.LIGHTMAGENTA_EX + "8. Seçenek - En Büyük Ortak Bölen")
    print(Fore.LIGHTYELLOW_EX + "9. Seçenek - Asallık")
    print(Fore.LIGHTCYAN_EX + "10. Seçenek - Daha Hızlı Fibonacci Hesabı")
    print(Fore.LIGHTMAGENTA_EX + "11. Çıkış")
    print(Style.RESET_ALL)

def main():
    while True:
        print_menu()
        try:
            secim = int(input("Lütfen bir seçenek girin (1-11): "))
            if secim == 1:
                def k_kucuk(k, liste):
                    if k > 0 and k <= len(liste):
                        liste.sort()
                        return liste[k - 1]
                    else:
                        return None

                liste = [7, 10, 4, 3, 20, 15]
                k_degeri = 1

                sonuc = k_kucuk(k_degeri, liste)

                if sonuc is not None:
                    print(f"Listenin {k_degeri}. en küçük elemanı: {sonuc}")
                else:
                    print("Geçersiz k değeri.")

            elif secim == 2:
                def en_yakin_cift(hedef, liste):
                    liste.sort()
                    en_kucuk_fark = None
                    en_yakin_cift = None

                    for i in range(len(liste) - 1):
                        for j in range(i + 1, len(liste)):
                            toplam = liste[i] + liste[j]
                            fark = abs(hedef - toplam)

                            if en_kucuk_fark is None or fark < en_kucuk_fark:
                                en_kucuk_fark = fark
                                en_yakin_cift = (liste[i], liste[j])

                    return en_yakin_cift


                hedef_sayi = 54
                liste = [10, 22, 28, 29, 30, 40]
                print(en_yakin_cift(hedef_sayi, liste))
            elif secim == 3:

                def tekrar_eden_elemanlar(liste):
                    tekrar_edenler = [a for a in liste if liste.count(a) > 1]
                    sonuc = list(set(tekrar_edenler))

                    return sonuc

                liste = [1, 2, 3, 2, 1, 5, 6, 5, 5, 5]
                sonuc = tekrar_eden_elemanlar(liste)
                print(sonuc)
            elif secim == 4:
                def matris_carpimi(A, B):

                    sonuc = [[sum(a * b for a, b in zip(A_satir, B_sutun)) for B_sutun in zip(*B)] for A_satir in A]
                    return sonuc

                A = [[1, 2, 3], [4, 5, 6]]
                B = [[7, 8], [9, 10], [11, 12]]

                sonuc = matris_carpimi(A, B)
                print("Matris: ")
                for i in sonuc:
                    print(i)
                print()
                no = [23, 56, 87, 47, 12, 36, 45, 47]
                isim = ["Ahmet", "Mehmet", "Ayşe", "Zeynep", "Elif", "Kemal", "Fatma", "Can"]
                zip1 = zip(no, isim)
                print(list(zip1))
            elif secim == 5:
                from collections import Counter

                def kelime_frekans(dosyanin_yeri):
                    try:
                        with open(dosyanin_yeri, 'r') as dosya:
                            kelimeler = dosya.read()
                            kelimeler = kelimeler.split()

                            kelime_frekans_sonuc = Counter(kelimeler)
                            return kelime_frekans_sonuc

                    except FileNotFoundError:
                        return "Dosya bulunamadı."

                dosyanin_yeri = r"C:\Users\user\Desktop\giris_metni.txt"
                frekans = kelime_frekans(dosyanin_yeri)

                if isinstance(frekans, str):
                    print(frekans)
                else:
                    for kelime, sayi in frekans.items():
                        print(f"{kelime}={sayi}")
            elif secim == 6:
                def en_kucuk_deger(liste):

                    if len(liste) == 0:
                        return None

                    if len(liste) == 1:
                        return liste[0]

                    kucuk_deger = en_kucuk_deger(liste[1:])

                    if liste[0] < kucuk_deger:
                        return liste[0]
                    else:
                        return kucuk_deger

                liste1 = [1, 4, 6, 91, 2, 5]
                print(en_kucuk_deger(liste1))

                liste2 = [1, 2, 3, -1, 4, -2, 5]
                print(en_kucuk_deger(liste2))
            elif secim == 7:
                def karekok(N, x0, tol=1e-10, maxiter=10):
                    for i in range(maxiter):
                        x1 = 0.5 * (x0 + N / x0)
                        hata = abs(x1 ** 2 - N)

                        if hata < tol:
                            return x1

                        x0 = x1

                    print(f"{maxiter} iterasyonda sonuca ulaşılamadı. 'hata' veya 'maxiter' değerlerini değiştirin.")
                    return x1

                print(karekok(N=10, x0=1))
                print(karekok(N=10000, x0=0.1))
                print(karekok(N=10000, x0=0.1, maxiter=15))

            elif secim == 8:
                def eb_ortak_bolen(k, l):
                    if l == 0:
                        return k
                    return eb_ortak_bolen(l, k % l)

                print(eb_ortak_bolen(18, 64))
                print(eb_ortak_bolen(32, 64))

            elif secim == 9:
                def asal_veya_degil(sayi, bolen1=2):
                    if sayi <= 1:
                        return False
                    if bolen1 > int(sayi ** 0.5):
                        return True
                    if sayi % bolen1 == 0:
                        return False
                    return asal_veya_degil(sayi, bolen1 + 1)

                print(asal_veya_degil(35))
                print(asal_veya_degil(97))

            elif secim == 10:
                def hizlandirici(n, k, fibk, fibk1):
                    if k == n:
                        return fibk
                    else:
                        return hizlandirici(n, k + 1, fibk + fibk1, fibk)

                n = 8
                sonuc = hizlandirici(n, 1, 1, 0)
                print(f"Fibonacci({n}) = {sonuc}")

            elif secim == 11:
                print(Fore.RED + "Çıkış yapılıyor. Teşekkürler...")
                break
            else:
                print(Fore.RED + "Böyle bir seçenek yok. Lütfen tekrar girin.")
        except ValueError:
            print(Fore.RED + "Geçersiz giriş. Lütfen bir sayı girin.")

if __name__ == "__main__":
    main()
