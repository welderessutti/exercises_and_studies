segundos = int(input("Digite os segundos: "))

dias = segundos // 86400
'''print(dias)'''
segundos_restantes = segundos % 86400
'''print(segundos_restantes)'''
horas = segundos_restantes // 3600
'''print(horas)'''
segundos_restantes = segundos_restantes % 3600
'''print(segundos_restantes)'''
minutos = segundos_restantes // 60
'''print(minutos)'''
segundos_restantes = segundos_restantes % 60
'''print(segundos_restantes)'''

print(f"{dias} dias, {horas} horas, {minutos} minutos e {segundos_restantes} segundos.")
