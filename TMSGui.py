import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from TMSLogic import TMSLogic

class TMSGui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Task Manager")
        self.logic = TMSLogic()

        style = ttk.Style(self.root)
        style.configure("Strikethrough.TCheckbutton", foreground="gray", font=("Arial", 10, "overstrike"))

        self.root.geometry("600x400")

        self.entry = ttk.Entry(self.root, width=40)
        self.entry.pack()

        self.button = ttk.Button(self.root, text = " Add Task", command=self.add_task)
        self.button.pack()

        self.button = ttk.Button(self.root, text = " Delete Tasks", command=self.delete_tasks)
        self.button.pack()

        self.root.bind("<Return>", lambda e: self.add_task())



        self.task_frame = ttk.Frame(self.root) 
        self.task_frame.pack()

        self.chart_frame = ttk.Frame(self.root)
        self.chart_frame.pack()

        self.figure = Figure(figsize=(5,5))
        self.ax = self.figure.add_subplot(211)
        ax = self.figure.add_subplot(212)
        ax.text(0.5,0.5,"HI")

        self.piecanvas = FigureCanvasTkAgg(self.figure, self.chart_frame)
        self.piecanvas.get_tk_widget().pack()
        self.refresh_tasks()
        self.root.mainloop()

    def add_task(self):
        task = self.entry.get()
        self.logic.add_task(task)
        self.entry.delete(0,tk.END)
        print(self.logic.tasks)
        self.refresh_tasks()

    def refresh_tasks(self):
        for widget in self.task_frame.winfo_children():
            widget.destroy()

        for index, (task, done) in enumerate(self.logic.tasks):
            var = tk.BooleanVar(value=done)
            chk = ttk.Checkbutton(self.task_frame, text=task, variable=var, command= lambda idx = index: self.toggle_task(idx))
            style_name = "Strikethrough.TCheckbutton" if done else "TCheckbutton"
            chk.configure(style=style_name)
            chk.pack()
        self.update_piechart()

    def toggle_task(self, idx):
        self.logic.toggle_task(idx)
        print(self.logic.tasks)
        self.refresh_tasks()
        
    def update_piechart(self):
        self.ax.clear()
        if len(self.logic.tasks) == 0:
            self.ax.text(0.5,0.5, "No Tasks",ha="center", va= "center",fontsize=14)

        else:
            compleated = self.logic.completion_rate()
            self.ax.pie([compleated, 1 - compleated],
                labels=["Compleated","Incompleated"],
                colors=["green","red"],
                autopct="%1.1f%%",
                startangle=90)
            self.ax.set_title("Task Compleated %")
        self.piecanvas.draw()

    def delete_tasks(self):
        self.logic.delete_tasks()
        self.refresh_tasks()




if __name__ == "__main__":
    TMSGui()
