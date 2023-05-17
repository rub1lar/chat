import openpyxl
from openpyxl import load_workbook


def mostrar_contenido_excel(ruta_archivo, nombre_hoja):
    # Cargar el archivo de la hoja de cálculo
    workbook = openpyxl.load_workbook(ruta_archivo)
    # Seleccionar la hoja de cálculo
    sheet = workbook[nombre_hoja]
    # Obtener las dimensiones de la hoja de cálculo
    filas = sheet.max_row
    columnas = sheet.max_column
    # Iterar sobre las filas y columnas
    for fila in range(1, filas + 1):
        for columna in range(1, columnas + 1):
            # Obtener el valor de la celda
            valor = sheet.cell(row=fila, column=columna).value
            # Imprimir el valor de la celda
            print(valor, end="\t")
        # Imprimir salto de línea después de cada fila
        print()


# Ejemplo de uso
ruta_archivo = "datos2.xlsx"
nombre_hoja = "Hoja 1"

mostrar_contenido_excel(ruta_archivo, nombre_hoja)


def buscar_nombre_en_tabla(ruta_archivo, nombre_hoja, nombre_buscar):
    # Cargar el archivo de Excel
    workbook = load_workbook(ruta_archivo)

    # Seleccionar la hoja de cálculo que nos interesa
    sheet = workbook[nombre_hoja]
    # Buscar el nombre en la tabla
    for row in sheet.iter_rows():
        for cell in row:
            if cell.value == nombre_buscar:
                # Obtener la posición de la fila y la columna
                fila = cell.row
                columna = cell.column_letter
                # Obtener el contenido de la celda
                contenido = cell.value
                return fila, columna, contenido
    # Si el nombre no se encuentra en la tabla
    return None, None, None


# Ejemplo de uso
nombre_buscar = "Parker Lai"

fila, columna, contenido = buscar_nombre_en_tabla(
    ruta_archivo, nombre_hoja, nombre_buscar
)
if fila and columna:
    print(
        f"El nombre '{nombre_buscar}' se encuentra en la fila {fila}, columna {columna}"
    )
    print("Contenido:", contenido)
else:
    print(f"El nombre '{nombre_buscar}' no se encuentra en la tabla")


# averiguar datos


def obtener_datos(ruta_archivo, nombre_hoja, valor_buscar):
    # Cargar el archivo de Excel
    workbook = load_workbook(ruta_archivo, read_only=True)

    # Seleccionar la hoja de cálculo que nos interesa
    sheet = workbook[nombre_hoja]

    # Buscar el valor en la tabla
    celdas_siguientes = []
    encontrado = False

    for row in sheet.iter_rows():
        for cell in row:
            if encontrado:
                # Agregar el valor de la celda siguiente a la lista
                celdas_siguientes.append(cell.value)

            if cell.value == valor_buscar:
                # Encontrar el valor buscado
                encontrado = True

    # Devolver la lista de celdas siguientes
    return celdas_siguientes


# Ejemplo de uso
nombre_datos_a_buscar = "Layla Wu"

celdas_siguientes = obtener_datos(ruta_archivo, nombre_hoja, nombre_datos_a_buscar)
if celdas_siguientes:
    print("Datos de La Persona Buscada:")
    print(celdas_siguientes)
else:
    print("No se encontró el nombre" + nombre_datos_a_buscar + " en la tabla")
