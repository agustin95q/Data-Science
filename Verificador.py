import pandas as pd

def verificar_csv(ruta_csv):
    errores = []
    try:
        df = pd.read_csv(ruta_csv)
    except Exception as e:
        return [f"No se pudo leer el CSV: {e}"]

    # Normaliza encabezados
    df.columns = [str(c).strip().replace("\ufeff", "") for c in df.columns]

    #CSV vacio
    if df.shape[0] == 0:
        errores.append("El archivo está vacío (0 filas de datos).")
        return errores

    #Convertir indice de pandas a numero de línea del CSV 
    def filas(mask):
        return (mask[mask].index + 2).tolist()

    #Nombres repetidos
    if "Nombre" in df.columns:
        dup_mask = df["Nombre"].duplicated(keep=False)
        if dup_mask.any():
            filas_dup = filas(dup_mask)
            valores = df.loc[dup_mask, "Nombre"].tolist()
            errores.append(f"Hay Pokémon repetidos en 'Nombre'. Filas: {filas_dup}. Valores: {valores}")
    else:
        errores.append("Falta la columna obligatoria 'Nombre'.")

    #Nombre vacio
    if "Nombre" in df.columns:
        vacio_mask = df["Nombre"].isna() | (df["Nombre"].astype(str).str.strip() == "")
        if vacio_mask.any():
            errores.append(f"Existen Pokémon sin nombre. Filas: {filas(vacio_mask)}")

    return errores