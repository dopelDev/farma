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
