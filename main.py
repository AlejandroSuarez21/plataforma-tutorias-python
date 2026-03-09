import tkinter as tk
from tkinter import messagebox

tutores = []

def registrar_tutor():
    nombre = entrada_nombre.get()
    materia = entrada_materia.get()

    if nombre == "" or materia == "":
        messagebox.showwarning("Error", "Complete todos los campos")
        return

    tutores.append((nombre, materia))
    messagebox.showinfo("Éxito", "Tutor registrado")

    entrada_nombre.delete(0, tk.END)
    entrada_materia.delete(0, tk.END)

def mostrar_tutores():
    lista.delete(0, tk.END)

    for tutor in tutores:
        lista.insert(tk.END, tutor[0] + " - " + tutor[1])


ventana = tk.Tk()
ventana.title("Plataforma de Tutorías")
ventana.geometry("400x400")

titulo = tk.Label(ventana, text="Sistema de Tutorías", font=("Arial", 16))
titulo.pack(pady=10)

tk.Label(ventana, text="Nombre del tutor").pack()
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

tk.Label(ventana, text="Materia").pack()
entrada_materia = tk.Entry(ventana)
entrada_materia.pack()

boton_registrar = tk.Button(ventana, text="Registrar tutor", command=registrar_tutor)
boton_registrar.pack(pady=10)

boton_mostrar = tk.Button(ventana, text="Mostrar tutores", command=mostrar_tutores)
boton_mostrar.pack()

lista = tk.Listbox(ventana)
lista.pack(pady=10, fill=tk.BOTH, expand=True)

ventana.mainloop()
