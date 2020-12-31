import pandas as pd
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import scipy.optimize as optimize
import numpy as np

from settings import curve_fit_parameter_settings
from models.ST_D_L import ST_D_L
from models.InterST_D_L import InterST_D_L
from models.InterDE_D_L import InterDE_D_L

DF = pd.read_csv('data/Riess1998_DL_Data.csv')

x = DF['ExpFact']
d = DF['D_L']
ed = DF['Err_D_L']

# Enforce non-zero error to avoid NaN in least squares resulting as product of inf and 0
ed.mask(ed == 0, 1e-9, inplace=True)


root = tk.Tk()


models = [
    ST_D_L,
    InterST_D_L,
    InterDE_D_L,
    # 'logDE_mag',
    # 'logInterST_mag',
    # 'logST_mag'
]

############################
# Model selector
labelTop = tk.Label(root, text = "Model")
labelTop.pack(side=tk.LEFT)

modelSelector = ttk.Combobox(
    root,
    values=[model.__name__ for model in models],
    state='readonly'
)
modelSelector.current(0)
modelSelector.pack(side=tk.LEFT)
modelSelector.bind("<<ComboboxSelected>>", run)

############################
# Plot
figure = plt.Figure(figsize=(6,5), dpi=100)
ax = figure.add_subplot(111)
chart_type = FigureCanvasTkAgg(figure, root)
chart_type.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)


############################
def run():
    model = models[modelSelector.current()]

    ax.clear()
    ax.errorbar(x, d, ed, fmt='.', label='data', capsize=5)
    ax.autoscale(enable=True)

    popt, pcov = optimize.curve_fit(model, x, d, sigma=ed, **curve_fit_parameter_settings)
    xf = np.linspace(x.min(), x.max(), num=50)
    ax.plot(xf, model(xf, *popt), 'g--',
            label='fit: Hubble=%5.3f, Matter=%5.3f' % (popt[0], popt[1]))

    ax.set_title('Model: %s' % (model.__name__))
    ax.set_xlabel('Expansion factor')
    ax.set_ylabel('D_L')
    ax.legend()
    figure.canvas.draw()
    print("updated!")

run()
root.mainloop()
