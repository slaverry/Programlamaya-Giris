a = int(input("1 sayıyı giriniz"))
b = int(input("2. sayıyı giriniz"))
c = int(input("3.sayıyı giriniz"))

if a > b and a < c:
    print("a, b ve c arasındadır" )
elif a == b and a < c:
    print("a, b ye eşit c den küçüktür")
elif a > b or a > c:
    print("a, b ve c den büyüktür")
elif a == b ==c:
    print("a b ve c birbirine eşittir")
else:
    print("girilen koşulları sağlamayan durumlar var")
    
    
    
    #emirarslan
