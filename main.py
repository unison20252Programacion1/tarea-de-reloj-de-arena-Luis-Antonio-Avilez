# Completa las validaciones y llama a la función

import sys
from solucion import reloj_arena

def main():
    """
    data: lista de líneas leídas desde la entrada estándar o ingresadas por el usuario
          donde cada elemento de la lista es un string    
    """

    # Vamos a construir la lista de strings data en base a lectura desde stdin 
    # o en base a lectura interactiva usando input()
    if sys.stdin.isatty():
        # cuando el comando se ejecuta en forma interactiva
        data = []
        data.append(input("Ingresa la altura: ").strip())
        data.append(input("Ingresa el caracter: "))
    else:
        # cuando se usa redireccion de entrada (por ejemplo "python main.py < datos.txt")
        data = sys.stdin.read().strip().splitlines()

    # TODO: validar que data tenga 2 líneas
    if len(data) < 2:
        print("Error: Se esperan 2 lineas de entrada (altura, caracter)")
        return
        
    m_str = data[0].strip()
    s = data[1]

    # TODO: validar que s no sea vacío usando print("Error: El caracter no puede ser vacío")
    if s == "":
        print("Error: El caracter no puede ser vacío")
        return

    # TODO: intentar convertir m_str a entero y en caso de fallo imprimir and salir. 
    try:
        m = int(m_str)
    except ValueError:
        print("Error: La altura debe ser un numero entero")
        return

    # Llama a la función reloj_arena y muestra el resultado
    res = reloj_arena(m, s)

    if res is not None:
        print(res)

if __name__ == "__main__":
    main()
