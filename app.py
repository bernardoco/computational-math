import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from methods import euler, runge_kutta_4


def newton_cooling_law(t, T, T_ambiente=40, k=0.019):
    return -k*(T-T_ambiente)


def f(T, Ts, t, k=0.019):
    return Ts + (T-Ts)*np.exp(-k*t)

def mse(x1, x2):
    n = len(x1)
    s = 0
    for xi1, xi2 in zip(x1, x2):
        s += (xi1 - xi2)**2
    return s/n


def plot():
    t = float(t_input.get())
    t0 = float(t0_input.get())
    t_amb = float(t_amb_input.get())
    k = float(k_input.get())
    step = float(step_input.get())

    ts_rk, xs_rk, der_rk = runge_kutta_4(newton_cooling_law, t, 0, t0, step, t_amb, k)
    ts_euler, xs_euler = euler(newton_cooling_law, t, 0, t0, step, t_amb, k)

    exact = [f(t0, t_amb, x, k) for x in ts_rk]
    rk4_mse = mse(exact, xs_rk)
    mse_rk4.config(text=("Erro Medio Quadratico RK4: " + '{:0.3e}'.format(rk4_mse)))

    exact = [f(t0, t_amb, x, k) for x in ts_euler]
    euler_mse = mse(exact, xs_euler)
    mse_euler.config(text=("Erro Medio Quadratico Euler: " + '{:0.3e}'.format(euler_mse)))

    plt.close('all')

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,4))
    ax1.axhline(y=t_amb, color='purple', linestyle='--', label='Temp. Ambiente')
    ax1.plot(ts_rk, xs_rk, label='Runge Kutta 4')
    ax1.plot(ts_euler, xs_euler, label='Euler')

    ax1.legend(loc='best')
    ax1.set_xlabel('Tempo')
    ax1.set_ylabel('Temperatura')

    ax2.plot(xs_rk, der_rk)
    ax2.set_xlabel('T')
    ax2.set_ylabel('dT/dt')


    for widget in graph1.winfo_children():
       widget.destroy()

    canvas = FigureCanvasTkAgg(fig, graph1)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)


window = tk.Tk()

padx = 20
pady = 5

input_fields = tk.Frame(window)
t0_label = tk.Label(input_fields, text="Temperatura Inicial")
t0_label.config(width=30)
t0_label.config(font=('Arial', 11))
t0_input = tk.Entry(input_fields)
t0_label.grid(row=0, column=0, padx=padx, pady=pady)
t0_input.grid(row=1, column=0, padx=padx, pady=pady)

t_amb_label = tk.Label(input_fields, text="Temperatura Ambiente")
t_amb_label.config(width=30)
t_amb_label.config(font=('Arial', 11))
t_amb_input = tk.Entry(input_fields)
t_amb_label.grid(row=0, column=2, padx=padx, pady=pady)
t_amb_input.grid(row=1, column=2, padx=padx, pady=pady)

k_label = tk.Label(input_fields, text="k")
k_label.config(width=30)
k_label.config(font=('Arial', 11))
k_input = tk.Entry(input_fields)
k_label.grid(row=2, column=0, padx=padx, pady=pady)
k_input.grid(row=3, column=0, padx=padx, pady=pady)

t_label = tk.Label(input_fields, text="Tempo")
t_label.config(width=30)
t_label.config(font=('Arial', 11))
t_input = tk.Entry(input_fields)
t_label.grid(row=2, column=2, padx=padx, pady=pady)
t_input.grid(row=3, column=2, padx=padx, pady=pady)

step_label = tk.Label(input_fields, text="Passo")
step_label.config(width=30)
step_label.config(font=('Arial', 11))
step_input = tk.Entry(input_fields)
step_label.grid(row=4, column=1, padx=padx, pady=pady)
step_input.grid(row=5, column=1, padx=padx, pady=pady)

button = tk.Button(input_fields,
                   text="Plot",
                   command=plot)
button.grid(row=6, column=1, pady=pady*4)

graph1 = tk.Frame(window)


title = tk.Label(text="Troca de Calor")
title.config(width=40)
title.config(font=('Arial', 30))

title.pack(pady=30)
input_fields.pack()
graph1.pack()

errors = tk.Frame(window)

mse_rk4 = tk.Label(errors, text="Erro Medio Quadratico RK4:")
mse_euler = tk.Label(errors, text="Erro Medio Quadratico Euler:")

mse_rk4.config(width=30)
mse_rk4.config(font=('Arial', 11))
mse_euler.config(width=30)
mse_euler.config(font=('Arial', 11))

mse_rk4.grid(row=0, column=0, padx=padx, pady=pady)
mse_euler.grid(row=0, column=1, padx=padx, pady=pady)
errors.pack()


w = 1200
h = 850

ws = window.winfo_screenwidth() # width of the screen
hs = window.winfo_screenheight() # height of the screen

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

window.geometry('%dx%d+%d+%d' % (w, h, x, y))

window.title('Troca de Calor')
window.mainloop()
