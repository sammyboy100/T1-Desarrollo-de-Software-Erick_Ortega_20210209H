# T1 - Desarrollo de Software (Erick Daniel Ortega Moran)

[cite_start]Este repositorio contiene la solución a los dos problemas del Laboratorio 1, implementados en **Python**[cite: 22, 23].

## Archivos del Proyecto

* **`p1DS.py`** : Solución del Problema 1 (Simulador de enrutamiento).
* **`p2DS.py`** : Solución del Problema 2 (Cliente más fiel por socio).
* **`input.txt`** : Archivo de datos de prueba para el Problema 1.
* **`input2.txt`** : Archivo de datos de prueba para el Problema 2.

---

## 1) Simulador de enrutamiento — `p1DS.py`

**¿Qué hace?**
[cite_start]Simula el comportamiento de enrutamiento en una aplicación de una sola página (SPA)[cite: 1]. [cite_start]Recibe un conjunto de rutas (algunas con parámetros como `/user/:id`) y una lista de transiciones[cite: 5, 8]. [cite_start]El programa determina la ruta correspondiente y devuelve el contenido asociado, o muestra `404 Not Found` si la ruta no existe[cite: 6, 7].

**¿Cómo ejecutarlo?**
Asegúrate de que `input.txt` esté en la misma carpeta que el código y ejecuta en la terminal:
> `python p1DS.py`

---

## 2) Cliente más fiel por socio — `p2DS.py`

**¿Qué hace?**
[cite_start]Ayuda a determinar al cliente más fiel para cada socio del Banco de la Nación[cite: 24, 26]. [cite_start]Procesa una lista de terminales y transacciones para identificar qué cliente realizó la mayor cantidad de compras en los terminales de un socio específico[cite: 26]. [cite_start]Si hay un empate, prioriza al cliente con el ID más pequeño[cite: 28]. [cite_start]Si un socio no tiene ventas, devuelve `-1`[cite: 28].

**¿Cómo ejecutarlo?**
Asegúrate de que `input2.txt` esté en la misma carpeta que el código y ejecuta en la terminal:
> `python p2DS.py`