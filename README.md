# Farma
**Author** Priscilla

### Models.py
**1. Tabla: medicamentos**

| id (PK) | nombre | dosis | frecuencia | cantidad_actual | cantidad_optima | demanda_anual |
|---------|--------|-------|------------|-----------------|-----------------|---------------|
| INT     | STRING | STRING| STRING     | INT             | INT             | INT           |

Relación:
- 1 medicamento puede tener múltiples transacciones.

**2. Tabla: pacientes**

| id (PK) | nombre  | enfermedad | alergias |
|---------|---------|------------|----------|
| INT     | STRING  | STRING     | STRING   |

Relación:
- 1 paciente puede tener múltiples transacciones.

**3. Tabla: transacciones**

| id (PK) | paciente_id (FK) | medicamento_id (FK) | cantidad |
|---------|------------------|---------------------|----------|
| INT     | INT              | INT                 | INT      |

Relaciones:
- Una transacción está asociada a 1 paciente.
- Una transacción está asociada a 1 medicamento.

**Las siglas "PK" y "FK" significan "Primary Key" y "Foreign Key" respectivamente. Estas claves son esenciales para establecer y mantener las relaciones entre las tablas.**
