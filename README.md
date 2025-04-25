# **README - OrdenadorDeMatrices**  

## **📌 Descripción del Proyecto**  
**OrdenadorDeMatrices** es un proyecto en Python diseñado para procesar archivos de matrices (`.atsp`), extraer sus datos, ordenarlos y guardarlos en formatos **Excel (.xlsx)** y **texto (.txt)**.  

- **Entrada:** Archivos `.atsp` ubicados en `D:\python_suba\Matrix list`.  
- **Salida:**  
  - Matrices ordenadas en Excel → `D:\python_suba\Sorted matrices`.  
  - Matrices ordenadas en texto → `C:\Users\USS\Desktop\python_suba\Sorted Matrices TEXT`.  

---

## **⚙️ Funcionalidades**  
1. **Extracción de datos:**  
   - Lee archivos `.atsp` y extrae matrices numéricas (ignorando metadatos y "EOF").  
   - Detecta automáticamente el tamaño de las submatrices desde la línea 4 del archivo.  

2. **Procesamiento:**  
   - Convierte los datos en matrices bidimensionales.  
   - Excluye el token "EOF" si está presente.  

3. **Exportación:**  
   - Genera archivos Excel (`.xlsx`) con las matrices ordenadas.  
   - Genera archivos de texto (`.txt`) con formato legible (valores separados por tabulaciones).  

4. **Organización:**  
   - Crea carpetas de destino automáticamente si no existen.  

---

## **📂 Estructura del Proyecto**  
```
OrdenadorDeMatrices/  
├── Matrix_list/                  # Carpeta de entrada (archivos .atsp)  
├── Sorted_matrices/              # Matrices exportadas en Excel (.xlsx)  
├── Sorted_Matrices_TEXT/         # Matrices exportadas en texto (.txt)  
├── Comprobacion_dbg443/          # (Carpeta adicional, propósito no especificado)  
├── prueba_funcion/               # (Carpeta de pruebas)  
├── README.md                     # Este archivo  
└── ordenador_matrices.py         # Script principal  
```

---

## **🚀 Instalación y Uso**  
### **Requisitos**  
- Python 3.8+  
- Librerías:  
  ```bash
  pip install openpyxl
  ```

### **Ejecución**  
1. Coloca tus archivos `.atsp` en `Matrix_list/`.  
2. Ejecuta el script:  
   ```bash
   python ordenador_matrices.py
   ```
3. Los resultados se guardarán en:  
   - `Sorted_matrices/` (Excel).  
   - `Sorted_Matrices_TEXT/` (texto).  

---

## **📝 Ejemplo de Salida**  
### **Archivo de Texto (`_sorted.txt`)**  
```
23    21    23    4    14  
100   200   300   400  500  
```  
### **Archivo Excel (`_sorted.xlsx`)**  
| A  | B  | C  | D  | E  |  
|----|----|----|----|----|  
| 23 | 21 | 23 | 4  | 14 |  

---

## **🔍 Detalles Técnicos**  
- **Manejo de errores:**  
  - Verifica que los archivos `.atsp` existan.  
  - Valida el formato del tamaño de la matriz (línea 4).  

- **Eficiencia:**  
  - Procesa archivos grandes mediante lectura línea por línea.  

---

## **📜 Licencia**  
MIT License.  

---

## **📧 Contacto**  
¿Preguntas? ¡Abre un *issue* o contacta al desarrollador!  

--- 

✨ **¡Listo para ordenar matrices!** ✨
