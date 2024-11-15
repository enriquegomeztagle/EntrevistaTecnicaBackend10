
# Preguntas Teóricas

1. ¿Qué es el algoritmo de Manacher y para qué se utiliza?

- Es un algoritmo para encontrar el palíndromo más largo en cadenas.

- Tiene tiempo lineal O(n) y busca simetrías.

- Sirve para encontrar todos los palíndromos en una cadena.

2. Explica por qué los algoritmos de cadenas suelen ser intensivos en tiempo y cómo optimizarlos.

- Porque cualquier operación de búsqueda y/o comparación requiere tiempo proporcional al tamaño de tu cadena.

- Conforme crece tu cadena, aumenta tu complejidad computacional.

- Una forma de optimizarlos es usar alguna estructura de datos como algún árbol o una hash table y combinarlo con algoritmos como KMP o Rabin-Karp.

- Otra forma puede ser algún preprocesamiento, técnicas de sliding window o un autómata finito.

3. ¿Cuándo es útil construir un sufijo array para procesamiento de cadenas?

- Si ocupas buscar algún patrón rapidamente en un texto grande.

- Encontrar el substring común más largo que hay entre dos cadenas.

- Poder comparar cadenas de forma eficiente.
