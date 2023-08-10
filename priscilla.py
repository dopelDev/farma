1. import random

# Lista de medicamentos disponibles
medicamentos = [
    {"nombre": "Medicamento A", "dosis": "10 mg", "frecuencia": "12 horas"},
    {"nombre": "Medicamento B", "dosis": "5 mg", "frecuencia": "8 horas"},
    {"nombre": "Medicamento C", "dosis": "20 mg", "frecuencia": "24 horas"},
    # Agrega más medicamentos aquí
]

# Función para seleccionar una combinación de medicamentos aleatoria para el paciente
def seleccionar_combinacion_medicamentos():
    combinacion = random.sample(medicamentos, random.randint(1, len(medicamentos)))
    return combinacion

# Función para rotar los medicamentos del paciente
def rotar_medicamentos(paciente, dias_de_rotacion):
    print(f"Rotando medicamentos para el paciente {paciente['nombre']} cada {dias_de_rotacion} días.")
    for dia in range(dias_de_rotacion):
        combinacion_actual = seleccionar_combinacion_medicamentos()
        print(f"Día {dia + 1}: {', '.join(m['nombre'] for m in combinacion_actual)}")
    print("Rotación de medicamentos completada.\n")

# Ejemplo de paciente
paciente_1 = {"nombre": "Juan", "enfermedad": "Hipertensión", "alergias": []}

# Rotar medicamentos para el paciente durante 7 días
rotar_medicamentos(paciente_1, dias_de_rotacion=7)

2. import time

# Lista de medicamentos disponibles
medicamentos = [
    {"nombre": "Medicamento A", "dosis": "10 mg", "frecuencia": "12 horas"},
    {"nombre": "Medicamento B", "dosis": "5 mg", "frecuencia": "8 horas"},
    {"nombre": "Medicamento C", "dosis": "20 mg", "frecuencia": "24 horas"},
    # Agrega más medicamentos aquí
]

# Función para seleccionar una combinación de medicamentos aleatoria para el paciente
def seleccionar_combinacion_medicamentos():
    combinacion = random.sample(medicamentos, random.randint(1, len(medicamentos)))
    return combinacion

# Función para rotar los medicamentos del paciente con ANDON
def rotar_medicamentos_con_andon(paciente, dias_de_rotacion):
    print(f"Rotando medicamentos para el paciente {paciente['nombre']} cada {dias_de_rotacion} días.")
    for dia in range(dias_de_rotacion):
        combinacion_actual = seleccionar_combinacion_medicamentos()
        print(f"Día {dia + 1}: {', '.join(m['nombre'] for m in combinacion_actual)}")

        # Simulación de detección de problemas con ANDON
        problema_detectado = random.random() < 0.2  # 20% de probabilidad de detectar un problema
        if problema_detectado:
            print("¡Problema detectado! El paciente no tomó sus medicamentos correctamente.")
            # Aquí podrías enviar una notificación visual o auditiva para alertar al personal médico.

        time.sleep(1)  # Simulación de tiempo de rotación entre días

    print("Rotación de medicamentos completada.\n")

# Ejemplo de paciente
paciente_1 = {"nombre": "Juan", "enfermedad": "Hipertensión", "alergias": []}

# Rotar medicamentos para el paciente durante 7 días con ANDON
rotar_medicamentos_con_andon(paciente_1, dias_de_rotacion=7)

3. def verificar_estado_stock(medicamentos):
    for medicamento in medicamentos:
        nombre = medicamento['nombre']
        cantidad_actual = medicamento['cantidad_actual']
        cantidad_optima = medicamento['cantidad_optima']
        porcentaje_actual = (cantidad_actual / cantidad_optima) * 100

        if porcentaje_actual > 150:
            estado = "Sobrestock"
        elif porcentaje_actual >= 70:
            estado = "Normostock"
        else:
            estado = "Desabastecimiento"

        print(f"{nombre}: {estado}")

# Ejemplo de lista de medicamentos con sus niveles actuales de inventario y cantidad óptima
medicamentos_ejemplo = [
    {"nombre": "Medicamento A", "cantidad_actual": 200, "cantidad_optima": 100},
    {"nombre": "Medicamento B", "cantidad_actual": 80, "cantidad_optima": 120},
    {"nombre": "Medicamento C", "cantidad_actual": 150, "cantidad_optima": 200},
    # Agrega más medicamentos aquí
]

verificar_estado_stock(medicamentos_ejemplo)

4. import time

def verificar_estado_stock(medicamentos):
    for medicamento in medicamentos:
        nombre = medicamento['nombre']
        cantidad_actual = medicamento['cantidad_actual']
        cantidad_optima = medicamento['cantidad_optima']
        porcentaje_actual = (cantidad_actual / cantidad_optima) * 100

        if porcentaje_actual > 150:
            estado = "Sobrestock"
        elif porcentaje_actual >= 70:
            estado = "Normostock"
        else:
            estado = "Desabastecimiento"

            # Simulación de notificación ANDON para desabastecimiento
            print(f"¡ANDON activado! Desabastecimiento de {nombre} detectado.")

        print(f"{nombre}: {estado}")

# Ejemplo de lista de medicamentos con sus niveles actuales de inventario y cantidad óptima
medicamentos_ejemplo = [
    {"nombre": "Medicamento A", "cantidad_actual": 200, "cantidad_optima": 100},
    {"nombre": "Medicamento B", "cantidad_actual": 80, "cantidad_optima": 120},
    {"nombre": "Medicamento C", "cantidad_actual": 150, "cantidad_optima": 200},
    # Agrega más medicamentos aquí
]

while True:
    verificar_estado_stock(medicamentos_ejemplo)
    time.sleep(60)  # Verificar el estado de inventario cada 1 minuto
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
