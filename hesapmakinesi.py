print("1.Toplama")
print("2.Çıkarma")
print("3.Çarpma")
print("4.Bölme")

islem=int(input("Yapmak istediğiniz işlemi giriniz(1/2/3/4): "))

sayi1=int(input("Birinci sayıyı giriniz: "))
sayi2=int(input("İkinci sayıyı giriniz: "))


if (islem==1):
    toplam=sayi1 + sayi2
    print(f'{sayi1} + {sayi2} = {toplam}')
elif (islem==2):
    fark=sayi1 - sayi2
    print(f'{sayi1} - {sayi2} = {fark}')
elif (islem==3):
    çarpım=sayi1 * sayi2
    print(f'{sayi1} * {sayi2} = {çarpım}')
elif (islem==4):
    bölme=sayi1 / sayi2
    print(f'{sayi1} / {sayi2} = {bölme}')   
