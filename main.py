import tkinter as tk
from tkinter import messagebox


def add_digit(digit):
    value = entry_calc.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    entry_calc['state'] = tk.NORMAL
    entry_calc.delete(0, tk.END)
    entry_calc.insert(0, value + digit)
    entry_calc['state'] = tk.DISABLED


def add_operation(operation):
    value = entry_calc.get()
    if value[-1] in ('-', '+', '/', '*'):
        value = value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value:
        calculate()
        value = entry_calc.get()
    entry_calc['state'] = tk.NORMAL
    entry_calc.delete(0, tk.END)
    entry_calc.insert(0, value + operation)
    entry_calc['state'] = tk.DISABLED


def calculate():
    value = entry_calc.get()
    if value[-1] in ('-', '+', '/', '*'):
        value = value + value[:-1]
    entry_calc['state'] = tk.NORMAL
    entry_calc.delete(0, tk.END)
    try:
        entry_calc.insert(0, eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo('Внимание', 'Нужно вводить только цифры! Вы ввели символы')
        entry_calc.insert(0, 0)
    except ZeroDivisionError:
        messagebox.showinfo('Внимание', 'Деление на ноль невозможно!')
        entry_calc.insert(0, 0)
    entry_calc['state'] = tk.DISABLED

def clear():
    entry_calc['state'] = tk.NORMAL
    entry_calc.delete(0, tk.END)
    entry_calc.insert(0, 0)
    entry_calc['state'] = tk.DISABLED


def make_digit_button(digit):
    return tk.Button(text=digit, bd=5, font=("Arial", 13), command=lambda: add_digit(digit))


def make_operation_button(operation):
    return tk.Button(text=operation, bd=5, font=("Arial", 13), fg="#960962", command=lambda: add_operation(operation))


def make_calc_button(operation):
    return tk.Button(text=operation, bd=5, font=("Arial", 13), fg="#960962", command=calculate)


def make_clear_button(operation):
    return tk.Button(text=operation, bd=5, font=("Arial", 13), fg="#960962", command=clear)


def press_key(event):
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in ('-', '+', '/', '*'):
        add_operation(event.char)
    elif event.char in ('=', '\r'):
        calculate()


root = tk.Tk()
x = int((root.winfo_screenwidth() - root.winfo_reqwidth()) / 2)
y = int((root.winfo_screenheight() - root.winfo_reqheight()) / 2)
root.geometry(f'240x280+{x}+{y}')
root['bg'] = '#4BB0E7'
root.title("Калькулятор")

root.bind('<Key>', press_key)

entry_calc = tk.Entry(root, justify=tk.RIGHT, font=("Arial", 15), width=15)
entry_calc.insert(0, '0')
entry_calc['state'] = tk.DISABLED
entry_calc.grid(row=0, column=0, columnspan=4, stick="we", padx=5, pady=5)

make_digit_button("1").grid(row=1, column=0, stick="wens", padx=5, pady=5)
make_digit_button("2").grid(row=1, column=1, stick="wens", padx=5, pady=5)
make_digit_button("3").grid(row=1, column=2, stick="wens", padx=5, pady=5)
make_digit_button("4").grid(row=2, column=0, stick="wens", padx=5, pady=5)
make_digit_button("5").grid(row=2, column=1, stick="wens", padx=5, pady=5)
make_digit_button("6").grid(row=2, column=2, stick="wens", padx=5, pady=5)
make_digit_button("7").grid(row=3, column=0, stick="wens", padx=5, pady=5)
make_digit_button("8").grid(row=3, column=1, stick="wens", padx=5, pady=5)
make_digit_button("9").grid(row=3, column=2, stick="wens", padx=5, pady=5)
make_digit_button("0").grid(row=4, column=0, stick="wens", padx=5, pady=5)

make_operation_button('+').grid(row=1, column=3, stick="wens", padx=5, pady=5)
make_operation_button('-').grid(row=2, column=3, stick="wens", padx=5, pady=5)
make_operation_button('*').grid(row=3, column=3, stick="wens", padx=5, pady=5)
make_operation_button('/').grid(row=4, column=3, stick="wens", padx=5, pady=5)

make_calc_button("=").grid(row=4, column=2, stick="wens", padx=5, pady=5)
make_clear_button("C").grid(row=4, column=1, stick="wens", padx=5, pady=5)

root.grid_columnconfigure(0, minsize=60)
root.grid_columnconfigure(1, minsize=60)
root.grid_columnconfigure(2, minsize=60)
root.grid_columnconfigure(3, minsize=60)
root.grid_rowconfigure(1, minsize=60)
root.grid_rowconfigure(2, minsize=60)
root.grid_rowconfigure(3, minsize=60)
root.grid_rowconfigure(4, minsize=60)

if __name__ == "__main__":
    root.mainloop()
