""" Ejercicio

Sistema para escuelas en sqlalchemy como parte del curso de "Bases de datos en Python"

Consigna: Se invita a crear un sistema para una escuela mediante SQLAlchemy. Este sistema permite registrar nuevos alumnos, profesores y cursos.

Un alumno es asignado a un curso y un curso puede tener asociado más de un profesor. Los profesores tienen un horario que indica cuando están en cada curso.

El horario asociará un curso y un profesor para un día de la semana (Lunes, Martes, Miércoles, Jueves, Viernes, Sábado, Domingo), una hora desde y una hora hasta.

El sistema permitirá exportar los alumnos que pertenecen a un curso, el horario de cada profesor y el horario del curso.

Se agradece los comentarios o sugerencias que puedan otorgar.

Nota: Se consideró que la entidad "horario" poseerá dos claves foráneas que harán referencia tanto a "Curso" como "Profesor" . Se anexa diagrama Entidad-Relación. Otra entidad a poseer una entidad con clave foránea es "alumno"

"""


from datetime import time
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Time
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///C:/Users/54346/Documents/frro-python-2024-04/sqlAlchemy/escuela.db')

class Curso(Base):
    __tablename__ = 'curso'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    alumnos = relationship("Alumno", back_populates="curso")
    horarios = relationship("Horario", back_populates="curso")

class Alumno(Base):
    __tablename__ = 'alumno'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    curso_id = Column(Integer, ForeignKey('curso.id'))
    curso = relationship("Curso", back_populates="alumnos")

class Profesor(Base):
    __tablename__ = 'profesor'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    horarios = relationship("Horario", back_populates="profesor")

class Horario(Base):
    __tablename__ = 'horario'
    id = Column(Integer, primary_key=True)
    curso_id = Column(Integer, ForeignKey('curso.id'))
    profesor_id = Column(Integer, ForeignKey('profesor.id'))
    dia_semana = Column(String)
    hora_desde = Column(Time)
    hora_hasta = Column(Time)
    curso = relationship("Curso", back_populates="horarios")
    profesor = relationship("Profesor", back_populates="horarios")

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

nuevo_curso = Curso(nombre='Matemáticas')
session.add(nuevo_curso)

nuevo_alumno = Alumno(nombre='Juan Pérez', curso=nuevo_curso)
session.add(nuevo_alumno)

nuevo_profesor = Profesor(nombre='Ana García')
session.add(nuevo_profesor)

# Usar datetime.time para crear objetos de tiempo correctamente
nuevo_horario = Horario(
    dia_semana='Lunes',
    hora_desde=time(8, 0),  # Hora desde las 8:00 AM
    hora_hasta=time(10, 0),  # Hora hasta las 10:00 AM
    curso=nuevo_curso,
    profesor=nuevo_profesor
)
session.add(nuevo_horario)

session.commit()
