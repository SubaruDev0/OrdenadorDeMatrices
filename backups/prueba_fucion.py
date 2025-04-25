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

def contar_palabras_y_almacenar_en_matriz(nombre_archivo, n):
    
    try:
        with open("br17.txt", 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            palabras = contenido.split()
            matriz = [palabras[i:i + n] for i in range(0, len(palabras), n)]
            return len(palabras), matriz
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")
        return 0, []

# Ejemplo de uso
if __name__ == "__main__":
    archivo = "archivo_ejemplo.txt"  # Cambia esto por el nombre de tu archivo
    tamano_sublista = 17  # Cambia esto por el tamaño deseado de las sublistas
    total_palabras, matriz_palabras = contar_palabras_y_almacenar_en_matriz(archivo, tamano_sublista)
    print(f"El archivo contiene {total_palabras} palabras.")
    print("Matriz de palabras:")
    matriz_a_excel(matriz_palabras, "matriz.xlsx")