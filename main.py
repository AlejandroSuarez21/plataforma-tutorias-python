import tkinter as tk
from tkinter import messagebox
import datos

def registrar_tutor():
    nombre = entry_tutor.get()
    materia = entry_materia.get()

    if nombre == "" or materia == "":
        messagebox.showwarning("Error","Complete los campos")
        return

    datos.agregar_tutor(nombre,materia)
    messagebox.showinfo("Listo","Tutor registrado")

def registrar_estudiante():
    nombre = entry_estudiante.get()

    if nombre == "":
        messagebox.showwarning("Error","Ingrese nombre")
        return

    datos.agregar_estudiante(nombre)
    messagebox.showinfo("Listo","Estudiante registrado")

def ver_tutores():
    lista_tutores.delete(0,tk.END)

    for t in datos.obtener_tutores():
        lista_tutores.insert(tk.END,t[0]+" - "+t[1])

def buscar_materia():
    materia = entry_buscar.get()

    lista_tutores.delete(0, tk.END)

    resultado = datos.buscar_por_materia(materia)

    for t in resultado:
        lista_tutores.insert(tk.END, t[0] + " - " + t[1])

def agendar():
    estudiante = entry_estudiante_tutoria.get()
    tutor = entry_tutor_tutoria.get()
    materia = entry_materia_tutoria.get()

    datos.agendar_tutoria(estudiante,tutor,materia)

    messagebox.showinfo("Correcto","Tutoría agendada")


ventana = tk.Tk()
ventana.title("Sistema de Tutorías")
ventana.geometry("450x600")

tk.Label(ventana,text="PLATAFORMA DE TUTORÍAS",font=("Arial",16)).pack(pady=10)

# REGISTRAR TUTOR

tk.Label(ventana,text="Registrar Tutor").pack()

entry_tutor = tk.Entry(ventana)
entry_tutor.pack()

entry_materia = tk.Entry(ventana)
entry_materia.pack()

tk.Button(ventana,text="Registrar Tutor",command=registrar_tutor).pack(pady=5)

# REGISTRAR ESTUDIANTE

tk.Label(ventana,text="Registrar Estudiante").pack()

entry_estudiante = tk.Entry(ventana)
entry_estudiante.pack()

tk.Button(ventana,text="Registrar Estudiante",command=registrar_estudiante).pack(pady=5)

# VER TUTORES

tk.Label(ventana,text="Tutores disponibles").pack()

lista_tutores = tk.Listbox(ventana)
lista_tutores.pack(pady=5)

tk.Button(ventana,text="Mostrar Tutores",command=ver_tutores).pack()

# BUSCAR POR MATERIA

tk.Label(ventana,text="Buscar tutor por materia").pack()

entry_buscar = tk.Entry(ventana)
entry_buscar.pack()

tk.Button(ventana,text="Buscar",command=buscar_materia).pack()

# AGENDAR TUTORIA

tk.Label(ventana,text="Agendar Tutoría").pack()

entry_estudiante_tutoria = tk.Entry(ventana)
entry_estudiante_tutoria.pack()

entry_tutor_tutoria = tk.Entry(ventana)
entry_tutor_tutoria.pack()

entry_materia_tutoria = tk.Entry(ventana)
entry_materia_tutoria.pack()

tk.Button(ventana,text="Agendar",command=agendar).pack(pady=10)

ventana.mainloop()
