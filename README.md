# Reto Técnico: Procesamiento de Transacciones Bancarias (CLI)

## Objetivo:

Desarrolla una aplicación de línea de comandos (CLI) que procese un archivo CSV con transacciones bancarias y genere un reporte que incluya:

- **Balance Final:**  
  Suma de los montos de las transacciones de tipo "Crédito" menos la suma de los montos de las transacciones de tipo "Débito".

- **Transacción de Mayor Monto:**  
  Identificar el ID y el monto de la transacción con el valor más alto.

- **Conteo de Transacciones:**  
  Número total de transacciones para cada tipo ("Crédito" y "Débito").

---

## Instrucciones de Ejecución

### Requisitos:
- Tener Python 3.x instalado en el equipo.

### Pasos para ejecutar la aplicación:

1. Clona o haz un fork del repositorio base disponible en:  
   `https://github.com/codeableorg/interbank-academy-25`

2. Verifica que el archivo **`data.csv`** esté en la misma carpeta que **`main.py`** (como ya tienes actualmente).

3. Abre una terminal en la carpeta del proyecto.

4. Ejecuta el siguiente comando:

```bash
python main.py
```

El resultado se mostrará directamente en la terminal.
_No es necesario instalar dependencias adicionales, ya que se utilizan únicamente librerías estándar de Python._

---

## Enfoque y Solución + Estructura del Proyecto

La solución se estructura de la siguiente manera:

- **Lectura del CSV:**  
  Se utiliza la librería estándar `csv.DictReader` para procesar cada línea como un diccionario.

- **Cálculo del balance final:**  
  Se suman los montos de las transacciones de tipo "Crédito" y se restan los de tipo "Débito".

- **Identificación de la transacción de mayor monto:**  
  Se utiliza la función `max()` para encontrar la transacción con el monto más alto.

- **Conteo de transacciones por tipo:**  
  Se utilizan expresiones generadoras para contar cuántas transacciones corresponden a cada tipo.

- **Simplicidad del código:**  
  La aplicación se mantiene sencilla y clara, utilizando funciones separadas para cada responsabilidad.

## Estructura del Proyecto

```
RetoTecnico/
│   .gitignore              # Archivo para ignorar archivos no deseados por Git
│   data.csv                # Archivo CSV con las transacciones bancarias
│   main.py                 # Script principal de la aplicación
│   README.md               # Documentación del proyecto (este archivo)
```

✅ Proyecto listo para ejecutar y entregar.
