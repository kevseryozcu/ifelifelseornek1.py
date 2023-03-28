vize1 = int(input("ilk vizenizi giriniz: "))
vize2 = int(input("ilk vizenizi giriniz: "))
vize3 = int(input("ilk vizenizi giriniz: "))
ortnot = (vize1 * 3/10 + vize2 * 3/10 + vize3 * 4/10)
if ortnot >= 90:
    print("AA")
elif ortnot >= 85:
    print("BA")
elif ortnot >= 80:
    print("BB")
elif ortnot >= 75:
    print("CB")
elif ortnot >= 70:
    print("CC")
elif ortnot >= 65:
    print("CD")
elif ortnot >= 60:
    print("DD")
elif ortnot >= 55:
    print("DF")
else:
    print("FF")
