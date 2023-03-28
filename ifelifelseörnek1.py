boy = float(input("boyunuzu giriniz(metre cinsinden ör.1.60): "))
kilo = int(input("kilonuzu giriniz: "))
bki = kilo / (boy ** 2)
if bki < 18.5:
    print("zayıfsınız ")
elif 18.5 <= bki < 25:
    print("normalsiniz ")
elif 25 <= bki < 30:
    print("fazla kilolusunuz ")
else:
    print("obez ")
