num = 0
num1 = 1
limit = int(input("Insert limit: "))

for i in range(limit):
    sig = num + num1  
    num = num1
    num1 = sig
    print(sig)