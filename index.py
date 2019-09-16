import tkinter as tk
import webbrowser

app = tk.Tk()
app.title('Search')

search_label = tk.Label(app, text='Seach form')
search_label.grid(row=0, column=0)

text_field = tk.Entry(app, width=50)
text_field.grid(row=0, column=1)

app.mainloop()
