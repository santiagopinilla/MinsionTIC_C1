def promedio_estatura(codigo:str,estatura1:float,estatura2:float,estatura3:float,estatura4:float,estatura5:float):
    estatura_promedio = int(((estatura1 + estatura2 + estatura3 + estatura4 + estatura5)/5)*100)/100
    return (f"El promedio de estatura de los 5 jugadores titulares del equipo de Baloncesto de la selección Colombia es: {estatura_promedio}")

