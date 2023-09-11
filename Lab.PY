import matplotlib.pyplot as plt

# Mensaje de bienvenida
print("Bienvenido al Laboratorio de Suma")

# Inicializamos una lista vacía para almacenar los números ingresados
numeros = []

# Inicializamos una lista para almacenar la suma acumulativa
suma_acumulativa = []

# Ciclo para ingresar números
while True:
    try:
        numero = float(input("Ingresa un número (o introduce 0 para finalizar): "))
        
        # Verificamos si el usuario desea finalizar ingresando 0
        if numero == 0:
            break
        
        # Agregamos el número a la lista1
        numeros.append(numero)
        
        # Actualizamos la suma acumulativa
        suma_acumulativa.append(sum(numeros))
        
        # Mostramos la suma acumulativa actualizada
        print(f"Suma acumulativa: {suma_acumulativa[-1]}")
    
    except ValueError:
        print("¡Error! Ingresa un número válido.")

# Mostramos la suma colectiva
print(f"La suma colectiva de los números ingresados es: {suma_acumulativa[-1]}")

# Mostramos la lista de números ingresados
print("Lista de números ingresados:")
print(numeros)

# Creamos el gráfico
plt.bar(range(len(suma_acumulativa)), suma_acumulativa)
plt.xlabel('Iteración')
plt.ylabel('Suma Acumulativa')
plt.title('Suma Acumulativa de Números Ingresados')
plt.show()
