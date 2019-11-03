a = int(input("Masukkan bilangan ke 1:"))
b = int(input("Masukkan bilangan ke 2:"))
c = int(input("Masukkan bilangan ke 3:"))

if a > b and a > c:
    print("Bilangan terbesar adalah:", a)
elif b > a and b > c:
    print("Bilangan terbesar adalah:", b)
else:
    print("Bilangan terbesar adalah:", c)
