from random import choice


print("Taş,Kağıt,Makas oyununa hoşgeldiniz")
print("Oyundan çıkmak için 'e' tuşuna basın")

x=["taş","kağıt","makas"]

sen=0
bilgisayar=0


while True:
    secim=input("Taş/Kağıt/Makas:  ")
    bil_secim=choice(x)

    if (secim=="taş"):
        if (bil_secim=="taş"):
            print("Berabere")
            print(f'Senin puanın: {sen}')
            print(f'Bilgisayarın puanı: {bilgisayar}')
        elif (bil_secim=="kağıt"):
            print("Kağıt taşı sarar ben kazandım :)")
            bilgisayar=bilgisayar + 1
            print(f'Senin puanın: {sen}')
            print(f'Bilgisayarın puanı: {bilgisayar}')
        elif (bil_secim=="makas"):
            print("Taş makası kırar sen kazandın :/") 
            sen=sen + 1
            print(f'Senin puanın: {sen}')
            print(f'Bilgisayarın puanı: {bilgisayar}')
    elif (secim=="kağıt"):
        if (bil_secim=="taş"):
            print("Kağıt taşı sarar sen kazandın :/")
            sen=sen + 1
            print(f'Senin puanın: {sen}')
            print(f'Bilgisayarın puanı: {bilgisayar}')
        elif (bil_secim=="kağıt"):
            print("Berabere")
            print(f'Senin puanın: {sen}')
            print(f'Bilgisayarın puanı: {bilgisayar}')
        elif (bil_secim=="makas"):
            print("Makas kağıdı keser ben kazandım :)")
            bilgisayar=bilgisayar + 1 
            print(f'Senin puanın: {sen}')
            print(f'Bilgisayarın puanı: {bilgisayar}')
    elif (secim=="makas"):
        if (bil_secim=="taş"):
            print("Taş makası kırar ben kazanıdm :)")
            bilgisayar=bilgisayar + 1
            print(f'Senin puanın: {sen}')
            print(f'Bilgisayarın puanı: {bilgisayar}')
        elif (bil_secim=="kağıt"):
            print("Makas kağıdı keser sen kazandın :/")
            sen=sen + 1
            print(f'Senin puanın: {sen}')
            print(f'Bilgisayarın puanı: {bilgisayar}')
        elif (bil_secim=="makas"):
            print("Berabere")
            print(f'Senin puanın: {sen}')
            print(f'Bilgisayarın puanı: {bilgisayar}')
    elif (secim=="e"):
        print(f'Senin puanın: {sen}')
        print(f'Bilgisayarın puanı: {bilgisayar}')
        print("Sistem kapatılıyor...")
        break
    else:
        print("Hatalı giriş yaptın tekrar dene")
