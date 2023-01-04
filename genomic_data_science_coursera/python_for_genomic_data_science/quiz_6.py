import sys
import random
import time

print(sys.version)


def create_dna(n, alphabet="actg"):
    return "".join([random.choice(alphabet) for i in range(n)])


def count1(dna, base):
    i = 0
    for c in dna:
        if c == base:
            i += 1 
    return i


def count2(dna, base):
    i = 0 
    for j in range(len(dna)):
        if dna[j] == base:
            i += 1 
    return i 


def count3(dna, base):
    match = [c == base for c in dna]
    return sum(match)


def count4(dna, base):
    return dna.count(base)


def count5(dna, base):
    return len([i for i in range(len(dna)) if dna[i] == base])


def count6(dna,base):
    return sum(c == base for c in dna)


dna = create_dna(1000000)
'''print(dna)'''

base = "a"

start = time.time()
print(count1(dna, base))
end = time.time()
print(f"count1 {end - start}")

start = time.time()
print(count2(dna, base))
end = time.time()
print(f"count2 {end - start}")

start = time.time()
print(count3(dna, base))
end = time.time()
print(f"count3 {end - start}")

start = time.time()
print(count4(dna, base))
end = time.time()
print(f"count4 {end - start}")

start = time.time()
print(count5(dna, base))
end = time.time()
print(f"count5 {end - start}")

start = time.time()
print(count6(dna, base))
end = time.time()
print(f"count6 {end - start}")

dir()
