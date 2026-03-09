import sqlite3

conexion = sqlite3.connect("tutorias.db")
cursor = conexion.cursor()

# Crear tablas
cursor.execute("CREATE TABLE IF NOT EXISTS tutores (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, materia TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS estudiantes (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS tutorias (id INTEGER PRIMARY KEY AUTOINCREMENT, estudiante TEXT, tutor TEXT, materia TEXT)")
conexion.commit()

def agregar_tutor(nombre, materia):
    cursor.execute("INSERT INTO tutores (nombre, materia) VALUES (?, ?)", (nombre, materia))
    conexion.commit()

def agregar_estudiante(nombre):
    cursor.execute("INSERT INTO estudiantes (nombre) VALUES (?)", (nombre,))
    conexion.commit()

def obtener_tutores():
    cursor.execute("SELECT nombre, materia FROM tutores")
    return cursor.fetchall()

def buscar_por_materia(materia):
    cursor.execute("SELECT nombre, materia FROM tutores WHERE LOWER(materia) = LOWER(?)", (materia,))
    return cursor.fetchall()

def agendar_tutoria(estudiante, tutor, materia):
    cursor.execute("INSERT INTO tutorias (estudiante, tutor, materia) VALUES (?, ?, ?)", (estudiante, tutor, materia))
    conexion.commit()
