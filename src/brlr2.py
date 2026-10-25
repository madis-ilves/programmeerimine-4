import tkinter as tk
from tkinter import ttk
 
 
class TimetableUI:
 
    DAYS = [
        "ESMASPÄEV",
        "TEISIPÄEV",
        "KOLMAPÄEV",
        "NELJAPÄEV",
        "REEDE"
    ]
 
    # Placeholder data, only so the layout has something to show
    CLASSES = ["12A", "12B", "11A"]
 
    LESSON_TIMES = [
        ("8:15", "9:00"),
        ("9:10", "9:55"),
        ("10:05", "10:50")
    ]
 
    # None = empty cell, str = fixed lesson, list = dropdown choices
    SAMPLE = [
        ["Matemaatika", "Füüsika", "Keemia"],
        ["Eesti keel", ["Puudub", "Segakoor"], "Kehaline kasvatus"],
        [["Inglise keel", "Saksa keel"], "Bioloogia", ["Matemaatika", "Keemia"]],
        ["Ajalugu", ["Saksa keel", "Prantsuse keel"], "Geograafia"],
        [["Puudub", "Praktiline kunst"], "Kirjandus", "Inglise keel"]
    ]
 
    def __init__(self, root):
 
        self.root = root
        self.root.title("Tunniplaan")
        self.root.geometry("1400x900")
 
        self.create_header()
        self.create_grid()
        self.draw_grid()
 
    def create_header(self):
 
        top = ttk.Frame(self.root)
        top.pack(fill="x", pady=10)
 
        ttk.Label(
            top,
            text="Vali klass:"
        ).pack(side="left", padx=10)
 
        self.class_box = ttk.Combobox(
            top,
            values=self.CLASSES,
            state="readonly",
            width=15
        )
        self.class_box.pack(side="left")
        self.class_box.current(0)
 
        ttk.Button(
            top,
            text="Prindi valikud"
        ).pack(side="right", padx=10)
 
        ttk.Button(
            top,
            text="Upload to Calendar"
        ).pack(side="right", padx=10)
 
    def create_grid(self):
 
        self.grid_frame = ttk.Frame(self.root)
        self.grid_frame.pack(fill="both", expand=True)
 
    def draw_grid(self):
 
        # Corner label
        ttk.Label(self.grid_frame, text="").grid(row=0, column=0)
 
        # Day headers
        for col, day in enumerate(self.DAYS, start=1):
            ttk.Label(
                self.grid_frame,
                text=day,
                font=("Arial", 11, "bold")
            ).grid(row=0, column=col, padx=5, pady=5)
 
        # Lesson number and time labels
        for lesson_nr, (start_time, end_time) in enumerate(
                self.LESSON_TIMES, start=1):
            ttk.Label(
                self.grid_frame,
                text=f"{lesson_nr}. tund\n{start_time}-{end_time}",
                relief="ridge"
            ).grid(
                row=lesson_nr,
                column=0,
                sticky="nsew",
                padx=2,
                pady=2
            )
 
        # Lesson cells
        for day_index, day in enumerate(self.SAMPLE):
            for lesson_index, lesson in enumerate(day):
                self.lesson_widget(
                    lesson,
                    lesson_index + 1,
                    day_index + 1
                )
 
        for c in range(6):
            self.grid_frame.columnconfigure(c, weight=1)
 
    def lesson_widget(self, lesson, row, col):
 
        if not lesson:
            return
 
        # Dropdown
        if isinstance(lesson, list):
 
            selected = tk.StringVar(value=lesson[0])
 
            ttk.Combobox(
                self.grid_frame,
                textvariable=selected,
                values=lesson,
                state="readonly"
            ).grid(
                row=row,
                column=col,
                sticky="nsew",
                padx=2,
                pady=2
            )
 
        # Fixed lesson
        else:
 
            ttk.Label(
                self.grid_frame,
                text=lesson,
                relief="solid",
                anchor="center",
                justify="center",
                wraplength=180
            ).grid(
                row=row,
                column=col,
                sticky="nsew",
                padx=2,
                pady=2
            )
 
 
root = tk.Tk()
app = TimetableUI(root)
root.mainloop()
