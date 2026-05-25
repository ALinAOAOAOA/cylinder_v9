# Вычисление площади полной поверхности цилиндра
# Вариант № 9: S = 2 * π * R * H + 2 * π * R²  (π = 3.14)
# Автор: Дотдаева Алина Группа: ИСиП-331

import tkinter as tk
from tkinter import messagebox

# Вычислительный модуль 
def calculate(R: float, H: float) -> tuple:
    """
    Вычисляет площадь полной поверхности цилиндра.
    Параметры: R — радиус основания (м), H — высота (м).
    Возвращает: (S_боковая, S_основания, S_полная) в м².
    """
    PI = 3.14
    S_lateral = 2 * PI * R * H
    S_bases   = 2 * PI * R ** 2
    S_total   = S_lateral + S_bases
    return S_lateral, S_bases, S_total
  
# Модуль валидации 
def validate_input(value_str: str, field_name: str) -> float | None:
    """
    Проверяет строку на корректность числового ввода.
    Возвращает float при успехе или None при ошибке.
    """
    try:
        value = float(value_str.replace(',', '.'))
    except ValueError:
        messagebox.showerror(
            "Ошибка ввода",
            f"Поле «{field_name}»: введите числовое значение.\n"
            f"Пример корректного ввода: 3  или  2.5"
        )
        return None
    if value <= 0:
        messagebox.showerror(
            "Ошибка ввода",
            f"Поле «{field_name}»: значение должно быть\n"
            f"положительным числом, большим нуля."
        )
        return None
    return value

