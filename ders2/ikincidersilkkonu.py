"""
a = True
print(a)
#tru
print(type(a))
#bool
print(1<0)
#false
print(0==0)
#true
b = None
print(b)
#none
print("AB'=2018"=="sad")
#false
print("e">"w")
#alfabetik sıralama için yapılabilir.

print(True < False)
#false döner

print(1>0 and "Murat"=="Murat")
#true
print(1>2 and "Murat"=="Murat")
#false
print(1>2 or "Murat"=="Murat")
#true
print(1>2 or "Murat"=="murat")
#false
print(not(1<2))
#false
print(not 0)
#true

a = 2
if(a ==2):
    print(a)
    #2 olur çıktısı çünkü koşul içerisinde bulunmaktadır.
print("asd")
#çıktıyı geçtik çünkü giridi de geçtik bu nun çıktısı ise direkt asd olur.

if(a ==2):
    pass
#if boş kalmasın diye pass kullanılır break kullanılmaz .




yas = int(input("lütfen yaşınızı giriniz"))
if(yas>17):
    print("a")
elif(yas>12):
    print("b")
else:
    print("c")
"""
"""
kadi = input("lütfen kıllanıcı adınızı giriniz:")
parola = input("lütfen parolanızı giriniz.")
k = "ab2018"
p = "12345"
if(kadi ==k and parola ==p ):
    print("giriş yapıldı")
else:
    print("giriş başarısız")


"""
"""
a = int(input("sayi:"))
b= int(input("ikincisayi:"))
c = input("hangi işlem(toplama,cikarma,bolme,carpma):")
if(c=="toplama"):
    d=a+b
    print("'{}' bu sayı ile {} bu sayının {}işleminin sonucu {}".format(a,b,c,d))
elif(c=="cikarma"):
    d=a-b
    print("'{}' bu sayı ile {} bu sayının {}işleminin sonucu {}".format(a, b, c, d))
elif(c=="carpma"):
    d=a*b
    print("'{}' bu sayı ile {} bu sayının {}işleminin sonucu {}".format(a, b, c, d))
elif(c=="bolme"):
    d=a/b
    print("'{}' bu sayı ile {} bu sayının {}işleminin sonucu {}".format(a, b, c, d))
else:
    print("boyle bir islem bulunmamaktadir")





liste = [1,2,3,4,5,6,7]

for elaman in liste:
    print("Elaman",elaman,sep="-")


liste = [1,2,3,4,5,6,7]
toplam = 0
for elaman in liste:
    toplam+=elaman
    print("{} toplam: {}".format(elaman, toplam))

for elaman in range(0,20):
    toplam+=elaman
    print("{} toplam: {}".format(elaman, toplam))
"""

"""
liste = [1,2,3,4,5,6,7,8,9]
for elaman in liste:
    if elaman % 2 ==0:
        print(elaman)

isim = "yunus emre"
for harf in isim:
    print(harf*3)

"""
"""
liste = [(1,2),(3,4),(5,6),(7,8)]
for dön in liste:
    print(dön)

for (i,j) in liste:
    print(i,j,sep="\n")
"""
"""

#aşağıdakini dersten hariç isimlerin baş harfine göre çektim
liste2 = ["yunus","yusuf","hakan","hayat"]
for isim in liste2:
    for harf in isim[0]:
        if(harf=="y"):
            print(isim)
#buraya kadar yaptım
"""


"""
if "a" in "sigara":
    print("asd")
b = "sigara"
print(b.count("a"))
#kaç adet a olduğunu saydırdım

"""
"""
i =0
while (i<10):
    if i % 2 != 0:
        print("i 2 ye bölünemez")
        i += 1
        continue
    print("i nin değeri", i)
    i +=1
    if i ==6:
        break
        """




