# PseudoRandom-Number-Generators

## Descripción

En este proyecto se han implementado diversos algoritmos que generan números pseudoaleatorios, como el algoritmo BBS, LGC, y un par de algoritmos de mezcla de secuencias obtenidos del libro de Knuth. Este proyecto es capaz de crear secuencias pseudoaleatorias, mezclarlas, proporcionar una opción para mostrar por pantalla o guardar las secuencias generadas en un archivo de texto y, finalmente, obtener una gráfica en la que se muestran los tiempos de ejecución separados por algoritmos en función del número de elementos procesados.

## Instalación

1. Clonar el repositorio:
    ```sh
    git clone https://github.com/alvcamar/PseudoRandom-Number-Generators.git
    cd PseudoRandom-Number-Generators
    ```
2. Ejecutar el archivo `main.py` y seguir las instrucciones que se muestran por pantalla:
    ```sh
    python main.py
    ```
3. Configuración opcional: Dentro de la carpeta `utils` existe un archivo llamado `config.py` que contiene dos variables que el usuario puede modificar:
    - `amountPRNGs`: Cantidad máxima de generadores que se podrán generar.
    - `lengthOfPRNGs`: Cantidad de elementos pseudoaleatorios que debe generar cada generador en caso de que el usuario desee emplear esta variable.

## Uso

1. Ejecutar el archivo `main.py`:
    ```sh
    python main.py
    ```
2. Seguir las instrucciones que se muestran por pantalla para obtener los archivos con los números generados y la gráfica que muestra los tiempos de ejecución.

## Contribución

¡Las contribuciones son bienvenidas! Pueden añadir nuevos generadores, nuevas formas de mezclar, o incluso crear una nueva clase de pruebas y tests que comprueben la calidad de los elementos generados. Los números generados se guardan en archivos de texto.

## Autores

- Álvaro Cámara Fernández

## Tecnologías

- Lenguaje de programación: Python

## Licencia

Este proyecto está bajo la Licencia MIT - mira el archivo [LICENSE](LICENSE) para más detalles.

## Contacto

Para preguntas o problemas, puedes contactarme en [tu-email@ejemplo.com].

