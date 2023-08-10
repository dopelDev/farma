def verificar_estado_stock(medicamentos, umbral_sobrestock, umbral_desabastecimiento):
    for medicamento in medicamentos:
        nombre = medicamento['nombre']
        cantidad_actual = medicamento['cantidad_actual']
        cantidad_optima = medicamento['cantidad_optima']

        if cantidad_actual > cantidad_optima + umbral_sobrestock:
            estado = "Sobrestock"
        elif cantidad_actual < cantidad_optima - umbral_desabastecimiento:
            estado = "Desabastecimiento"
        else:
            estado = "Normostock"

        print(f"{nombre}: {estado}")

# Ejemplo de lista de medicamentos con sus niveles actuales de inventario y cantidad óptima
medicamentos_ejemplo = [
    {"nombre": "Medicamento A", "cantidad_actual": 200, "cantidad_optima": 150},
    {"nombre": "Medicamento B", "cantidad_actual": 80, "cantidad_optima": 100},
    {"nombre": "Medicamento C", "cantidad_actual": 120, "cantidad_optima": 180},
    # Agrega más medicamentos aquí
]

# Definir umbrales para sobrestock y desabastecimiento
umbral_sobrestock = 50
umbral_desabastecimiento = 30

verificar_estado_stock(medicamentos_ejemplo, umbral_sobrestock, umbral_desabastecimiento)
