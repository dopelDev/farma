def calcular_sor(stock_out_count, request_count):
    return (stock_out_count / request_count) * 100

def calcular_it(demanda_anual, promedio_inventario):
    return demanda_anual / promedio_inventario

def calcular_fr(stock_out_count, request_count):
    return ((request_count - stock_out_count) / request_count) * 100

def calcular_doi(promedio_inventario, demanda_diaria):
    return promedio_inventario / demanda_diaria

def determinar_estado_stock(sor, it, fr, doi):
    if sor > 10:
        estado = "Desabastecimiento"
    elif it < 2:
        estado = "Sobrestock"
    else:
        estado = "Normostock"
    return estado

# Ejemplo de datos sobre medicamentos y solicitudes
demanda_anual_med_a = 500
inventario_inicial_med_a = 100
inventario_final_med_a = 200
stock_out_med_a = 10
solicitudes_med_a = 150

# Calculamos indicadores logísticos para el medicamento A
promedio_inventario_med_a = (inventario_inicial_med_a + inventario_final_med_a) / 2
sor_med_a = calcular_sor(stock_out_med_a, solicitudes_med_a)
it_med_a = calcular_it(demanda_anual_med_a, promedio_inventario_med_a)
fr_med_a = calcular_fr(stock_out_med_a, solicitudes_med_a)
doi_med_a = calcular_doi(promedio_inventario_med_a, demanda_anual_med_a / 365)  # Suponiendo demanda diaria

# Determinamos el estado de inventario del medicamento A
estado_med_a = determinar_estado_stock(sor_med_a, it_med_a, fr_med_a, doi_med_a)

print(f"Medicamento A - Estado de inventario: {estado_med_a}")
