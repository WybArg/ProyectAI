# ==============================================================================
# SCRIPT: solicitar_nombre.py
# DESCRIPCIÓN: Este script solicita interactiva y secuencialmente el nombre del
#              usuario a través de la consola/terminal, y posteriormente
#              muestra un mensaje personalizado de bienvenida con dicho nombre.
# PROPÓSITO: Servir como ejemplo básico de interacción con el usuario mediante
#            entrada y salida estándar en Python, cumpliendo con las reglas del workspace.
# ==============================================================================

# Solicitar el nombre del usuario mediante la entrada estándar y guardarlo en la variable 'nombre'
nombre = input("Por favor, introduce tu nombre: ")  # Lee la entrada del usuario y la asigna a 'nombre'.

# Mostrar el mensaje de saludo utilizando la función print para imprimirlo en la terminal
print(f"Hola, {nombre}! Un placer saludarte.")  # Imprime un saludo personalizado con el nombre ingresado.
