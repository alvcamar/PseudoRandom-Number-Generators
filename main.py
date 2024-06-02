#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: alvarocamarafernandez
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) #definimos correctamente la raiz del proyecto


import PRNGs
from utils.utils import initialDescription
from utils.customExceptions import InvalidInput

def generate(prng):
    """
    Dado un objeto de la clase PRNG, esta funcion pregunta al usuario el algoritmo (método) a utilizar para generar la secuencia de números pseudoaleatoria.

    Parameters
    ----------
    prng : PRNG
        Objeto de la clase PRNG.

    Raises
    ------
    TypeError
        El objeto de entrada no es de la clase PRNG.
    ValueError
        El método a utilizar no es aceptado.

    Returns
    -------
    prng.

    """
    if not isinstance(prng, PRNGs.PRNG):
        raise TypeError("Atributo de entrada no es un objeto de la clase PRNG.")
    
    while True:
        try:
            ans = str(input(("Seleccione uno de los siguientes algoritmos generadores para usar: ['BBS', 'LCG'] --> ")))
            
            if ans.upper() == "BBS":
                print("Para utilizar valores por defecto, pulse enter.")
                values, params = [None] * 2 , ['p', 'q'] #valores p y q
                for i in range(0,2):
                    while True:
                        try:
                            val = input("Introduzca un valor para " + params[i] + ": ")
                            if val == '': #por defecto
                                values[i] = val
                        
                            else: #si hay texto introducido, hay que comprobar que sea de tipo INT
                                values[i] = int(val)
                            break
                        except:
                            print ("El valor introducido para " + params[i] + " debe de ser un número entero. Intentelo de nuevo.")
                
                if values[0] == '':     #valor p por defecto
                    if values[1] == '': #si ambos son vacíos, ejecutamos el caso por defecto
                        prng.BBS()
                    else:       #valor para q usamos el insertado
                        prng.BBS(q = values[1])
                else:   # valor para p usamos el insertado
                    if values[1] == '':     #valor para q es por defecto
                        prng.BBS(p = values[0])
                    else:
                        prng.BBS(p = values[0], q = values[1])
                break #si se llega a este punto, ha ido OK
            
            elif ans.upper() == "LCG":
                print("Para utilizar valores por defecto, pulse enter.")
                values, params = [None] * 3 , ['a', 'c', 'm'] #valores a, c y m
                for i in range(0,3):
                    while True:
                        try:
                            val = input("Introduzca un valor para " + params[i] + ": ")
                            if val == '': #por defecto
                                values[i] = val
                        
                            else: #si hay texto introducido, hay que comprobar que sea de tipo INT
                                values[i] = int(val)
                            break
                        except:
                            print ("El valor introducido para " + params[i] + " debe de ser un número entero. Intentelo de nuevo.")
                            continue
                
                if values[0] == '':     #valor a por defecto
                
                    if values[1] == '':     #valor c por defecto
                    
                        if values[2] == '':     #valor m por defecto
                            prng.LCG()
                        
                        else:       
                            prng.LCG(m = values[2])
                            
                    else:       
                        
                        if values[2] == '':     #valor m por defecto pero c no
                            prng.LCG(c = values[1])
                            
                        else:   #valor m y c son los obtenidos 
                            prng.LCG(c = values[1], m = values[2])
                
                else:     #valor a es el obtenido
                
                    if values[1] == '':     #valor c por defecto
                    
                        if values[2] == '':     #valor m por defecto
                            prng.LCG(a = values[0])
                        
                        else:       
                            prng.LCG(a = values[0], m = values[2])
                            
                    else:       
                        
                        if values[2] == '':     #valor m por defecto pero c no
                            prng.LCG(a = values[0], c = values[1])
                            
                        else:   #valor m y c son los obtenidos 
                            prng.LCG(a = values[0], c = values[1], m = values[2])
                break # si se llega a este punto, ha ido OK
            
            else:
                print("El valor introducido para el generador debe de ser uno de la lista anterior. Vuelve a intentarlo")
        
        except InvalidInput as error: #error en el algoritmo BBS o en el LCG. Si es en el algoritmo LCG -> volver a introducir los datos. Si es en el algoritmo BBS, hay que cambiar la semilla
            print(error)
            if ans.upper() == "BBS":
                print("Asegurese de resetear el generador.")
                break
            else:
                print("Seleccione de nuevo los valores a utilizar.")
                continue
            
        except Exception as error:
            print(error)
            continue
    
    return prng


