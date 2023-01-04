from math import hypot

cat = float(input('Digite o comprimento em cm do cateto: '))
cat_oposto = float(input('Digite o compromento em cm do cateto oposto: '))

hipotenusa = hypot(cat, cat_oposto)  # ou sqrt(cat**2 + cat_oposto**2) ou (cat**2 + cat_oposto**2) ** (1/2)

print(f'O comprimento da hipotenusa é {hipotenusa} cm.')
