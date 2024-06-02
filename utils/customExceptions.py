#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: alvarocamarafernandez
"""

class NotPrime(Exception):
    """
    Excepción creada para indicar que el número introducido no es primo de Blum.
    
    Para lanzar esta exception, usamos:
        
        - n: Excepcion que indica que el número de entrada no es primo. 
        
    """
    
    def __init__(self, n):
        self.n = n
        super().__init__("El valor " + str(n) + " no es primo.")

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