def mix(prngList):
    """
    Dada una lista de objetos pertenecientes a la clase PRNG, esta funcion pregunta al usuario el algoritmo a utilizar y los generadores a mezclar y realiza la mezcla.

    Parameters
    ----------
    prngList : LIST
        Lista de objetos de la clase PRNG.

    Raises
    ------
    TypeError
        Los objetos de la lista de entrada no son de la clase PRNG.
    ValueError
        El método a utilizar no es aceptado.

    Returns
    -------
    None.

    """
    for prng in prngList:
        if not isinstance(prng, PRNGs.PRNG): 
            raise TypeError("Atributo de entrada no es un objeto de la clase PRNG.")
    
    while True:
        try:
            k = int(input("Indique la cantidad de elementos que tenga la secuencia mezclada: "))
            break
        except:
            print("El valor introducido debe ser de tipo entero. Intentelo de nuevo.")
            continue
    
    while True:
        try:
            ans = str(input(("Seleccione uno de los siguientes algoritmos generadores para mezclar: ['M', 'B'] --> ")))
        
            if ans.upper() == "M":
                print ("Se ha seleccionado el algoritmo de mezcla 'M': ")
                
                #preguntamos qué 2 generadores van a ser usados para mezclarse:
                txt = ""
                for index , _ in enumerate(prngList): 
                    txt += str(str(index + 1) + ", ")
                txt = txt[:-2]
                while True: #repetimos hasta obtener dos generadores correctos
                    try:
                        prngMixed = int (input("Seleccione el generador que será mezclado y modificado: [" + txt + "]: "))
                        prngMixedWith = int (input("Seleccione el generador que será utilizado para mezclar con el anterior (este no se modificará): [" + txt + "]: "))
                        
                        if (prngMixed < 0) or (prngMixed > len(prngList)) or (prngMixedWith < 0) or (prngMixedWith > len(prngList)):
                            print("Los valores introducidos para '" + str(prngMixed) + "' o para '" + str(prngMixedWith) + "' se encuentran fuera del rango de valores aceptados. Intentelo de nuevo")
                        elif prngMixed == prngMixedWith:    #si los 2 generadores introducidos coinciden, preguntamos si desea cambiarlos, ya que lo ideal es que sean generadores independientes
                            res = input("¿Está seguro de que desea usar los 2 mismos generadores para mezclarse (no son independientes)? (si/no): ")
                            if res.lower() == "si": # si se quiere utilizar -> OK
                                print("Se utilizarán los mismos generadores para mezclar.")
                                break
                            else:
                                print("Seleccione de nuevo ambos valores.")
                        else: #los 2 son generadores distintos dentro del rango posible -> OK
                            break
                    except:
                        print("El valor introducido debe ser de tipo entero. Intentelo de nuevo.")
                    
                generatorMixed = prngList[prngMixed - 1]
                generatorMixedWith = prngList[prngMixedWith - 1]
                
                generatorMixed.shuffleSequences(generatorMixedWith, k)
                print("Generador mezclado correctamente.")
                break
            
            elif ans.upper() == "B":
                print ("Se ha seleccionado el algoritmo de mezcla 'B': ")
                
                #preguntamos qué generador van a utilizarse para mezclarse:
                txt = ""
                for index , _ in enumerate(prngList):
                    txt += str("Generador " + str(index + 1) + ", ")
                txt = txt[:-2]
                while True: #repetimos hasta obtener dos generadores correctos
                    try:
                        prngMixed = int (input("Seleccione el número del generador que será mezclado y modificado: [" + txt + "]: "))
                        if (prngMixed < 1) or (prngMixed > len(prngList)): #valor incorrecto
                            print("El valor introducido para '" + str(prngMixed) + "' se encuentra fuera del rango de valores aceptados. Intentelo de nuevo.")
                            continue
                        else: #valor correcto
                            break
                    except:
                        print("El valor introducido debe ser de tipo entero. Intentelo de nuevo.")
                        continue
                    
                generatorMixed = prngList[prngMixed - 1]
                
                generatorMixed.shuffleOwn(k)
                print("Generador mezclado correctamente.")
                break
            else:
                print ("El valor introducido para el generador debe de ser uno de la lista anterior. Intentelo de nuevo.")

        except InvalidInput as error: #si se lanza este error es porque el valor introducido para k no es correcto -> Volvemos a preguntar al usuario el nuevo valor
            print(error)
            raise Exception()
        except Exception as error:
            print(error)
            continue

