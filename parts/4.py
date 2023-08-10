def calcular_eoq(costo_pedido, costo_mantenimiento, demanda_anual):
    eoq = ((2 * costo_pedido * demanda_anual) / costo_mantenimiento) ** 0.5
    return eoq

def verificar_estado_stock(medicamentos, costo_pedido, costo_mantenimiento):
    for medicamento in medicamentos:
        nombre = medicamento['nombre']
        cantidad_actual = medicamento['cantidad_actual']
        demanda_anual = medicamento['demanda_anual']

        eoq = calcular_eoq(costo_pedido, costo_mantenimiento, demanda_anual)

        if cantidad_actual > eoq:
            estado = "Sobrestock"
        elif cantidad_actual < eoq:
            estado = "Desabastecimiento"
        else:
            estado = "Normostock"

        print(f"{nombre}: {estado}")

# Ejemplo de lista de medicamentos con sus niveles actuales de inventario y demanda anual
medicamentos_ejemplo = [
    {"nombre": "Medicamento A", "cantidad_actual": 200, "demanda_anual": 500},
    {"nombre": "Medicamento B", "cantidad_actual": 80, "demanda_anual": 200},
    {"nombre": "Medicamento C", "cantidad_actual": 120, "demanda_anual": 300},
    # Agrega más medicamentos aquí
]

# Definir costos de pedido y costo de mantenimiento
costo_pedido = 50  # Costo de realizar un pedido
costo_mantenimiento = 10  # Costo de mantener una unidad de inventario durante un año

verificar_estado_stock(medicamentos_ejemplo, costo_pedido, costo_mantenimiento)
