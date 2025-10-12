import tkinter as tk

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Calculadora simples com interface gráfica (Tkinter)


# Avalia expressões de forma básica (usa eval com ambiente restrito)
def safe_eval(expr):
    try:
        # Substituições para símbolos visuais
        expr = expr.replace('×', '*').replace('÷', '/').replace('^', '**')
        # Avalia sem builtins
        return str(eval(expr, {"__builtins__": None}, {}))
    except Exception:
        return "Erro"

class Calculadora:
    def __init__(self, root):
        self.root = root
        root.title("Calculadora")
        root.resizable(False, False)

        self.display = tk.Entry(root, font=("Arial", 24), borderwidth=4, relief="ridge", justify="right")
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)
        self.display.focus_set()

        buttons = [
            ('C', 1, 0), ('←', 1, 1), ('(', 1, 2), (')', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('÷', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('×', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('%', 5, 2), ('+', 5, 3),
            ('=', 6, 0, 4)
        ]

        for btn in buttons:
            text = btn[0]
            row = btn[1]
            col = btn[2]
            colspan = btn[3] if len(btn) == 4 else 1
            b = tk.Button(root, text=text, font=("Arial", 20), command=lambda t=text: self.on_click(t))
            b.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=2, pady=2)

        # Configure grid weight
        for i in range(7):
            root.grid_rowconfigure(i, weight=1)
        for j in range(4):
            root.grid_columnconfigure(j, weight=1)

        # Teclado
        root.bind("<Return>", lambda e: self.on_click('='))
        root.bind("<BackSpace>", lambda e: self.on_click('←'))
        root.bind("<Escape>", lambda e: self.on_click('C'))
        root.bind("<Key>", self.on_key)

    def on_click(self, char):
        if char == 'C':
            self.display.delete(0, tk.END)
        elif char == '←':
            current = self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(0, current[:-1])
        elif char == '=':
            expr = self.display.get()
            # tratando porcento: transforma "50%" em "(50/100)"
            expr = expr.replace('%', '/100')
            result = safe_eval(expr)
            self.display.delete(0, tk.END)
            self.display.insert(0, result)
        else:
            self.display.insert(tk.END, char)

    def on_key(self, event):
        allowed = "0123456789.+-*/()%^"
        ch = event.char
        if ch in allowed:
            # traduz * e / para símbolos padrão se quiser (mantém como está)
            self.display.insert(tk.END, ch)
        elif ch == '\r':
            self.on_click('=')
        # ignora outros

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()