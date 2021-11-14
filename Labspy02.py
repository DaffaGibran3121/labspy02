print("Mencari bilangan terbesar dari 3 bilangan")

a = int(input("Masukkan Bilangan Pertama: "))
b = int(input("Masukkan Bilangan Kedua: "))
c = int(input("masukkan bilang ketiga: "))
if a > b > c:
    print("Bilangan Pertama Adalah Bilangan Terbesar = %s" % a)
elif b > c:
    print("Bilangan kedua Adalah Bilangan Terbesar = %s" % b)
else:
    print("Bilangan ketiga Adalah Bilangan Terbesar = %s" % c)