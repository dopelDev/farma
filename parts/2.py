def ajustar_stock(medicamentos):
    for medicamento in medicamentos:
        nombre = medicamento['nombre']
        cantidad_actual = medicamento['cantidad_actual']
        cantidad_optima = medicamento['cantidad_optima']
        demanda_historica = medicamento['demanda_historica']

        if cantidad_actual > cantidad_optima:
            excedente = cantidad_actual - cantidad_optima
            print(f"Kaizen: Reduciendo el sobrestock de {nombre} en {excedente} unidades.")
            medicamento['cantidad_actual'] = cantidad_optima

        elif cantidad_actual < cantidad_optima and cantidad_actual > demanda_historica:
            faltante = cantidad_optima - cantidad_actual
            print(f"Kaizen: Ajustando el inventario de {nombre} para evitar desabastecimiento.")
            medicamento['cantidad_actual'] = cantidad_optima

        elif cantidad_actual <= demanda_historica:
            print(f"Kaizen: Detectado desabastecimiento de {nombre}. Tomar medidas para reabastecer.")

# Ejemplo de lista de medicamentos con sus niveles actuales de inventario, cantidad óptima y demanda histórica
medicamentos_ejemplo = [
    {"nombre": "Medicamento A", "cantidad_actual": 200, "cantidad_optima": 150, "demanda_historica": 50},
    {"nombre": "Medicamento B", "cantidad_actual": 80, "cantidad_optima": 100, "demanda_historica": 70},
    {"nombre": "Medicamento C", "cantidad_actual": 120, "cantidad_optima": 180, "demanda_historica": 90},
    # Agrega más medicamentos aquí
]

ajustar_stock(medicamentos_ejemplo)

