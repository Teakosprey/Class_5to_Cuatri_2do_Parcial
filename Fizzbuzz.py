#Escribe un programa que mustre los numeros del 1 al 100 y que cambie:
#Los multiplos de 3 por la palabra “Fizz”.
#Los multiplos de 5 por la palabra “Buzz".
#Los multiplos de 3 y 5 por la palabra “FizzBuzz”.

for i in range(1,101):
    if i %3==0 and i %5==0:
        print("FizzBuzz")
    else:
        if i %3==0:
            print("Fizz")
        else:
            if i %5==0:
                print("Buzz")
            else:
                print(i)