tutores = []
estudiantes = []
tutorias = []

def agregar_tutor(nombre, materia):
    tutores.append((nombre, materia))

def agregar_estudiante(nombre):
    estudiantes.append(nombre)

def obtener_tutores():
    return tutores

def buscar_por_materia(materia):
    resultado = []
    for tutor in tutores:
        if tutor[1].lower() == materia.lower():
            resultado.append(tutor)
    return resultado

def agendar_tutoria(estudiante, tutor, materia):
    tutorias.append((estudiante, tutor, materia))

    archivo = open("tutorias.txt","a")
    archivo.write(estudiante + "," + tutor + "," + materia + "\n")
    archivo.close()
