# T1 - Desarrollo de Software

Autor: Erick Daniel Ortega Moran

Este repositorio contiene las soluciones en Python para la primera práctica de laboratorio. El enfoque de ambos scripts es el procesamiento de cadenas de texto y la manipulación de estructuras de datos como diccionarios y listas para resolver problemas de lógica de programación.

---

## Estructura del Repositorio

* p1DS.py : Código fuente de la solución al Problema 1.
* input.txt : Archivo de texto con los casos de prueba para el Problema 1.
* p2DS.py : Código fuente de la solución al Problema 2.
* input2.txt : Archivo de texto con los casos de prueba para el Problema 2.

---

## Problema 1: Simulador de Enrutamiento (SPA)

El primer script simula el sistema de enrutamiento de una página web. Recibe un directorio de rutas válidas y evalúa las peticiones entrantes de los usuarios, devolviendo el contenido correspondiente o un error 404.

### Desglose del código (p1DS.py):

* Lectura y limpieza de datos: 
Se utiliza `open()` para procesar el archivo `input.txt`. Se utiliza comprensión de listas `[linea.strip() for linea in archivo.readlines()]` para eliminar saltos de línea innecesarios.

* Almacenamiento de rutas: 
Se utiliza `split(maxsplit=1)` en lugar de un split normal. Esto es crucial para separar correctamente la ruta (ej. /profile) de su contenido, evitando que el contenido se corte si tiene espacios intermedios.

* Detección de parámetros dinámicos: 
Para comparar las peticiones con las rutas base, se divide cada una por bloques usando `split('/')`. Mediante la función `zip()`, se comparan simultáneamente. Si un bloque de la ruta empieza con dos puntos (`startswith(':')`), el programa sabe que no debe buscar una coincidencia exacta, sino capturar ese valor y agregarlo a la lista `parametros`.

* Limpieza con expresiones regulares: 
Al encontrar una coincidencia, se hace uso de `import re`. La instrucción `re.sub(r'\{.*?\}', '', contenido)` se encarga de buscar y eliminar del contenido original cualquier texto encerrado entre llaves (como el "{id}"), para poder imprimir un resultado limpio concatenado con los parámetros capturados.

---

## Problema 2: Cliente Más Fiel

El segundo script analiza un volumen de transacciones de distintos terminales de pago. Su objetivo es relacionar cada terminal con su socio correspondiente y determinar qué cliente registró la mayor cantidad de operaciones por socio.

### Desglose del código (p2DS.py):

* Diccionario de mapeo O(1): 
Se inicializa el diccionario `terminal_a_socio`. Este segmento lee los datos y guarda como clave el ID del terminal y como valor el ID del socio. Esto permite que más adelante, al leer cada transacción, el programa sepa a quién le pertenece la máquina de forma inmediata sin necesidad de bucles anidados.

* Estructura de anidamiento para el conteo: 
Se crea el diccionario `compras_por_socio`, donde cada llave (el socio) contiene otro diccionario vacío. Al procesar las transacciones, el código hace `compras_por_socio[p][c] += 1`. Si el cliente no existe aún en el registro de ese socio, primero se inicializa en cero. Esto crea un historial completo de las frecuencias de compra.

* Lógica de evaluación y desempate: 
En la fase final, se itera sobre los clientes de cada socio usando `.items()`. La línea clave aquí es la condición del if:
`if cantidad_compras > max_compras or (cantidad_compras == max_compras and cliente_id < mejor_cliente):`
Esta línea garantiza que el programa reemplace al "mejor cliente" si encuentra uno con más compras, pero también asegura que si dos clientes tienen la misma cantidad de compras, gane estrictamente el que tenga el número de ID inferior.

* Manejo de casos nulos: 
Antes de evaluar las frecuencias, un `if not clientes_de_este_socio:` verifica si el socio tuvo alguna venta. Si el diccionario está vacío, el programa imprime automáticamente `-1`.