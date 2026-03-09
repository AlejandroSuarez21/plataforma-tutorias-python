tutores = []
estudiantes = []
tutorias = []

def agregar_tutor(nombre, materia):
    tutores.append((nombre, materia))

def agregar_estudiante(nombre):
    estudiantes.append(nombre)

def obtener_tutores():
    return tutores

def agendar_tutoria(estudiante, tutor, materia):
    tutorias.append((estudiante, tutor, materia))
