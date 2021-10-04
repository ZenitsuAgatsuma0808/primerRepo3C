# Este programa calcula la edad y año de retiro persona, dadas su edad actual y la edad a la que se quiere retirar
# 04 de octubre de 2021
# 1. Inicio
# Definir anio_actual = 2021
anio_actual = 2021
# 3. Preguntar al usuario "¿Qué edad tienes?"
print ("¿Qué edad tienes?")
# 4. Definir edad actual = entradad del usuario 
edad_actual = int(input()) # int() convierte texto en numero entero, es decir sin decimales
# 5. Preguntar al usuario "A qué edad te quieres retirar?"
print ("A que edad te quieres retirar?")
# 6. Definir edad de retiro = entrada del usuario
edad_de_retiro = int(input())
# 7. Hacer anios_para_retiro = edad de retiro - edad_actual
anios_para_retiro = edad_de_retiro - edad_actual
# 8. Hacer anio_de_retiro = anio_actual + anios_para_retiro
anio_de_retiro = anio_actual + anios_para_retiro
# 9. Mostrar mensaje "Tienes " anios_para_retiro" hasat que te puedas retirar"
print ("Tienes ", anios_para_retiro, "años hasta que te puedas retirar")
# 10. Mostrar mensaje "Es el año " anio_actual " entonces te podras retirar en " anio_de_retiro
print ("Es el año ", anio_actual, " entonces, te podras retirar en ", anio_de_retiro) 