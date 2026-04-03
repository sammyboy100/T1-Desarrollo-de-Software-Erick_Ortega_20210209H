# T1 - Desarrollo de Software (Erick Daniel Ortega Moran)

Este repositorio almacena las soluciones en Python para la primera tarea de laboratorio.

## Archivos del Proyecto

* **`p1DS.py`** : Código del primer ejercicio (Enrutador web).
* **`p2DS.py`** : Código del segundo ejercicio (Fidelidad de clientes).
* **`input.txt`** : Casos de prueba para el primer ejercicio.
* **`input2.txt`** : Casos de prueba para el segundo ejercicio.

---

## 1) Simulador de enrutamiento — `p1DS.py`

**¿Qué hace?**
Es un programa que imita la navegación en una página web. Lee direcciones (algunas con variables como `/user/:id`) y revisa a qué contenido corresponden. Si el usuario intenta entrar a una dirección que no existe, el sistema arroja un error de no encontrado (`404 Not Found`).

**¿Cómo ejecutarlo?**
Asegúrate de tener el archivo `input.txt` en la misma carpeta y corre este comando en tu consola:
> `python p1DS.py`

---

## 2) Cliente más fiel por socio — `p2DS.py`

**¿Qué hace?**
Analiza un registro de ventas de distintos terminales para descubrir qué persona compró más veces en cada negocio. En caso de que dos personas tengan la misma cantidad de compras, elige al que tenga el número de identificador más bajo. Si un negocio no vendió nada, muestra un `-1`.

**¿Cómo ejecutarlo?**
Asegúrate de tener el archivo `input2.txt` en la misma carpeta y corre este comando en tu consola:
> `python p2DS.py`