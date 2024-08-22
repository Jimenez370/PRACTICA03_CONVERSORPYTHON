from cProfile import label
import tkinter as tk
from tkinter import BUTT, Button, Entry, ttk
from traceback import clear_frames

def Celsius_a_Fahrenheit():
    try:        
        Celsius = float(entry_Celsius.get())
        Fahrenheit = (Celsius * 9 / 5) + 32
        entry_Fahrenheit.delete(0, tk.END)
        entry_Fahrenheit.insert(0, str(Fahrenheit))
    except ValueError:
        entry_Fahrenheit.delete(0, tk.END)
        entry_Fahrenheit.insert(0, "invalid input ")
 
def Fahrenheit_a_Celsius():
    try:
        Fahrenheit = float(entry_Fahrenheit.get())
        Celsius = 5.0 / 9.0 * (Fahrenheit - 32)
        entry_Celsius.delete(0, tk.END)
        entry_Celsius.insert(0, str(Celsius))
    except ValueError:
        entry_Celsius.delete(0, tk.END)
        entry_Celsius.insert(0, " invalid input ")

def Clear_Fields():
    entry_Celsius.delete(0, tk.END)
    entry_Fahrenheit.delete(0, tk.END)
    entry_Celsius.insert(0, " 0.0 ")
    entry_Fahrenheit.insert(0, " 0.0 ")
root = tk.Tk()
root.title(" Convertido de Grados ")

label_Celsius = ttk.Label(root, text=" Celsius: ")
label_Celsius.grid(column=0, row=0, padx=10, pady=10)

entry_Celsius = ttk.Entry(root)
entry_Celsius.grid(column=1, row=0, padx=10, pady=10)

label_Fahrenheti = ttk.Label(root, text=" Fahrenheit: ")
label_Fahrenheti.grid(column=0, row=1, padx=10, pady=10)

entry_Fahrenheit = ttk.Entry(root)
label_Fahrenheti.grid(column=1, row=1, padx=10, pady=10)

Button_convertir_a_Fahrenheit = ttk.Button(root, text=" Convertir a Fahrenheit ", command=Celsius_a_Fahrenheit)
Button_convertir_a_Fahrenheit.grid(column=0, row=2, padx=10, pady=10)

Button_convertir_a_Celsius = ttk.Button(root, text= " Convertir a Celsius ", command=Fahrenheit_a_Celsius)
Button_convertir_a_Celsius.grid(column=1, row=2, padx=10, pady=10)

Button_Clear = ttk.Button(root, text= " Limpiar ", command=Clear_Fields)
Button_Clear.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

root.mainloop()

