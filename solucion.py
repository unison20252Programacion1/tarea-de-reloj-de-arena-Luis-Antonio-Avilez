# En este archivo debes implementar la función

def reloj_arena(m: int, s: str) -> str:
    # TODO: validar altura mayor que 0 e imprimir "Error: La altura debe ser un entero positivo" y salir
    # La función NO debe imprimir; debe devolver el mensaje.
    if m <= 0:
        return "Error: La altura debe ser un entero positivo"

    # TODO: implementar la lógica para generar el reloj de arena en ASCII
    c = s[0]
    lineas = []

    # Parte superior (triángulo invertido)
    ancho_max = 2 * m - 1
    for i in range(m):
        espacios = i
        chars = ancho_max - 2 * i
        lineas.append(" " * espacios + c * chars)

    # Parte inferior (triángulo normal)
    for i in range(m - 2, -1, -1):
        espacios = i
        chars = ancho_max - 2 * i
        lineas.append(" " * espacios + c * chars)

    return "\n".join(lineas)
