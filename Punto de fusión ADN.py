#cadena = input("Introduce la cadena de nucleótidos \n")
def contar_cadena(cadena):
    cadena_m = cadena.upper()
    numero_g = 0
    numero_c = 0 
    numero_a = 0
    numero_t = 0
    for i in cadena_m: 
        if i == 'A': 
            numero_a += 1 
        if i == 'C': 
            numero_c += 1 
        if i == 'G': 
            numero_g += 1 
        if i == 'T': 
            numero_t += 1 
    return 2*(numero_t+numero_a)+ 4*(numero_c+numero_c)

cadena = input("Introduzca la cadena para analizar: ")

print(f'El punto de fusión de la cadena introducida es {contar_cadena(cadena)}')
