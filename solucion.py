# En este archivo debes implementar la función

def reloj_arena(m: int, s: str) -> str:
    # TODO: validar altura mayor que 0 e imprimir "Error: La altura debe ser un entero positivo" y salir
    if m<=0:
        print("Error: La altura debe ser un entero positivo")
        return
    # TODO: implementar la lógica para generar el reloj de arena en ASCII
    c = s[0]
    lineas = []

    # Parte superior
    for i in range(m):
        espacios = i
        chars = 2 * (m - i) - 1
        lineas.append(" " * espacios + c * chars)

    # Parte inferior
    for i in range(1, m):
        espacios = m - i - 1
        chars = 2 * i + 1
        lineas.append(" " * espacios + c * chars)

    return "\n".join(lineas)



        


