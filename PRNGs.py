#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 19 20:29:12 2024

@author: alvarocamarafernandez
"""

from utils import utils
import math


class InvalidInput(Exception):
    """
    Excepción creada para indicar que el input introducido no es válido.
    
    Para lanzar esta exception, usamos:
        
        - string: cadena de caracteres usada para mostrar el mensaje al lanzar la excepcion. 
        
    """
    
    def __init__(self, string):
        self.string = string
        super().__init__(str(string))



class NotBlumPrime(Exception):
    """
    Excepción creada para indicar que el número introducido no es primo de Blum.
    
    Para lanzar esta exception, usamos:
        
        - n: indica el número el cual NO es primo de Blum. Es obligatorio.
        
        - lst: indica una lista de números de Blum, menores que n, que el usuario puede usar. Es opcional. Por defecto, la lista es vacía. 
    """
    
    def __init__(self, n, lst = []):
        self.n = n
        self.lst = lst
        super().__init__("El número " + str(n) + " no es un primo de Blum. Prueba con alguno de la siguiente lista: " + str(lst))



class PRNG(object):
    """
    Los diferentes métodos de esta clase constituyen diferentes generadores de números pseudoaleatorios.
    
    Para cada generador, necesitamos:
        - size: Será la cantidad de números aleatorios generados por el generador. Tiene que ser mayor o igual que 1
        
        - seed: semilla usada por el generador en cuestión.
        
        - lst: lista de números generada. Inicialmente, vacía. 
            
    En función del generador que estemos usando, se añadirán sus respectivos atributos.
    
    lista de métodos de la clase PRNG:
        -> __init__, __str__ , __addGeneratedNumber no deberían ser invocados desde fuera de los métodos de la clase
        
        -> LCG(a,c,m) -> genera una secuencia pseudoaleatoria mediante el algoritmo del generador lineal congruencial.
        
        -> BBS(p,q) -> genera una secuencia pseudoaleatoria mediante el algoritmo BBS
    """
    
    
    def __init__ (self, size, seed):
        if not isinstance (size, int) or size < 1:
            raise TypeError("El valor size = " + str(size) + " debe de ser tipo entero (int) mayor o igual a 1.")
        if not isinstance (seed, int) or seed < 1:
            raise TypeError("El valor seed = " + str(seed) + " debe de ser tipo entero (int) mayor o igual a 1.")
        self.__size = size
        self.__seed = seed
        self.__lst = []
        self.__module = 0
    
    
    def getSize(self): #devuelve el valor actual del atributo size
        return self.__size
    
    
    def setSize(self, size): #actualiza el valor actual del atributo size
        if not isinstance (size, int) or size < 1:
            raise TypeError("El valor size = " + str(size) + " debe de ser tipo entero (int) mayor o igual a 1.")
        self.__size = size
    
    
    def __getSeed(self): #devuelve el valor actual del atributo seed
        return self.__seed
    
    
    def __setSeed(self, seed): #actualizamos el valor de la semilla a un valor de tipo entero.
        if not isinstance (seed, int) or seed < 1:
            raise TypeError("El valor seed = " + str(seed) + " debe de ser tipo entero (int) mayor o igual a 1.")
        self.__seed = seed
    
    
    def getGeneratedNumbers(self): #devuelve el valor actual del atributo lst
        return self.__lst
    
    
    def __setGeneratedNumbers(self, genNumbers): #actualizamos el valor actual del atributo lst. Está pensado para usar con los algoritmos M y B
        if not isinstance (genNumbers, list):
            raise TypeError("El valor " + str(genNumbers) + " debe de ser tipo lista.")    
        self.__lst = genNumbers
        
        
    def __getModule(self): #la idea de este método es que sea privado y no sea accesible fuera de la clase. Se multiplica por 3 para mayor seguridad en caso de poder acceder
        return self.__module * 3
    
    
    def __setModule(self, module): #actualizamos el valor del módulo
        if not isinstance (module, int) or module < 0:
            raise TypeError("El valor module = " + str(module) + " debe de ser tipo entero (int) mayor o igual a 1.")
        self.__module = module
    
    
    def isEmpty(self): #booleano que devuelve True si no hay numeros generados o False en caso contrario
        return self.getGeneratedNumbers() == []
        
    
    def __str__ (self):
        res = "Lista de números generada: "
        n = len(self.getGeneratedNumbers())
        if n == 0:
            return res + '[]'
        else:
            for i in range(min(n , self.getSize())):
                res += str(self.getGeneratedNumbers()[i]) + ', '
            return res[:-2] + ' .'
        
        
    def __addGeneratedNumber (self, value): 
        """
        si la cantidad de numeros pseudoaleatorios generados es menor que el la cantidad a generar y el valor es de tipo int o float -> lo añadimos a la lista
        en caso contrario -> no hacemos nada

        Parameters
        ----------
        value : str
            nuevo valor pseudoaleatorio añadido a la lista

        Returns
        -------
        None.

        """
        if ((len(self.getGeneratedNumbers()) < self.getSize()) and isinstance(value, (int, float))): 
            self.__lst.append(value)
    
    
    def resetGenerator(self, seed = "None", amount = 10,  generator = True): #si generator = True -> reseteamos la lista de valores generados
        """
        resetea el objeto de la clase. Si tiene números generados, es posible borrarlos usando la variable generador. También es posible resetear la semilla utilizada.

        Parameters
        ----------
        seed : int
            nuevo valor para la semilla del algoritmo. Si el valor es "None", se deja la semilla anterior.

        generator : bool
            determina si eliminamos o no la lista de números generada
        
        amount : int
            determina la nueva cantidad de elementos pseudoaleatorios a generar
        Returns
        -------
        None.

        """
        if not isinstance (generator, bool):
            raise TypeError("El valor " + str(generator) + " debe de ser tipo bool.")
        
        if generator:
            self.__setGeneratedNumbers([])
        
        if seed != "None": 
            self.__setSeed(seed) #controla en input de seed
        self.__setModule(0)
        
    
    def LCG (self, a = 48271 , c = 0 , m = 2147483647 ):
        """

        Parameters
        ----------
        a : INT
            corresponde con el multiplicador del LCG. Se cumple que: 0 <= a < m
            En el caso concreto de que a = 0, la secuencia resultante será siempre constante.
            Por defecto, 'a' coge el valor 48271, que es primo.
        c : INT
            corresponde al incremento del LCG. Se cumple que: 0 <= c < m
            Por defecto, 'c' es nulo.
        m : INT
            es el módulo del LCG. Cumple que: m > 0
            Por defecto, 'm' coge el valor pow(2,31) - 1, que es primo. 
        
        Los valores por defecto han sido seleccionados para que represente la función del generador estándar mínimo minstd_rand usada en C++.
        
        Returns
        -------
        None.

        """
        #comprobamos que a,c,m son valores enteros y cumplen las condiciones anteriores:
        if not isinstance (a, int):
            raise TypeError ("El valor proporcionado para a = " + str(a) + " debe ser entero.")
            
        if not isinstance (c, int):
            raise TypeError ("El valor proporcionado para c = " + str(c) + " debe ser entero.")
            
        if not isinstance (m, int):
            raise TypeError ("El valor proporcionado para m = " + str(m) + " debe ser entero.")
        
        if not (0 <= a and a < m ):
            raise InvalidInput ("El valor proporcionado para a = " + str(a) + " debe ser mayor o igual a 0 y menor estricto que m = " + str(m) + " .")
            
        if not (0 <= c and c < m ):
            raise InvalidInput ("El valor proporcionado para c = " + str(c) + " debe ser mayor o igual a 0 y menor estricto que m = " + str(m) + " ." )
        
        if not ( m > 0 ):
            raise InvalidInput ("El valor proporcionado para m = " + str(m) + " debe ser mayor estricto que 0 .")
        
        if not self.isEmpty(): #comprobamos que no haya ningún elemento añadido a la lista
            raise InvalidInput ("Este generador contiene elementos pseudoaleatorios y solo se puede utilizar este método con le generador vacío. Resetea la lista.")
        
        #verificaciones finalizadas. Procedemos a generar la secuencia pseudoaleatoria.
        
        self.__setModule(m)
        for i in range(0, self.getSize()):
            if ( len(self.getGeneratedNumbers()) == 0 ): #si la lista está vacía -> primera iteración del bucle
                
                self.__addGeneratedNumber(pow(a * self.__getSeed() + c , 1 , m))
            
            else:   #la lista resultado tiene ya algún valor -> usamos los ya generados
                
                self.__addGeneratedNumber(pow(a * (self.getGeneratedNumbers()[ i-1 ]) + c , 1 , m))
        
    
    def BBS(self, p = 307 , q = 223):
        """
        Parameters
        ----------
        p : INT
            Primo de Blum asociado al algoritmo BBS
        
        q : INT
            Primo de Blum asociado al algoritmo BBS

        Returns
        -------
        None.

        """
        if not isinstance (p, int):
            raise TypeError ("El valor proporcionado para p = " + str(p) + " debe ser entero.")
            
        if not isinstance (q, int):
            raise TypeError ("El valor proporcionado para q = " + str(q) + " debe ser entero.")
        
        if not self.isEmpty(): #comprobamos que no haya ningún elemento añadido a la lista
            raise InvalidInput ("Este generador contiene elementos pseudoaleatorios y solo se puede utilizar este método con le generador vacío. Resetea la lista.")
        
        #comprobamos que la semilla sea mayor o igual que 1 y menor que N:
         
        N = p * q
        if self.__getSeed() < 1 or self.__getSeed() > N-1:
            raise InvalidInput("El valor de " + str(self.__getSeed()) + " es incorrecto pare el valor de " + str(N) + " . Debe de estar entre 1 y " + str(N-1) + ".")
        
        #comprobamos si, realmente, los números introducidos son primos de Blum
        
        tryP, tryQ = utils.isBlumPrime(p), utils.isBlumPrime(q) #lanzará una excepción si p y q no son números primos.
        
        if not tryP: #si p es primo, pero no es primo de Blum:
            lst = utils.BlumPrimes(max(p, q)) #lista de  números de primos de Blum menores que el máximo de p y q. 
            raise NotBlumPrime(p, lst)
        
        if not tryQ: #si p es primo, pero no es primo de Blum:
            lst = utils.BlumPrimes(max(p, q)) #lista de  números de primos de Blum menores que el máximo de p y q. 
            raise NotBlumPrime(q, lst)
        
        self.__setModule(N)
        for i in range(0, self.getSize()):
            if ( len(self.getGeneratedNumbers()) == 0 ): #si la lista está vacía -> primera iteración del bucle
                
                self.__addGeneratedNumber(pow(self.__getSeed(), 2 , N))
            
            else:
                
                self.__addGeneratedNumber(pow(self.getGeneratedNumbers()[ i-1 ], 2 , N))
        
        
    def shuffleSequences(self, prng, k = 100): #TODO añadir descripcion. Representa el algoritmo M de Knuth
        if not isinstance(prng, PRNG):
            raise TypeError("Atributo de entrada no es un objeto de la clase PRNG.")
            
        if not isinstance(k, int):
            raise TypeError ("El valor proporcionado para k = " + str(k) + " debe ser entero.")

        if self.isEmpty() or prng.isEmpty():
            raise InvalidInput("Uno de los 2 generadores es vacío y no se puede efectuar el algoritmo.")

        if k <= 0 or k > min(len(self.getGeneratedNumbers()), len(prng.getGeneratedNumbers())): 
            raise InvalidInput("El valor k = " + str(k) + " debe ser un mayor o igual a 1 y menor o igual que la cantidad de números generados por ambos generadores: " + str(min(len(self.getGeneratedNumbers()), len(prng.getGeneratedNumbers()))) ++ " .")    
        
        m = prng.__getModule() // 3
        
        aux = (self.getGeneratedNumbers())[0:k] #lista con los primeros k valores del primer generador
        res = [0] * k
        for i in range(k):
            j = math.floor((k * prng.getGeneratedNumbers() [ i ] ) / m) # 0 <= j < k. 
            res [i] = aux [j]
            aux [j] = aux [i]
        
        self.__setGeneratedNumbers(res)
    
    
    def shuffleOwn(self, k = 100): #TODO añadir descripcion. Representa el algoritmo B de Knuth
        if not isinstance(k, int):
            raise TypeError ("El valor proporcionado para k = " + str(k) + " debe ser entero.")

        if self.isEmpty():
            raise InvalidInput("El generador está vacío y no se puede efectuar el algoritmo.")

        if k <= 0 or k > len(self.getGeneratedNumbers()) -1:
            raise InvalidInput("El valor k = " + str(k) + " debe ser mayor o igual a 1 y menor o igual que la cantidad de números generados por el generador menos 1: " + str(len(self.getGeneratedNumbers()) -1) + " .") 
        
        m = self.__getModule() // 3
        aux, value = (self.getGeneratedNumbers())[0:k], self.getGeneratedNumbers()[k] #lista con los primeros k valores del primer generador
        res = [0] * k
        for i in range(k):
            j = math.floor((k * value ) / m) # 0 <= j < k.
            value = aux[ j ]
            res[ i ] = value
            aux[ j ] = self.getGeneratedNumbers()[ i ]
        
        self.__setGeneratedNumbers(res)


