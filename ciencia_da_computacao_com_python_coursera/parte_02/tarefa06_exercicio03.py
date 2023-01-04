def elefantes(n):
    if n <= 0:
        return ""
    if n == 1:
        return "Um elefante incomoda muita gente" + "\n"
    return elefantes(n - 1) + str(n) + " elefantes " + incomodam(n) + ("muita gente" if n % 2 > 0 else "muito mais") + "\n"


def incomodam(n):
    if n <= 0:
        return ""
    if n == 1:
        return "incomodam "
    return "incomodam " + incomodam(n - 1)
