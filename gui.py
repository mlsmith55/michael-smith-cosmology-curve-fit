import pandas as pd
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

data1 = {
    'Country': ['US','CA','GER','UK','FR'],
    'GDP_Per_Capita': [45000,42000,52000,49000,47000]
    }
df = pd.DataFrame(data1,columns=['Country','GDP_Per_Capita'])

root = tk.Tk()


figure = plt.Figure(figsize=(6,5), dpi=100)
ax = figure.add_subplot(111)
chart_type = FigureCanvasTkAgg(figure, root)
chart_type.get_tk_widget().pack()
df = df[['Country','GDP_Per_Capita']].groupby('Country').sum()
df.plot(kind='bar', legend=True, ax=ax)
ax.set_title('The Title for your chart')


root.mainloop()