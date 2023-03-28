sekil = input("hangi şekil tipini öğrenmek istiyorsunuz?: ")

if sekil == "dörtgen":
    print("lütfen kenar uzunluklarını sırayla giriniz")
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    d = int(input("d: "))
    if a == b and b == c and a == d:
        print("kare")
    elif a == c and b == d:
        print("eşkenar")
    else:
        print("dörtgen")
elif sekil == "üçgen":
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    if abs(a+b > c and a+c > b and c+b > a):
        if a == b and a == c:
            print("eşkanar üçgen")
        elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
            print("ikizkenar üçgen")
        else:
            print("çeşitkenar üçgen")

    else:
        print("üçgen belirtmiyor")
else:
    print("şekil belirtmiyor")
