import openpyxl

def matriz_a_excel(matriz, nombre_archivo):
    # Crear un libro de trabajo y una hoja
    libro = openpyxl.Workbook()
    hoja = libro.active

    # Escribir la matriz en la hoja
    for i, fila in enumerate(matriz, start=1):
        for j, valor in enumerate(fila, start=1):
            hoja.cell(row=i, column=j, value=valor)

    # Guardar el archivo de Excel
    libro.save(nombre_archivo)
    print(f"Matriz guardada en {nombre_archivo}")

# Ejemplo de uso
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matriz_a_excel(matriz, "matriz.xlsx")