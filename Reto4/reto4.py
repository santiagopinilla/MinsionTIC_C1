'''def imprimir_resultados()->str:
    nombreImpuesto = [' Industria y Comercio ', ' Predial ', ' Alcohol, cigarrillos y loterías', ' Sobretasa a la gasolina ']        
    promedioRecaudosImpuestos = [223333333,350000000,533333333,533333333]
    for x in range(len(nombreImpuesto)):
        print("Impuesto:{}".format(nombreImpuesto[x]))
        print("")
        print("{} {:,}".format('Recaudo Enero :'.ljust(1),recaudoEnero[x]))
        print("{} {:,}".format('Recaudo Febrero :'.ljust(1),recaudoFebrero[x]))
        print("{} {:,}".format('Recaudo Marzo :'.ljust(1),recaudoMarzo[x]))
        print("{} {:,}".format('Promedio Recaudo Trimestre :'.ljust(1),promedioRecaudosImpuestos[x]))
        print("Meta: {}".format("Se alcanzó la meta del promedio de Recaudo en el Trimestre" if promedioRecaudosImpuestos[x] >= 500000000 else "No se alcanzó la meta del promedio de Recaudo en el Trimestre".ljust(1)))
        print("\n======================================================")'''