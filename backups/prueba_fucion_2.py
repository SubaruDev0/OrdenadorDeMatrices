import openpyxl
import os

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

def matriz_a_txt(matriz, nombre_archivo):
    # Escribir la matriz en un archivo de texto con formato
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        for fila in matriz:
            # Convertir cada elemento a string y unirlos con tabulaciones
            linea = '\t'.join(str(valor) for valor in fila)
            archivo.write(linea + '\n')
    print(f"Matriz guardada en {nombre_archivo}")

def contar_palabras_y_almacenar_en_matriz(nombre_archivo):
    """
    Cuenta la cantidad de palabras en un archivo de texto y las almacenas en una matriz cuyo tamaño de sublistas
    se extrae de la fila 4 del archivo. La matriz se forma a partir de la línea 8 en adelante y excluye "EOF".

    :param nombre_archivo: Ruta del archivo de texto.
    :return: Una tupla con el número total de palabras y la matriz de palabras.
    """
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
            # Extraer el tamaño de la sublista desde la fila 4
            tamano_sublista = int(lineas[3].split(":")[1].strip())
            
            # Obtener el contenido desde la línea 8 en adelante
            contenido = ''.join(lineas[7:])
            palabras = contenido.split()
            
            # Excluir "EOF" si está presente
            if palabras[-1] == "EOF":
                palabras = palabras[:-1]
            
            matriz = [palabras[i:i + tamano_sublista] for i in range(0, len(palabras), tamano_sublista)]
            return len(palabras), matriz
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")
        return 0, []
    except (IndexError, ValueError):
        print("Error al leer el tamaño de la sublista desde la fila 4.")
        return 0, []

def procesar_carpeta_matrices():
    # Definir rutas de carpetas
    carpeta_origen = r"D:\python_suba\Matrix list"
    carpeta_destino_excel = r"D:\python_suba\Sorted matrices"
    carpeta_destino_txt = r"C:\Users\USS\Desktop\python_suba\Sorted Matrices TEXT"
    
    # Crear carpetas de destino si no existen
    if not os.path.exists(carpeta_destino_excel):
        os.makedirs(carpeta_destino_excel)
        print(f"Carpeta {carpeta_destino_excel} creada.")
    
    if not os.path.exists(carpeta_destino_txt):
        os.makedirs(carpeta_destino_txt)
        print(f"Carpeta {carpeta_destino_txt} creada.")
    
    # Procesar cada archivo en la carpeta de origen
    for archivo in os.listdir(carpeta_origen):
        if archivo.endswith(".atsp"):  # Solo procesar archivos .atsp
            ruta_completa = os.path.join(carpeta_origen, archivo)
            print(f"\nProcesando archivo: {archivo}")
            
            # Procesar el archivo
            total_palabras, matriz_palabras = contar_palabras_y_almacenar_en_matriz(ruta_completa)
            print(f"El archivo contiene {total_palabras} palabras.")
            
            # Generar nombre para los archivos de salida
            nombre_base = os.path.splitext(archivo)[0]
            
            # Guardar la matriz en Excel
            ruta_salida_excel = os.path.join(carpeta_destino_excel, nombre_base + "_sorted.xlsx")
            matriz_a_excel(matriz_palabras, ruta_salida_excel)
            
            # Guardar la matriz en TXT
            ruta_salida_txt = os.path.join(carpeta_destino_txt, nombre_base + "_sorted.txt")
            matriz_a_txt(matriz_palabras, ruta_salida_txt)

if __name__ == "__main__":
    procesar_carpeta_matrices()
    print("\nProceso completado.")