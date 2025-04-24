import tkinter as tk

def click(symbol):
    entry.insert(tk.END, symbol)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Ділення на нуль!")
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Помилка")

root = tk.Tk()
root.title("Калькулятор")

entry = tk.Entry(root, width=25, font=("Arial", 16), borderwidth=2, relief="solid", justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Кнопки
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0
for btn in buttons:
    command = lambda x=btn: click(x) if x not in ('=',) else calculate()
    if btn == '=':
        b = tk.Button(root, text=btn, width=5, height=2, command=calculate)
    else:
        b = tk.Button(root, text=btn, width=5, height=2, command=command)
    b.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Кнопка очищення
clear_button = tk.Button(root, text="C", width=22, height=2, command=clear)
clear_button.grid(row=6, column=0, columnspan=4, padx=5, pady=5)

root.mainloop()
