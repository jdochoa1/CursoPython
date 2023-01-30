import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de Grid')
ventana.iconbitmap('icono.ico')

entrada1 = ttk.Entry(ventana, width=30)
entrada1.grid(row=0, column=0)


ventana.mainloop()
