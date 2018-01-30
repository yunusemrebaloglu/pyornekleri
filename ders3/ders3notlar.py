"""
i = 20
while (i < 20):
     print("sdf")
     i += 1
     print(i)
     while (True):
        giris = input("devam edekmi :")
        if giris =="E":
            break
"""

"""
for b in range(0,10):
    for c in range(0,10):
        print(" {} x {} = {}".format(b,c,b*c))
"""
"""
for b in range(0,100):
    if b%3==0:
        print(b)
"""
"""
a = int(input("birsayıgiriniz:"))
b = []
for c in range(1, a):

    if a % c == 0:
        b.append(c)
if sum(b)==a:
    print("mükemmel sayıdır {} ".format(a))
else:
    print("mükemmel değil{}".format(a))
"""


"""
b=[]
while True:
    a = input("sayi giriniz: çıkmak için ise q ya basın")
    if a == "q":
        print(sum(b))
        break
    b.append(int(a))
"""
"""
b=[]
a = input("lütfen sayınızı girin:")
for s in a:
    b.append(int(s)**int(len(a)))
if sum(b)== int(a):
    print("işte bu")
else:
    print("malesef")
print(b)
"""
"""
def selamla(isim="",soyisim=""):
    print("selam{} {}".format(isim,soyisim))

selamla(89)

"""
"""


def sirala(a,b):
    if a>b:
        return a,b
    else:
        return b,a

print(sirala(12,11))

sonuc= sirala(5,12)

print(type(sonuc))
print(sonuc)
buyuk,kucuk= sirala(2,12)
print(buyuk,kucuk)
print(buyuk)
print(kucuk)

"""
"""
a = input("sayıyıgirin:")
def mukemmel(a):

        b = []
        for s in a:
            b.append(int(s)**int(len(a)))
        if sum(b)== int(a):
            return 1
        return 0

if mukemmel(a):
    print("Mukemmel")
else:
    print("değil")

"""


"""
def mukemmel():
    for a in range(0,1000):
        b = []
        for c in range(1, a):
            if a % c == 0:
                b.append(c)
        if sum(b)==a:
             print("mükemmel sayıdır {} ".format(a))

mukemmel()
"""
"""
a= int(input("birinci:"))
b = int(input("ikinci"))
def ebob(a,b):
    if a<b:
        kucuk = a
        buyuk =b
        kuc =a
    else:
        kucuk = b
        buyuk =a
        kuc = b
    while True:
        if buyuk % kucuk ==0 and kuc % kucuk ==0 :
            return kucuk
        kucuk =kucuk -1
print(ebob(a,b))


"""

a= int(input("birinci:"))
b = int(input("ikinci"))
def ekok(a,b):
    c=1
    d=1

ekok(a,b)

"""
from math import sqrt

def pisagor():
    n = 0
    for a in range(1,101):
        for b in range(1,101):
            d =sqrt(a**2+b**2)
            k =[]
            k.append(int(d))
            if d in k:

                n +=1
                print("{} ile {} kenarının karşısı {}".format(a,b,d))
    print(n)

pisagor()
"""
"""
a = input("lütfen sıfır ile 100 arasında sayı giriniz")
def sozluk(a):
    soz1 = [("1","bir"),("2","iki"),("3","üç"),("4","dört"),("5","beş"),("6","altı"),("7","yedi"),("8","sekiz"),("9","dokuz")]
    soz2 = [("1", "on"), ("2", "yirmi"), ("3", "otuz"), ("4", "kırk"), ("5", "elli"), ("6", "altmış"), ("7", "yetmiş"),("8", "seksen"), ("9", "doksan")]
    if a =="0" :
        print("sıfır")
    elif a =="100":
        print("yüz")
    else:
        if len(a) == 1:
            print( soz1[int(a)-1][1])
        elif len(a)==2:
            print(soz2[int(a[0])-1][1],soz1[int(a[1])-1][1],sep="")
sozluk(a)
"""
