import tkinter as tk

window = tk.Tk()
window.title("Accident Detection System")
Label = tk.Label(window, text="Welcome to AI Accident Detection Dashboard")
Label.pack()
status_label = tk.Label(window, text="Current Status: Normal", fg="green", font=("Arial",16))
status_label.pack()
history_label = tk.Label(window, text="Incident History:", font=("Arial", 14))
history_label.pack()

history_box = tk.Text(window, height=10, width=50)
history_box.pack()

with open("incidents.csv", "r") as file:
    for line in file:
        history_box.insert(tk.END, line)
window.mainloop()