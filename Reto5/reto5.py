'''import numpy as np 
import  pandas as pd

def examen(ruta_archivo_csv: str) -> dict:
    if ruta_archivo_csv.endswith('.csv'):
        try: 
            df_examen=pd.read_csv(ruta_archivo_csv)
            DF=df_examen.to_dict()
            print(df_examen.groupby('sexo').agg(np.mean))
            print('\n')
        except:
            return 'No es posible leer los datos, verifique la ruta'
    else:
        return 'Extension erronea'
    return (DF)'''