def execute():
    """
    Función encargada de ejecutar y gestionar el flujo de la creacion de las PRNGs, su visualización y la representación final de las mismas.

    Raises
    ------
    ValueError
        El valor introducido para representar la cantidad de PRNGs es incorrecto.

    Returns
    -------
    None.

    """
    initialDescription()
    while True:
        try: 
            amount = int(input("Introduzca la cantidad de generadores que desea crear (número menor que 5, por eficiencia): "))
            if amount <= 0 or amount > 4:
                print("El valor introducido debe ser positivo y menor que 5. Intentelo de nuevo.")
                continue
            else: 
                break
        except:
            print("El valor introducido para el generador debe de ser de tipo entero. Intentelo de nuevo.")
    
    prngList = []
    
    for i in range(amount): # creamos los generadores
        while True: #repetimos hasta obtener un generador correcto
            try:
                size  = int(input("Indique el número de elementos pseudoaleatorios a generar para el generador " + str(i+1) + ": " ))
            except:
                print("El valor introducido debe de ser de tipo entero. Intentelo de nuevo.")
                continue
            while True:
                try:
                    seed = int(input("Indique la semilla del generador " + str(i+1) + ": " ))
                    prngList.append(PRNGs.PRNG(size, seed))
                    break
                except:
                    print("El valor introducido debe de ser de tipo entero. Intentelo de nuevo.")
            break
    
    for index, generator in enumerate(prngList):
        print(" \n ---> GENERADOR " + str(index + 1) + ": ")
        generate(generator)
        while True:
            ans = input("¿Desea resetear el generador " + str(index + 1) + " y generarlo con nuevos valores? Si ha ocurrido un error, el generador se reseteará independientemente de la respuesta proporcionada (si/no): ")
            if ans.lower() == "si" or generator.isEmpty():
                while True: #repetimos hasta obtener un generador correcto
                    try:
                        size  = int(input("Indique el número de elementos pseudoaleatorios a generar para el generador " + str(i+1) + ": " ))
                    except:
                        print("El valor introducido debe de ser de tipo entero. Intentelo de nuevo.")
                        continue
                    while True:
                        try:
                            seed = int(input("Indique la semilla del generador " + str(i+1) + ": " ))
                            generator.resetGenerator(seed, size, True)  #reseteamos generador
                            break
                        except:
                            print("El valor introducido debe de ser de tipo entero. Intentelo de nuevo.")
                            continue
                    break
                generate(generator)
            elif ans.lower() == "no":
                break
            else:
                print("El valor introducido no coincide con los esperados (si/no). Intentelo de nuevo.")
                
                
    ans = input("Todos los generadores han sido creados y generados correctamente. ¿Desea mezclar alguno? (si/no): ")
    if ans.lower() == "si": #si queremos mezclar, damos la opcion a hacerlo la cantidad de veces que el usuario desee
        while True:
            try:
                mix(prngList)
                ans = input("Mezcla realizada con éxito. ¿Desea seguir mezclando? (si/no): ")
                if ans.lower() == "si":
                    print("Continuamos mezclando los generadores.")
                    continue
                elif ans.lower() == "no":
                    break
                else:
                    print("El valor introducido no coincide con los esperados (si/no). Intentelo de nuevo.")
                    continue
            except:
                print("Ha ocurrido un error, pruebe de nuevo.")
                continue
        
        print("Todos los generadores han sido mezclados con éxito.")
    
    while True:
        try:
            ans = int(input("¿Desea guardar las secuencias en archivos (1) o mostrarlas por pantalla(2)? (1,2): "))
            if ans in (1,2):
                break
            else:
                print("El valor introducido no es uno de los esperados. Intentelo de nuevo.")
                continue
        except:
            print("El valor introducido debe de ser de tipo entero. Intentelo de nuevo.")
            continue
    
    if ans == 1:
        if not os.path.exists("Generated Numbers"):
            os.makedirs("Generated Numbers")
        for index, generator in enumerate(prngList):
            name = input("Introduce un nombre para el archivo que va a contener los datos del generador " + str(index + 1) + " (solo nombre, no extensión del archivo): ")
            name += ".txt"
            routeFile = os.path.join("Generated Numbers", name)
            with open(routeFile, 'w') as file:
                for number in generator.getGeneratedNumbers():
                    file.write(str(number) + "\n") 
        print("Archivos creados correctamente en la carpeta 'Generated Numbers'. ")
    else:
        for index, generator in enumerate(prngList):
            print ("Generador " + str(index + 1) + ": ")
            print (generator)
        
    print("Fin de la ejecución.")
    

if __name__ == "__main__":
    execute()
