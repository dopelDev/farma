def calcular_nivel_servicio(stock_out_count, request_count):
    return (1 - (stock_out_count / request_count)) * 100

def calcular_inventario_promedio(inventario_inicial, inventario_final):
    return (inventario_inicial + inventario_final) / 2

def calcular_rotacion_inventario(demanda_anual, inventario_promedio):
    return demanda_anual / inventario_promedio

def determinar_estado_stock(nivel_servicio, rotacion_inventario):
    if nivel_servicio < 90:
        estado = "Desabastecimiento"
    elif rotacion_inventario < 2:
        estado = "Sobrestock"
    else:
        estado = "Normostock"
    return estado

# Ejemplo de datos sobre medicamentos y ventas
demanda_anual_med_a = 500
inventario_inicial_med_a = 100
inventario_final_med_a = 200
stock_out_med_a = 10
solicitudes_med_a = 150

# Calculamos los indicadores de gestión de almacén para el medicamento A
nivel_servicio_med_a = calcular_nivel_servicio(stock_out_med_a, solicitudes_med_a)
inventario_promedio_med_a = calcular_inventario_promedio(inventario_inicial_med_a, inventario_final_med_a)
rotacion_inventario_med_a = calcular_rotacion_inventario(demanda_anual_med_a, inventario_promedio_med_a)

# Determinamos el estado de inventario del medicamento A
estado_med_a = determinar_estado_stock(nivel_servicio_med_a, rotacion_inventario_med_a)

print(f"Medicamento A - Estado de inventario: {estado_med_a}")
