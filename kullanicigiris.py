syskullaniciadi = "kevser"
sysparola = "123456"
kullaniciadi = input("kullanıcı adınızı giriniz: ")
parola = input("parolayı giriniz: ")
if kullaniciadi == syskullaniciadi and parola != sysparola:
    print("parola hatalı")
elif kullaniciadi != syskullaniciadi and parola == sysparola:
    print("kullanıcı adı hatalı")
elif kullaniciadi != syskullaniciadi and parola != sysparola:
    print("bilgilerin tümü hatalı!")
else:
    print("giriş başarılı")
