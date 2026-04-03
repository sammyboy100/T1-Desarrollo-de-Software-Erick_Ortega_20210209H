def encontrar_clientes_fieles(archivo_entrada):
    # Leemos el archivo
    with open(archivo_entrada, 'r') as archivo:
        lineas = [linea.strip() for linea in archivo.readlines() if linea.strip()]
        
    if not lineas:
        return

    # 1. Leer los tres números principales: Socios(N), Terminales(M), Transacciones(S)
    valores_principales = lineas[0].split()
    N = int(valores_principales[0])
    M = int(valores_principales[1])
    S = int(valores_principales[2])

    # Diccionario para saber a qué socio le pertenece cada terminal
    # Formato: {id_terminal: id_socio}
    terminal_a_socio = {}
    
    # Diccionario para llevar la cuenta de las compras. 
    # Formato: {id_socio: {id_cliente: cantidad_compras}}
    # Lo inicializamos para todos los socios del 1 al N, porque todos deben aparecer en la respuesta.
    compras_por_socio = {i: {} for i in range(1, N + 1)}

    # 2. Leer los M terminales
    for i in range(1, M + 1):
        partes = lineas[i].split()
        p = int(partes[0]) # ID del socio
        t = int(partes[1]) # ID del terminal
        terminal_a_socio[t] = p

    # 3. Leer las S transacciones (compras)
    # Empiezan justo después de los terminales (índice M + 1)
    for i in range(M + 1, M + 1 + S):
        partes = lineas[i].split()
        c = int(partes[0]) # ID del cliente
        t = int(partes[1]) # ID del terminal donde compró
        
        # Buscamos a qué socio le pertenece la máquina 't'
        if t in terminal_a_socio:
            p = terminal_a_socio[t]
            
            # Si es la primera vez que el cliente compra en este socio, le ponemos 0
            if c not in compras_por_socio[p]:
                compras_por_socio[p][c] = 0
            
            # Le sumamos 1 compra a su cuenta
            compras_por_socio[p][c] += 1

    # 4. Determinar el cliente más fiel para cada socio y mostrar el resultado
    for p in range(1, N + 1):
        clientes_de_este_socio = compras_por_socio[p]
        
        # Si el diccionario de clientes está vacío, significa que no hubo ventas
        if not clientes_de_este_socio:
            print(f"{p} -1")
        else:
            mejor_cliente = -1
            max_compras = -1
            
            # Comparamos todos los clientes de este socio
            for cliente_id, cantidad_compras in clientes_de_este_socio.items():
                # Si este cliente tiene MÁS compras que el máximo actual
                # O si tienen LA MISMA cantidad de compras, pero su ID de cliente es MENOR (regla de desempate)
                if cantidad_compras > max_compras or (cantidad_compras == max_compras and cliente_id < mejor_cliente):
                    max_compras = cantidad_compras
                    mejor_cliente = cliente_id
                    
            print(f"{p} {mejor_cliente}")

# Punto de inicio del programa
if __name__ == '__main__':
    encontrar_clientes_fieles('input2.txt')