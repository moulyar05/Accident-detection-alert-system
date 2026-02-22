# Dashboard UI for AI Accident Detection System
# Shows current status and incident history

import tkinter as tk
import os

def start():
    window = tk.Tk()
    window.title("Accident Detection System")

    # Welcome message
    Label = tk.Label(window, text="Welcome to AI Accident Detection Dashboard")
    Label.pack()

    # Current status display
    status_label = tk.Label(window, text="Current Status: Normal", fg="green", font=("Arial",16))
    status_label.pack()

    # Incident history section
    history_label = tk.Label(window, text="Incident History:", font=("Arial", 14))
    history_label.pack()

    history_box = tk.Text(window, height=10, width=50)
    history_box.pack()

    # Load incidents from CSV if it exists
    if os.path.exists("incidents.csv"):
        with open("incidents.csv", "r") as file:
            for line in file:
                history_box.insert(tk.END, line)

    def refresh():
        history_box.delete("1.0", tk.END)  # clear box
        if os.path.exists("incidents.csv"):
            with open("incidents.csv", "r") as file:
                for line in file:
                    history_box.insert(tk.END, line)
        history_box.see(tk.END)  # auto scroll to bottom
        window.after(2000, refresh)  # run again after 2 seconds

    refresh()  # start the loop
    window.mainloop()