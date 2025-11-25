# En este archivo debes implementar la función

def reloj_arena(m: int, s: str) -> str:
    # TODO: validar altura mayor que 0 e imprimir "Error: La altura debe ser un entero positivo" y salir
    if m<=0:
        print("Error: La altura debe ser un entero positivo")
        return
    # TODO: implementar la lógica para generar el reloj de arena en ASCII
     # Parte superior (triángulo invertido)
    for i in range(m):
        espacios = " " * i
        ancho = 2*(m - i) - 1
        print(espacios + s * ancho)

    # Parte inferior (triángulo normal)
    for i in range(m - 2, -1, -1):
        espacios = " " * i
        ancho = 2*(m - i) - 1
        print(espacios + s * ancho)



        


