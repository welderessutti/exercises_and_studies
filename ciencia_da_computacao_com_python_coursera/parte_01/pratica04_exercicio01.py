def fizzbuzz(n):
    if n % 3 == 0 and n % 5 != 0:
        return "Fizz"
    elif n % 5 == 0 and n % 3 != 0:
        return "Buzz"
    elif n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    else:
        return n


num = int(input("Digite um número: "))

print(fizzbuzz(num))