# Главный класс приложения
class CylinderApp:
    """Главный класс графического приложения."""

    BG        = "#f0f4f8"
    ACCENT    = "#2563eb"
    ACCENT_H  = "#1d4ed8"
    SUCCESS   = "#16a34a"
    ERROR_CLR = "#dc2626"
    TEXT      = "#1e293b"
    CARD      = "#ffffff"
    BORDER    = "#cbd5e1"
    FONT_MAIN = ("Segoe UI", 11)
    FONT_HEAD = ("Segoe UI", 13, "bold")
    FONT_TITLE= ("Segoe UI", 15, "bold")
    FONT_MONO = ("Consolas", 11)
    FONT_RES  = ("Consolas", 12, "bold")

    def __init__(self, root: tk.Tk):
        self.root = root
        self._setup_window()
        self._build_ui()

    # Настройка окна
    def _setup_window(self):
        self.root.title("Площадь поверхности цилиндра — вариант № 9")
        self.root.geometry("520x620")
        self.root.resizable(False, False)
        self.root.configure(bg=self.BG)
        # Центрируем окно на экране
        self.root.update_idletasks()
        w = self.root.winfo_width()
        h = self.root.winfo_height()
        x = (self.root.winfo_screenwidth()  - w) // 2
        y = (self.root.winfo_screenheight() - h) // 2
        self.root.geometry(f"+{x}+{y}")

    #Построение интерфейса 
    def _build_ui(self):
        # Заголовок
        header = tk.Frame(self.root, bg=self.ACCENT, pady=16)
        header.pack(fill="x")
        tk.Label(
            header,
            text="Площадь поверхности цилиндра",
            font=self.FONT_TITLE,
            bg=self.ACCENT, fg="white"
        ).pack()
        tk.Label(
            header,
            text="S = 2 × π × R × H  +  2 × π × R²     (π = 3,14)",
            font=("Segoe UI", 10),
            bg=self.ACCENT, fg="#bfdbfe"
        ).pack(pady=(4, 0))

        # Карточка ввода
        card_in = tk.Frame(self.root, bg=self.CARD, bd=0,
                           highlightthickness=1,
                           highlightbackground=self.BORDER)
        card_in.pack(fill="x", padx=20, pady=(20, 0))

        tk.Label(card_in, text="Введите параметры цилиндра",
                 font=self.FONT_HEAD, bg=self.CARD, fg=self.TEXT,
                 anchor="w").pack(fill="x", padx=16, pady=(14, 6))

        # Поле R
        self._make_field(card_in, "Радиус основания  R (м):", "r_var",
                         "Например: 3  или  2.5")
        # Поле H
        self._make_field(card_in, "Высота цилиндра  H (м):", "h_var",
                         "Например: 5  или  7.2")

        # Кнопки
        btn_frame = tk.Frame(card_in, bg=self.CARD)
        btn_frame.pack(fill="x", padx=16, pady=(10, 16))

        self.btn_calc = tk.Button(
            btn_frame,
            text="  Вычислить  ",
            font=("Segoe UI", 11, "bold"),
            bg=self.ACCENT, fg="white",
            activebackground=self.ACCENT_H, activeforeground="white",
            relief="flat", cursor="hand2", pady=8,
            command=self._on_calculate
        )
        self.btn_calc.pack(side="left", padx=(0, 8))

        btn_clear = tk.Button(
            btn_frame,
            text="  Очистить  ",
            font=("Segoe UI", 11),
            bg=self.BORDER, fg=self.TEXT,
            activebackground="#94a3b8", activeforeground="white",
            relief="flat", cursor="hand2", pady=8,
            command=self._on_clear
        )
        btn_clear.pack(side="left")

        # Карточка результата
        card_res = tk.Frame(self.root, bg=self.CARD, bd=0,
                            highlightthickness=1,
                            highlightbackground=self.BORDER)
        card_res.pack(fill="x", padx=20, pady=(14, 0))

        tk.Label(card_res, text="Результаты вычисления",
                 font=self.FONT_HEAD, bg=self.CARD, fg=self.TEXT,
                 anchor="w").pack(fill="x", padx=16, pady=(14, 6))

        # Метки результатов
        self.res_vars = {}
        fields = [
            ("r_disp",  "Радиус R:"),
            ("h_disp",  "Высота H:"),
            ("s_lat",   "Боковая поверхность:"),
            ("s_bas",   "Площадь оснований:"),
            ("s_total", "Площадь полная S:"),
        ]
        for key, label in fields:
            row = tk.Frame(card_res, bg=self.CARD)
            row.pack(fill="x", padx=16, pady=2)
            tk.Label(row, text=label, font=self.FONT_MAIN,
                     bg=self.CARD, fg="#64748b", width=24,
                     anchor="w").pack(side="left")
            var = tk.StringVar(value="—")
            self.res_vars[key] = var
            color = self.SUCCESS if key == "s_total" else self.TEXT
            font  = self.FONT_RES if key == "s_total" else self.FONT_MONO
            tk.Label(row, textvariable=var, font=font,
                     bg=self.CARD, fg=color,
                     anchor="w").pack(side="left")

        tk.Frame(card_res, bg=self.CARD, height=12).pack()

        # Статусная строка
        self.status_var = tk.StringVar(value="Введите данные и нажмите «Вычислить»")
        status_bar = tk.Label(
            self.root,
            textvariable=self.status_var,
            font=("Segoe UI", 10), bg="#e2e8f0", fg="#475569",
            anchor="w", padx=12, pady=6
        )
        status_bar.pack(fill="x", side="bottom")

        # Подсказка горячей клавиши
        self.root.bind("<Return>", lambda e: self._on_calculate())

    def _make_field(self, parent, label_text, var_name, placeholder):
        frame = tk.Frame(parent, bg=self.CARD)
        frame.pack(fill="x", padx=16, pady=4)
        tk.Label(frame, text=label_text, font=self.FONT_MAIN,
                 bg=self.CARD, fg=self.TEXT, width=26,
                 anchor="w").pack(side="left")
        var = tk.StringVar()
        setattr(self, var_name, var)
        entry = tk.Entry(
            frame, textvariable=var,
            font=self.FONT_MONO, width=14,
            relief="solid", bd=1,
            highlightthickness=1,
            highlightcolor=self.ACCENT,
            highlightbackground=self.BORDER
        )
        entry.pack(side="left", ipady=5)
        tk.Label(frame, text=placeholder, font=("Segoe UI", 9),
                 bg=self.CARD, fg="#94a3b8").pack(side="left", padx=8)

    # Обработчики событий
    def _on_calculate(self):
        R = validate_input(self.r_var.get().strip(), "Радиус R")
        if R is None:
            return
        H = validate_input(self.h_var.get().strip(), "Высота H")
        if H is None:
            return

        S_lat, S_bas, S_total = calculate(R, H)

        self.res_vars["r_disp"].set(f"{R} м")
        self.res_vars["h_disp"].set(f"{H} м")
        self.res_vars["s_lat"].set(f"{S_lat:.2f} м²")
        self.res_vars["s_bas"].set(f"{S_bas:.2f} м²")
        self.res_vars["s_total"].set(f"{S_total:.2f} м²")

        self.status_var.set(
            f"✓  Расчёт выполнен успешно  |  R = {R} м,  H = {H} м  |  S = {S_total:.2f} м²"
        )

    def _on_clear(self):
        self.r_var.set("")
        self.h_var.set("")
        for key in self.res_vars:
            self.res_vars[key].set("—")
        self.status_var.set("Поля очищены. Введите новые данные.")


# Точка входа 
if __name__ == "__main__":
    root = tk.Tk()
    app  = CylinderApp(root)
    root.mainloop()
