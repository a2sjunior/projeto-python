import tkinter as tk
from tkinter import messagebox
import random
import time

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
campo_minado.py
Jogo Campo Minado com interface gráfica (tkinter).
Três níveis de dificuldade com tamanhos de tabuleiro pré-definidos.
"""


# Nome do assistente (conforme instruções internas, não exibido)
# GitHub Copilot

# Configurações de dificuldade: (cols, rows, mines)
DIFFICULTIES = {
    "Fácil (9x9, 10 minas)": (9, 9, 10),
    "Médio (16x16, 40 minas)": (16, 16, 40),
    "Difícil (30x16, 99 minas)": (30, 16, 99),
}


class Minesweeper:
    def __init__(self, root):
        self.root = root
        root.title("Campo Minado")
        self.top_frame = tk.Frame(root)
        self.top_frame.pack(padx=8, pady=8, anchor="w")

        # Difficulty selection
        self.difficulty_var = tk.StringVar(value=list(DIFFICULTIES.keys())[0])
        tk.Label(self.top_frame, text="Dificuldade:").pack(side="left")
        self.diff_menu = tk.OptionMenu(self.top_frame, self.difficulty_var, *DIFFICULTIES.keys(), command=self.restart)
        self.diff_menu.pack(side="left", padx=4)

        # Mine counter and timer
        self.mines_var = tk.StringVar(value="Minas: 0")
        tk.Label(self.top_frame, textvariable=self.mines_var, width=12).pack(side="left", padx=6)
        self.time_var = tk.StringVar(value="Tempo: 0s")
        tk.Label(self.top_frame, textvariable=self.time_var, width=12).pack(side="left", padx=6)

        # Restart button
        self.restart_button = tk.Button(self.top_frame, text="Reiniciar", command=self.restart)
        self.restart_button.pack(side="left", padx=4)

        # Board frame
        self.board_frame = tk.Frame(root)
        self.board_frame.pack(padx=8, pady=8)

        # Initialize state
        self.cells = []
        self.buttons = []
        self.mines = 0
        self.cols = 0
        self.rows = 0
        self.first_click = True
        self.start_time = None
        self.timer_job = None

        self.restart()

    def restart(self, *args):
        # Stop timer
        if self.timer_job:
            self.root.after_cancel(self.timer_job)
            self.timer_job = None
        self.start_time = None
        self.time_var.set("Tempo: 0s")
        self.first_click = True

        # Clear board frame
        for widget in self.board_frame.winfo_children():
            widget.destroy()

        # Read difficulty
        key = self.difficulty_var.get()
        self.cols, self.rows, self.mines = DIFFICULTIES.get(key, (9, 9, 10))
        self.mines_var.set(f"Minas: {self.mines}")

        # Prepare arrays
        self.cells = [[{'mine': False, 'adj': 0, 'revealed': False, 'flagged': False} for _ in range(self.cols)] for _ in range(self.rows)]
        self.buttons = [[None for _ in range(self.cols)] for _ in range(self.rows)]

        # Create buttons grid
        for r in range(self.rows):
            for c in range(self.cols):
                b = tk.Button(self.board_frame, width=2, height=1, relief="raised", bg="#ddd",
                              command=lambda rr=r, cc=c: self.on_left_click(rr, cc))
                b.bind("<Button-3>", lambda e, rr=r, cc=c: self.on_right_click(rr, cc))
                b.grid(row=r, column=c, padx=1, pady=1)
                self.buttons[r][c] = b

        # Adjust window size minimally
        self.root.update_idletasks()

    def place_mines(self, safe_r, safe_c):
        # Place mines ensuring the first clicked cell and neighbors are safe
        all_cells = [(r, c) for r in range(self.rows) for c in range(self.cols)]
        forbidden = {(safe_r, safe_c)}
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                rr, cc = safe_r + dr, safe_c + dc
                if 0 <= rr < self.rows and 0 <= cc < self.cols:
                    forbidden.add((rr, cc))
        choices = [pos for pos in all_cells if pos not in forbidden]
        mines_positions = random.sample(choices, self.mines)
        for (r, c) in mines_positions:
            self.cells[r][c]['mine'] = True

        # Compute adjacency counts
        for r in range(self.rows):
            for c in range(self.cols):
                if self.cells[r][c]['mine']:
                    self.cells[r][c]['adj'] = -1
                else:
                    cnt = 0
                    for dr in (-1, 0, 1):
                        for dc in (-1, 0, 1):
                            rr, cc = r + dr, c + dc
                            if 0 <= rr < self.rows and 0 <= cc < self.cols and self.cells[rr][cc]['mine']:
                                cnt += 1
                    self.cells[r][c]['adj'] = cnt

    def on_left_click(self, r, c):
        if self.cells[r][c]['flagged'] or self.cells[r][c]['revealed']:
            return
        if self.first_click:
            self.place_mines(r, c)
            self.first_click = False
            self.start_timer()
        cell = self.cells[r][c]
        if cell['mine']:
            # Reveal all mines and end game
            self.reveal_all_mines(trigger=(r, c))
            self.game_over(False)
            return
        self.reveal_cell(r, c)
        if self.check_win():
            self.game_over(True)

    def on_right_click(self, r, c):
        cell = self.cells[r][c]
        if cell['revealed']:
            return "break"
        cell['flagged'] = not cell['flagged']
        btn = self.buttons[r][c]
        if cell['flagged']:
            btn.config(text="🚩", fg="red")
        else:
            btn.config(text="", fg="black")
        # update remaining mines display (approx)
        flagged_count = sum(1 for rr in range(self.rows) for cc in range(self.cols) if self.cells[rr][cc]['flagged'])
        self.mines_var.set(f"Minas: {self.mines - flagged_count}")
        return "break"

    def reveal_cell(self, r, c):
        stack = [(r, c)]
        while stack:
            rr, cc = stack.pop()
            cell = self.cells[rr][cc]
            btn = self.buttons[rr][cc]
            if cell['revealed'] or cell['flagged']:
                continue
            cell['revealed'] = True
            btn.config(relief="sunken", bg="#bbb")
            if cell['adj'] > 0:
                color = self.color_for_number(cell['adj'])
                btn.config(text=str(cell['adj']), fg=color, disabledforeground=color)
            else:
                btn.config(text="")
                # append neighbors if zero
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        nr, nc = rr + dr, cc + dc
                        if 0 <= nr < self.rows and 0 <= nc < self.cols:
                            neighbor = self.cells[nr][nc]
                            if not neighbor['revealed'] and not neighbor['mine'] and not neighbor['flagged']:
                                stack.append((nr, nc))
            btn.config(state="disabled")

    def reveal_all_mines(self, trigger=None):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.cells[r][c]['mine']:
                    btn = self.buttons[r][c]
                    btn.config(text="💣", bg="#f88")
        # mark wrong flags
        for r in range(self.rows):
            for c in range(self.cols):
                cell = self.cells[r][c]
                if cell['flagged'] and not cell['mine']:
                    btn = self.buttons[r][c]
                    btn.config(text="X", bg="#faa")

    def check_win(self):
        for r in range(self.rows):
            for c in range(self.cols):
                cell = self.cells[r][c]
                if not cell['mine'] and not cell['revealed']:
                    return False
        return True

    def game_over(self, won):
        # Stop timer
        if self.timer_job:
            self.root.after_cancel(self.timer_job)
            self.timer_job = None
        # reveal all appropriately
        if won:
            for r in range(self.rows):
                for c in range(self.cols):
                    cell = self.cells[r][c]
                    btn = self.buttons[r][c]
                    if cell['mine']:
                        btn.config(text="🚩", bg="#bfb")
            messagebox.showinfo("Campo Minado", f"Parabéns! Você venceu em {self.time_var.get().split()[-1]}!")
        else:
            messagebox.showinfo("Campo Minado", "Você clicou numa mina! Fim de jogo.")
        # disable all buttons
        for r in range(self.rows):
            for c in range(self.cols):
                try:
                    self.buttons[r][c].config(state="disabled")
                except Exception:
                    pass

    def start_timer(self):
        self.start_time = time.time()
        self.update_timer()

    def update_timer(self):
        if self.start_time is None:
            return
        elapsed = int(time.time() - self.start_time)
        self.time_var.set(f"Tempo: {elapsed}s")
        self.timer_job = self.root.after(1000, self.update_timer)

    @staticmethod
    def color_for_number(n):
        colors = {
            1: "#0000FF",
            2: "#008200",
            3: "#FF0000",
            4: "#000084",
            5: "#840000",
            6: "#008284",
            7: "#000000",
            8: "#808080",
        }
        return colors.get(n, "#000000")


if __name__ == "__main__":
    root = tk.Tk()
    game = Minesweeper(root)
    root.mainloop()