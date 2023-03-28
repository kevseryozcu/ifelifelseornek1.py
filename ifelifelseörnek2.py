a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
if a >= b and a >= c:
    print("en büyük sayı a")
elif b >= a and b >= c:
    print("en büyük sayı b")
elif c >= b and c >= a:
    print("en büyük sayı c")
