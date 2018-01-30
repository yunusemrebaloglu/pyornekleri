a = input("birinci aracın kilometrede yakıtğı")
ab = input("birinci aracın kilometresi")
b = input("ikinci aracın kilometrede yakıtğı")
bb = input("ikinci aracın kilometresi")
c = input("birinci aracın kilometrede yakıtğı")
cb = input("birinci aracın kilometresi")
a = int(a)
ab= int(ab)
b = int(b)
bb = int(bb)
c = int(c)
cb = int(cb)
af = a*ab
bf=b*bb
cf =c*cb
lisarac=[af,bf,cf]
sirali =sorted(lisarac)
print(sirali)
