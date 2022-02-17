import math



print("Çevre/Alan/Hacim")
islem=str(input("Yapmak istediğiniz işlemi giriniz: "))


pi=3


def cevre(sekil1):
    
    if (sekil1==1):
        a=int(input("Karenin bir kenarının uzunluğunu giriniz: "))
        print("Karenin çevresi=")
        print(4*a)
    elif (sekil1==2):
        r=int(input("Çemberin yarıçapını giriniz: "))
        print("Çemberin çevresi=")
        print(2*pi*r)
    elif (sekil1==3):
        print("Üçgenin kenarlarını giriniz")
        a=int(input())
        b=int(input())
        c=int(input())
        print("Üçgenin çevresi=")
        print(a+b+c)     
    elif(sekil1==4):
        a=int(input("Kısa kenarı giriniz: "))
        b=int(input("Uzun kenarı giriniz: "))
        print("Dikdörgenin çevresi=")
        print(2*a + 2*b)
    elif (sekil1==5):  
        print("Kenarları giriniz")
        a=int(input())  
        b=int(input())  
        print("Parelelkenarın çevresi=")
        print(2*a + 2*b)
    elif (sekil1==6):
        print("Çevreyi hesaplarken orta tabanı kullanacak mısınız?(Evet=E / Hayır=H)")
        karar=input("E/H: ")
        if (karar=="e" or "E"):
            o=int(input("Orta taban uzunluğunu giriniz: "))
            print("üst taban ve kenar uzunluğunu giriniz:")
            c=int(input())
            d=int(input())
            print("Yamuğun çevresi: ")
            print(2*o + c + d) 
        elif(karar=="h" or "H"):
            print("Yamuğun 4 kenar uzunluğunu giriniz: ")
            a=int(input())
            b=int(input())
            c=int(input())
            d=int(input())
            print("Yamuğun çevresi: ")
            print(a + b + c + d)    
        else:
            print("Hatalı giriş tekrar deneyin")



def alan(sekil2):
    if (sekil2==1):
        print("Karenin bir kenarını giriniz: ")
        a=int(input())
        print("Karenin alanı: ")
        print(math.pow(a,2))
    elif(sekil2==2):
        print("Çemberin yarıçapını giriniz: ")
        r=int(input())
        print("Çemberin alanı: ")
        print(pi*math.pow(r,2))    
    elif (sekil2==3):
        print("Üçgenin yüksekliğini giriniz: ")
        h=int(input())
        b=int(input("Taban uzunluğunu giriniz: "))
        print("Üçgenin alanı: ")
        print(1/2 * b * h)
    elif (sekil2==4):
        print("Dİkdörgenin kısa ve uzun kenarını giriniz: ")
        a=int(input())
        b=int(input())
        print("Dikdörtgenin alanı: ")
        print(a * b)
    elif (sekil2==5):
        b=int(input("Uzun kenarı giriniz: "))
        h=int(input("Yüksekliği giriniz: "))
        print("Paralelkenarın alanı: ")
        print(b*h)
    elif (sekil2==6):
        ust=int(input("Yamuğun üst taban uzunluğunu giriniz: "))
        alt=int(input("Alt taban uzunluğunu giriniz: "))
        h=int(input("Yüksekliği giriniz: "))
        print("Yamuğun alanı: ")
        print((1/2)* h *(ust +alt))
    

                
    
def hacim(sekil3):
    if (sekil3==1):
        a=int(input("Küpün bir kenar uzunluğunu giriniz: "))
        print("Küpün hacmi= ")
        print(math.pow(a,3))
    elif (sekil3==2):
        r=int(input("Kürenin yarıçapını giriniz: "))
        print("Kürenin hacmi: ")
        print((4/3) * pi * math.pow(r,3)) 
    elif (sekil3==3):
        print("Dikdörgenler prizmasının üç kenar uzunluğunu giriniz: ")
        a=int(input())
        b=int(input())
        c=int(input())
        print("Dİkdörtgenler prizmasının hacmi: ")
        print(a * b * c)
    elif (sekil3==4):
        r=int(input("Koninin yarıçağınnı giriniz: "))
        h=int(input("Koninin yüksekliğini  giriniz: "))
        print("Dik koninin hacmi= ")
        print((1/3) * pi * math.pow(r,2) * h)
    elif (sekil3==5):
        r=int(input("Silindirin  yarıçağınnı giriniz: "))
        h=int(input("Silindirin yüksekliğini  giriniz: "))
        print("Silindirin hacmi= ")
        print(pi * h * math.pow(r,2))




if islem=="Çevre" or "çevre":
    print("1- Kare"+'\n'+"2- Çember"+'\n'+"3- Üçgen"+'\n'+"4- Dikdörtgen"+'\n'+"5- Parelelkenar"+'\n'+"6- Yamuk")
    sekil1=int(input("Çevresini hesaplamak istediğiniz şeklin sıra sayısını giriniz:  "))
    cevre(sekil1)
elif islem=="Alan" or "alan":
    print("1- Kare"+'\n'+"2- Küre"+'\n'+"3- Üçgen"+'\n'+"4- Dikdörtgen"+'\n'+"5- Parelelkenar"+'\n'+"6- Yamuk")
    sekil2=int(input("Alanını hesaplamak istediğiniz şekli giriniz:  "))
    alan(sekil2)
elif islem=="Hacim" or "hacim":
   print("1- Küp"+'\n'+"2- Çember"+'\n'+"3- Dikdörgenler Prizması"+'\n'+"4- Dik Koni"+'\n'+"5- Silindir")
   sekil3=int(input("Hacimini hesaplamak istediğiniz şekli giriniz:  "))
   hacim(sekil3)
else:
    print("Hatalı işlem adı girdiniz lütfen tekrar deneyin")   
    