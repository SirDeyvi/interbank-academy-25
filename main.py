# Importamos la librería estándar para trabajar con archivos CSV
import csv

# Función para leer las transacciones desde el archivo CSV
def leer_transacciones(nombre_archivo):
    transacciones = []
    # Abrimos el archivo CSV en modo lectura
    with open(nombre_archivo, newline='', encoding='utf-8') as archivo_csv:
        lector = csv.DictReader(archivo_csv)
        for fila in lector:
            # Convertimos los datos a los tipos adecuados y los almacenamos en la lista
            transacciones.append({
                'id': int(fila['id']),
                'tipo': fila['tipo'],
                'monto': float(fila['monto'])
            })
    return transacciones

# Función para calcular el balance final de las transacciones
def calcular_balance(transacciones):
    # Sumamos los montos de tipo 'Crédito' y restamos los de tipo 'Débito'
    creditos = sum(t['monto'] for t in transacciones if t['tipo'] == 'Crédito')
    debitos = sum(t['monto'] for t in transacciones if t['tipo'] == 'Débito')
    return creditos - debitos

# Función para encontrar la transacción con el monto más alto
def transaccion_mayor(transacciones):
    # Utilizamos la función max() con una función lambda para obtener la transacción con mayor monto
    mayor = max(transacciones, key=lambda t: t['monto'])
    return mayor

# Función para contar la cantidad de transacciones por tipo
def contar_transacciones(transacciones):
    # Contamos cuántas transacciones son de tipo 'Crédito' y cuántas son de tipo 'Débito'
    creditos = sum(1 for t in transacciones if t['tipo'] == 'Crédito')
    debitos = sum(1 for t in transacciones if t['tipo'] == 'Débito')
    return creditos, debitos

# Función principal que coordina la ejecución del programa
def main():
    # Nombre del archivo CSV que contiene las transacciones
    nombre_archivo = 'data.csv'

    # Leemos las transacciones desde el archivo
    transacciones = leer_transacciones(nombre_archivo)

    # Calculamos el balance final
    balance = calcular_balance(transacciones)

    # Obtenemos la transacción con el mayor monto
    mayor_transaccion = transaccion_mayor(transacciones)

    # Contamos las transacciones por tipo
    creditos, debitos = contar_transacciones(transacciones)

    # Mostramos el reporte en la terminal
    print("Reporte de Transacciones")
    print("-" * 40)
    print(f"Balance Final: {balance:.2f}")
    print(f"Transacción de Mayor Monto: ID {mayor_transaccion['id']} - {mayor_transaccion['monto']:.2f}")
    print(f"Conteo de Transacciones: Crédito: {creditos} Débito: {debitos}")

# Verificamos si este archivo es el programa principal y ejecutamos la función main
if __name__ == '__main__':
    main()
