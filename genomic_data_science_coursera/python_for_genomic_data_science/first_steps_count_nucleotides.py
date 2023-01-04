dna = "atcgactgagtcgatcgatcgatctcggactgcatgcatcgatcgtcggatcgatgcatggcatgctagcatgctagctgctgatcgatgc"

print(f"a = {dna.count('a')}")
print(f"t = {dna.count('t')}")
print(f"c = {dna.count('c')}")
print(f"g = {dna.count('g')}")
print(f"Length = {len(dna)}")
print(f"'GC' % = {((dna.count('g') + dna.count('c')) * 100) / len(dna):.2f}")

print(chr(110))

print(dna.find("gac"))
print(dna.find("gac", 3))

print(type(0x12))
print(type(1e10))

print(4+6/2+2*2)

print(1234567)
print(1.234567*10**6)

a = 1
b = 2
c = a + b
a = b
a = c
d = a + c

print(a, b, c, d)
