def consolidar_ventas(datos: list):
  #inicializo variables
    total_ventas_punto = 0  
    total_ventas_virtual = 0
    for i in range(len(datos)):  
      #conionales 
        if datos[i]["tipo_venta"] == "virtual":  
            total_ventas_virtual += int(datos[i]["total_factura"])
        elif datos[i]["tipo_venta"] == "punto": 
            total_ventas_punto += int(datos[i]["total_factura"])
    #guardo variables en un diccionario 
    total_ventas = {"total_ventas_punto":total_ventas_punto,"total_ventas_virtual":total_ventas_virtual} 
    # retorno diccionario
    return total_ventas 

# Función ZIP
'''
* Zip es una función para reorganizar listas
* Como parámetros admite un conjunto de listas

*La función zip empareja el primer elemento de cada iterador 
luego a los segundos elementos y así sucesivamente.

* Los iterables pueden ser listas Python, diccionarios, 
  cadenas, o cualquier objeto iterable.

Lo que hace es tomar un elemento  de cada lista y unirlos 
en una tupla, después une todas las tuplas en una sola lista.
'''
