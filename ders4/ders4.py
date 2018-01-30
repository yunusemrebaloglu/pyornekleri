"""
try:
    a = int("213ad")
except:
    print("hata var")
print("son")
"""
"""
try:
    a = int("213ad")
except ValueError:
    print("hata var")
print("son")
"""
"""
try :
    print(20/0)
except ValueError:
    print("boş bırakma")
except ZeroDivisionError:
    print("sıfıra bölünmez")
"""
"""
try :
    print(20/0)
except (ZeroDivisionError,ValueError):
    print("sıfıra bölünmez")
"""
"""
try:
    a = int(input("biri:"))
    b = int(input("iki"))
    print(a/b)
except (ValueError,ZeroDivisionError):
    print("veriyi sıfır haricinde girin")
finally:
    print("mutluson")
"""
"""
def terscevir(s):
    if (type(s)!=str):
        raise ValueError("lürfen doğru değer girin")
    else:
        return s[::-1]

print(terscevir("Yunus Emre Baloğlu"))
"""
"""

liste = ["233","ads","12qw","12","qss"]
for a in liste:

    try:
        print(int(a))
    except ValueError:
        print( "integre yok")
"""
"""
a = int(input("bir sayı girin:"))
def tek(a):


    if a % 2 ==0:
        return a
    else:
        raise ValueError("çift değil")



print(tek(a))
"""
















