# Вычисление площади полной поверхности цилиндра
# Вариант № 9: S = 2 * π * R * H + 2 * π * R²  (π = 3.14)
# Автор: Дотдаева Алина Группа: ИСиП-331

import tkinter as tk
from tkinter import messagebox

PI = 3.14

def вычислить():
    try:
        R = float(поле_r.get().replace(',', '.'))
        H = float(поле_h.get().replace(',', '.'))
    except ValueError:
        messagebox.showerror("Ошибка", "Введите числовые значения!")
        return

    if R <= 0 or H <= 0:
        messagebox.showerror("Ошибка", "Радиус и высота должны быть больше нуля!")
        return

    S_бок  = 2 * PI * R * H       # боковая поверхность
    S_осн  = 2 * PI * R ** 2      # два основания
    S_полн = S_бок + S_осн        # полная поверхность

    метка_рез.config(text=f"Боковая:  {S_бок:.2f} м²\n"
                          f"Основания: {S_осн:.2f} м²\n"
                          f"Полная:   {S_полн:.2f} м²")

def очистить():
    поле_r.delete(0, tk.END)
    поле_h.delete(0, tk.END)
    метка_рез.config(text="")

окно = tk.Tk()
окно.title("Площадь цилиндра — вариант 9")
окно.geometry("340x280")

tk.Label(окно, text="Площадь поверхности цилиндра", font=("Arial", 13, "bold")).pack(pady=10)
tk.Label(окно, text="S = 2πRH + 2πR²   (π = 3.14)", font=("Arial", 9)).pack()

frame = tk.Frame(окно)
frame.pack(pady=10)

tk.Label(frame, text="Радиус R (м):", font=("Arial", 11)).grid(row=0, column=0, sticky="w", pady=4)
поле_r = tk.Entry(frame, font=("Arial", 11), width=10)
поле_r.grid(row=0, column=1, pady=4)

tk.Label(frame, text="Высота H (м):", font=("Arial", 11)).grid(row=1, column=0, sticky="w", pady=4)
поле_h = tk.Entry(frame, font=("Arial", 11), width=10)
поле_h.grid(row=1, column=1, pady=4)

tk.Button(окно, text="Вычислить", font=("Arial", 11), command=вычислить).pack(pady=4)
tk.Button(окно, text="Очистить",  font=("Arial", 11), command=очистить).pack()

метка_рез = tk.Label(окно, text="", font=("Arial", 11), justify="left")
метка_рез.pack(pady=10)

окно.mainloop()
