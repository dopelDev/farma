def calcular_demanda_total(medicamentos):
    demanda_total = sum(medicamento['demanda_anual'] for medicamento in medicamentos)
    return demanda_total

def analisis_abc(medicamentos):
    demanda_total = calcular_demanda_total(medicamentos)

    for medicamento in medicamentos:
        valor_inventario = medicamento['valor_inventario']
        demanda_anual = medicamento['demanda_anual']
        porcentaje_demanda = (demanda_anual / demanda_total) * 100

        if porcentaje_demanda >= 80:
            medicamento['categoria'] = "A"
        elif porcentaje_demanda >= 15:
            medicamento['categoria'] = "B"
        else:
            medicamento['categoria'] = "C"

def verificar_estado_stock(medicamentos):
    for medicamento in medicamentos:
        nombre = medicamento['nombre']
        cantidad_actual = medicamento['cantidad_actual']

        if medicamento['categoria'] == "A":
            umbral_sobrestock = 0.3
            umbral_desabastecimiento = 0.1
        elif medicamento['categoria'] == "B":
            umbral_sobrestock = 0.2
            umbral_desabastecimiento = 0.15
        else:
            umbral_sobrestock = 0.1
            umbral_desabastecimiento = 0.2

        cantidad_optima = medicamento['demanda_anual'] * (1 + umbral_sobrestock)
        cantidad_minima = medicamento['demanda_anual'] * (1 - umbral_desabastecimiento)

        if cantidad_actual > cantidad_optima:
            estado = "Sobrestock"
        elif cantidad_actual < cantidad_minima:
            estado = "Desabastecimiento"
        else:
            estado = "Normostock"

        print(f"{nombre}: {estado}")

# Ejemplo de lista de medicamentos con sus niveles actuales de inventario, valor de inventario y demanda anual
medicamentos_ejemplo = [
    {"nombre": "Medicamento A", "cantidad_actual": 200, "valor_inventario": 5000, "demanda_anual": 1000},
    {"nombre": "Medicamento B", "cantidad_actual": 80, "valor_inventario": 2000, "demanda_anual": 800},
    {"nombre": "Medicamento C", "cantidad_actual": 120, "valor_inventario": 3000, "demanda_anual": 400},
    # Agrega más medicamentos aquí
]

analisis_abc(medicamentos_ejemplo)
verificar_estado_stock(medicamentos_ejemplo)
