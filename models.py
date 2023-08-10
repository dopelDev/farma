from sqlalchemy import create_engine, Column, ForeignKey
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import relationship, Session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Medicamento(Base):
    __tablename__ = 'medicamentos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    dosis = Column(String)
    frecuencia = Column(String)
    cantidad_actual = Column(Integer)
    cantidad_optima = Column(Integer)
    demanda_anual = Column(Integer)

    transacciones = relationship('Transaccion', back_populates='medicamento')

class Paciente(Base):
    __tablename__ = 'pacientes'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    enfermedad = Column(String)
    alergias = Column(String)

    transacciones = relationship('Transaccion', back_populates='paciente')

class Transaccion(Base):
    __tablename__ = 'transacciones'
    id = Column(Integer, primary_key=True)
    paciente_id = Column(Integer, ForeignKey('pacientes.id'))
    medicamento_id = Column(Integer, ForeignKey('medicamentos.id'))
    cantidad = Column(Integer)

    paciente = relationship('Paciente', back_populates='transacciones')
    medicamento = relationship('Medicamento', back_populates='transacciones')

# create engine
engine = create_engine('sqlite:///farmacia.db', echo=True)
