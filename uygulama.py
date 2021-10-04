import random
list=range(1,101)
sayı=random.choice(list)

print("Sayı Tahmin Uyagulaması")
print("Uygulamaya [Hoşgeldiniz],Bu uygulama da sayıyı tahmin  etmeye çalışacaksınız.Sayıyı istediğiniz kadar tahminle bulmaya çalışabilirsiziz.Ancak unutmayın ne kadar hızlı tahmin ederseniz o kadar çok puan kazanırsınız.Başarılar ")
nickname=input("İsminiz nedir: ")

a=int(input("Kaç tahmin hakkı kullanmak istersiniz: "))

hak=a
sayaç=0

while hak>0:
    hak -= 1
    sayaç += 1
    tahmin=int(input('Tahmininizi giriniz: '))

    if sayı == tahmin:
        print(f'Tebrikler {nickname} {sayaç}. defada bildiniz.Toplam puanınız: {100 - (100/a) * {sayaç -1}}')
        break
    elif sayı>tahmin:
        print("yukarı")

    else:
        print("aşağı") 

if hak == 0:
    print(f'Hakkınız bitti tahmin:{sayı}')
    print("Tekrar denemek için ekrana 'py uygulama.py' yazınız")        

