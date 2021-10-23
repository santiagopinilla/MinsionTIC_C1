def consolidar_ventas(datos: list):
    total_ventas_punto = 0
    total_ventas_virtual = 0
    for i in range(len(datos)):
        if datos[i]["tipo_venta"] == "punto":
            total_ventas_punto += int(datos[i]["total_factura"])
        else:
            total_ventas_virtual += int(datos[i]["total_factura"])
    total_ventas = {"total_ventas_punto":total_ventas_punto,"total_ventas_virtual":total_ventas_virtual}
    return total_ventas




def generarReporteRegalo(dicReporte: dict):
    if dicReporte["antiguedad"] < 1:
        regalo = "Un Televisor de 43 Pulgadas y un bono para compras por valor de $100.000"
        reporteRegalo = {"regalo":regalo,"empleado":dicReporte["empleado"]}
    elif dicReporte["antiguedad"] >= 1 and dicReporte["antiguedad"] < 2:
        regalo = "Una Lavadora de 22 Kg y un bono para compras por valor de $200.000"
        reporteRegalo = {"regalo":regalo,"empleado":dicReporte["empleado"]}
    elif dicReporte["antiguedad"] >= 2 and dicReporte["antiguedad"] < 5:
        regalo = "Dos pasajes para San Andrés y un bono para compras por valor de $300.000"
        reporteRegalo = {"regalo":regalo,"empleado":dicReporte["empleado"]}
    elif dicReporte["antiguedad"] >= 5 and dicReporte["antiguedad"] < 10:
        regalo = "Una beca de estudio universitario para un hijo del empleado."
        reporteRegalo = {"regalo":regalo,"empleado":dicReporte["empleado"]}
    else:
        regalo = "Auxilio para compra de vivienda por el valor de Treinta millones de pesos."
        reporteRegalo = {"regalo":regalo,"empleado":dicReporte["empleado"]}
    return reporteRegalo

def reportarRegalo(dicEmpleado: dict):
    return f'{dicEmpleado["empleado"]} - Regalo: {dicEmpleado["regalo"]}'

#-----------------------------------------------------------------------------------------------------------------------------

def generarReporteRegalo(dicEmpleado: dict) -> str:
    antiguedad = dicEmpleado["antiguedad"]
    reporteRegalo = {
        "Empleado": dicEmpleado["empleado"],
        "Regalo": ""
    }
    
    if antiguedad < 1:
        reporteRegalo["Regalo"] = "Un televisor de 43” Pulgadas y un bono para compras por valor de $100.000"
    elif antiguedad >= 1 and antiguedad < 2:
        reporteRegalo["Regalo"] = "Una Lavadora de 22 Kg y un bono para compras por valor de $200.000"
    elif antiguedad >= 2 and antiguedad < 5:
        reporteRegalo["Regalo"] = "Dos pasajes para San Andrés y un bono para compras por valor de $300.000"
    elif antiguedad >= 5 and antiguedad < 10:
        reporteRegalo["Regalo"] = "Una beca de estudio universitario para un hijo del empleado"
    elif antiguedad >= 10:
        reporteRegalo["Regalo"] = "Auxilio para compra de vivienda por el valor de Treinta millones de pesos."
        
    return reporteRegalo
    
def reportarRegalo(reporteRegalo: dict) -> str:
    Empleado = reporteRegalo["Empleado"]
    Regalo = reporteRegalo["Regalo"]
    
    return f"{Empleado} - Regalo: {Regalo}"




'''  El curso de Python y Estadística se califica con dos parciales (el primero tiene un peso de 30% y el segundo 35%), una nota de laboratorios (25%) y una nota del trabajo final del curso (10%). Calcular la nota definitiva para un grupo de n estudiantes.

Se debe procesar n cantidad de datos de estudiantes con la siguiente información:
5.	Código del curso
6.	Calificación Primer parcial
7.	Calificación Segundo parcial
8.	Calificación Laboratorios
9.	Calificación Trabajo final 
Escriba una función que reciba como parámetros una lista de diccionarios que contengan la siguiente información:
5.	Cod_curso: str
6.	Nota_primer_parcial: float
7.	Nota_segundo_parcial: float
8.	Nota_laboratorios: float
9.	Nota_trabajo_final:float
Ejemplo Datos
datos: list = [
    {
        "cod_curso": 01
        "nota_primer_parcial": 4
        "nota_segundo_parcial ": 3
  "nota_laboratorios ": 4
  "nota_trabajo_final ": 4

    },
    
    {
        "cod_curso": 02
        "nota_primer_parcial": 3
        "nota_segundo_parcial ": 3
  "nota_laboratorios ": 5
  "nota_trabajo_final ": 4

    },

]


La respuesta debe retornar un diccionario con la siguiente información:
# total de estudiantes en los dos cursos
# total de estudiantes del curso de Python
# total de estudiantes del curso de Estadística
# Promedio de calificación del curso de Python
# Promedio de calificación del curso de Estadística
# de estudiantes que perdieron estadística
# de estudiantes que perdieron el curso de Python
# de estudiantes que obtuvieron calificación mayor o igual a 4.8 en el curso de Python.
# de estudiantes que obtuvieron calificación mayor o igual a 4.8 en el curso de Estadística.'''