#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: alvarocamarafernandez
"""

lstPrimes = [2]


class NotPrime(Exception):
    """
    Excepción creada para indicar que el número introducido no es primo de Blum.
    
    Para lanzar esta exception, usamos:
        
        - n: Excepcion que indica que el número de entrada no es primo. 
        
    """
    
    def __init__(self, n):
        self.n = n
        super().__init__("El valor " + str(n) + " no es primo.")

def initialDescription():
    """
    Muestra por pantalla la descripción del programa.
    """
    string = "        ----- GENERADOS DE NÚMEROS PSEUDOALEATORIO -----        " + '\n\n' 
    string += "Este programa está pensado para generar una determinada cantidad de números aleatorios a partir de una semilla dada. \n\n"
    string += "Inicialmente, el programa le pedira introducir el tamaño de números generados y la semilla usada para producir los números pseusoaleatorios. \n\n"
    string += "Posteriormente, podrá indicar, de las opciones, el generador que desea aplicar así como sus parámetros en caso de necesitarse. \n\n"
    string += "Para utilizar el algoritmo M (shuffleSequences), es necesario disponer de 2 generadores de números aleatorios. Por lo que si se desea usar este algoritmo, se pedirá generar una nueva secuancia.\n\n"
    string += "Es posible resetear el generador utilizado usando 'reset' una vez se tenga la secuencia pseudoaleatoria generada. \n"
    print (string)


def isPrimeNumber(p):
    """

    Parameters
    ----------
    p : INT
        número que analizaremos si es o no primo

    Returns
    -------
    True o False en caso que el número de entrada sea primo o no
    """
    if not isinstance(p, int) or p <= 1:
        raise TypeError("El valor " + (str(p)) + " no es de tipo entero o es menor o igual que 1." )
    
    #casos especiales a tener en cuenta
    if p <= 1:
        return False
    
    if p == 2 or p == 3: #el 2 y el 3 son numeros primos
        return True
    
    if p%2 == 0 or p%3 == 0: #si se puede dividir entre 2 o 3, entonces no es primo
        return False
    
    i = 5
    while pow(i,2) <= p:
        if p % i == 0 or p % (i+2) == 0:
            return False
        i += 6
    return True


def isBlumPrime(n, isPrime = False): 
    """

    Parameters
    ----------
    n : INT
        número que analizaremos si es o no primo de Blum.
    isPrime : Bool
        Booleano que si es False, indica que el valor n no es primo. Si isPrime es True, significa que n si es primo

    Returns
    -------
    True o False
    """
    if not isinstance(n, int) or n <= 1:
        raise TypeError("El valor " + (str(n)) + " no es de tipo entero o es menor o igual que 1." )
    
    if not isPrime: #si sabemos que el valor no es primo, lo comprobamos
        if not isPrimeNumber(n):
            raise NotPrime( str(n) )
    
    if (n - 3) % 4 == 0: 
        return True
    return False


def listOfPrimes(n):
    """

    Parameters
    ----------
    n : INT
        numero entero que representa el máximo elemento a ser analizado.

    Returns
    -------
    Lista de todos los números primos menores o iguales que n. Usamos la variable global lstPrimes para que el algoritmo sea mas eficiente.

    """
    global lstPrimes

    # Si ya hemos encontrado todos los primos hasta n, simplemente devolvemos la lista existente
    if lstPrimes[-1] >= n:
        return [p for p in lstPrimes if p <= n]

    # Si n es menor que 2, no hay primos
    if n < 2:
        return []

    # Inicializar una lista de booleanos para marcar si un número es primo. Utilizamos la criba de Eratóstenes
    es_primo = [True] * (n + 1)
    es_primo[0] = es_primo[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if es_primo[i]:
            for j in range(i * i, n + 1, i):
                es_primo[j] = False

    # Construir la lista de primos con todos los valores que sean true
    lstPrimes = [i for i in range(n + 1) if es_primo[i]]

    return lstPrimes


def BlumPrimes(n):
    """
    Parameters
    ----------
    n : INT
        numero entero que representa el máximo elemento a ser analizado.

    Returns
    -------
    Lista de todos los números primos de Blum menores o iguales que n.
    """
    if not isinstance(n, int):
        raise TypeError("El valor " + (str(n)) + " no es de tipo entero." )
    
    listOfPrimes(n)
    return [i for i in lstPrimes if isBlumPrime(i, True)]

