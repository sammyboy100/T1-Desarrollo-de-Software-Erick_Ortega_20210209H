# T1 - Desarrollo de Software

**Autor:** Erick Daniel Ortega Moran

Este repositorio contiene las soluciones en Python para la primera práctica de laboratorio. El objetivo principal es aplicar estructuras de datos (como listas, diccionarios y formateo de cadenas) para procesar información y resolver problemas de lógica computacional.

---

## 📁 Estructura del Proyecto

* **`p1DS.py`** : Algoritmo de enrutamiento.
* **`input.txt`** : Datos de prueba para el Problema 1.
* **`p2DS.py`** : Algoritmo de fidelidad de clientes.
* **`input2.txt`** : Datos de prueba para el Problema 2.

---

## 🚀 Problema 1: Simulador de Enrutamiento (SPA)

### Descripción
El programa simula el motor de enrutamiento interno de una aplicación web (Single Page Application). Se encarga de procesar un listado de rutas base (algunas con variables dinámicas) y evalúa las peticiones del usuario para determinar qué contenido exacto se debe renderizar.

### Lógica del Código (`p1DS.py`)
La solución procesa las cadenas de texto paso a paso:
1. **Lectura y segmentación:** Extrae las rutas y peticiones, dividiendo cada URL por el carácter `/` para analizarla por bloques.
2. **Comparación simultánea:** Compara los fragmentos de la petición del usuario con los fragmentos de las rutas almacenadas.
3. **Captura de parámetros dinámicos:** Si identifica que un bloque de la ruta base empieza con `:`, el algoritmo lo reconoce como una variable, guarda el valor que el usuario ingresó y permite que la validación continúe.
4. **Respuesta:** Si la estructura coincide, imprime el contenido limpio y le adjunta las variables capturadas. Si la ruta no existe, devuelve un error controlado (`404 Not Found`).

**Comando de ejecución:**
> `python p1DS.py`

---

## 🏦 Problema 2: Cliente Más Fiel

### Descripción
Este script procesa un registro masivo de transacciones bancarias para identificar qué cliente tiene la mayor cantidad de compras en las máquinas POS (terminales) de cada uno de los socios comerciales.

### Lógica del Código (`p2DS.py`)
La solución está optimizada mediante el uso de tablas hash (diccionarios en Python) para realizar búsquedas y conteos en tiempo rápido:
1. **Mapeo de Terminales:** Se construye un primer diccionario que relaciona el ID de cada terminal con el ID de su socio dueño (`Terminal -> Socio`).
2. **Conteo de Frecuencias:** Al leer las compras, el programa busca a qué socio le pertenece la máquina usada e incrementa el historial de compras de ese cliente en un diccionario anidado (`Socio -> Cliente -> Cantidad`).
3. **Desempate y Selección:** Finalmente, el algoritmo itera sobre los registros de cada socio para encontrar el valor máximo de compras. Si ocurre un empate entre dos clientes, se aplica la condición matemática de seleccionar estrictamente al de menor ID. Si un socio no registró movimientos, el sistema imprime `-1`.

**Comando de ejecución:**
> `python p2DS.py`