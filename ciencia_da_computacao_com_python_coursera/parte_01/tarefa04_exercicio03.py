def vogal(a):
    if a in "aeiouAEIOU":
        return True
    else:
        return False


abc = input("Digite uma letra: ")

print(vogal(abc))
