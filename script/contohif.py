a = float(input("a : "))
b = float(input("b : "))
if(a>b):
    print("a lebih besar dari b")
    if(a>(10+b)):
        print("a masih lebih besar dari b walau ditambahin 10")
    else:
        print("a tidak lebih besar dari b jika ditambahin 10")
elif(a==b):
    print("a sama dengan b")
else:
    print("a kurang dari b")
    if(a<(10+b)):
        print("a masih lebih kecil dari b walau ditambahin 10")
    else:
        print("a lebih besar dari b jika ditambahin 10")
print("selesai")
