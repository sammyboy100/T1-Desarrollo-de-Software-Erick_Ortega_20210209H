import re

def simular_enrutador(archivo_entrada):
    # Abrimos y leemos el archivo input.txt
    with open(archivo_entrada, 'r') as archivo:
        # Leemos las líneas y quitamos espacios en blanco o saltos de línea extra
        lineas = [linea.strip() for linea in archivo.readlines() if linea.strip()]
        
    if not lineas:
        return

    # 1. Leer la cantidad de rutas (N)
    N = int(lineas[0])
    rutas = []
    
    # Guardamos las N rutas en una lista de tuplas (path, contenido)
    for i in range(1, N + 1):
        # Separamos la ruta del contenido (ej: "/profile" y "ProfilePage")
        partes = lineas[i].split(maxsplit=1)
        path = partes[0]
        contenido = partes[1] if len(partes) > 1 else ""
        rutas.append((path, contenido))
        
    # 2. Leer la cantidad de transiciones (M)
    indice_M = N + 1
    M = int(lineas[indice_M])
    transiciones = lineas[indice_M + 1 : indice_M + 1 + M]
    
    # 3. Evaluar cada transición
    for transicion in transiciones:
        # Dividimos la ruta por las barras '/' para comparar bloque por bloque
        t_partes = transicion.split('/')
        encontrado = False
        
        for path, contenido in rutas:
            r_partes = path.split('/')
            
            # Solo comparamos si tienen la misma cantidad de bloques (ej: /user/42 y /user/:id)
            if len(t_partes) == len(r_partes):
                coincide = True
                parametros = []
                
                # Comparamos bloque por bloque
                for r, t in zip(r_partes, t_partes):
                    if r.startswith(':'): # Si es un parámetro (ej: :id)
                        parametros.append(t)
                    elif r != t: # Si no coinciden exactamente y no es parámetro, se descarta
                        coincide = False
                        break
                        
                if coincide:
                    encontrado = True
                    # Limpiamos el contenido por si tiene placeholders como "{id}" en el texto base
                    contenido_limpio = re.sub(r'\{.*?\}', '', contenido).strip()
                    
                    # Si capturamos parámetros, los añadimos al final [cite: 9]
                    if parametros:
                        print(f"{contenido_limpio} {' '.join(parametros)}")
                    else:
                        print(contenido_limpio)
                    break # Salimos del bucle porque ya encontramos la ruta correcta
                    
        # Si revisamos todas las rutas y ninguna coincidió [cite: 18, 19]
        if not encontrado:
            print("404 Not Found")

# Punto de entrada del programa
if __name__ == '__main__':
    # Llamamos a la función pasándole el nombre de nuestro archivo de texto
    simular_enrutador('input.txt')