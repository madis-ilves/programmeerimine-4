import tkinter as tk
from tkinter import ttk
import datetime
from infoGatherer import (
    saa_lingid,
    saa_tunniplaan,
    saa_tundide_ajad
)

from calenderupload import (
    append_events,
    upload_events
)


class TimetableUI:

    DAYS = [
        "ESMASPÄEV",
        "TEISIPÄEV",
        "KOLMAPÄEV",
        "NELJAPÄEV",
        "REEDE"
    ]
    
    DAY_CODES = [
        "MO",
        "TU",
        "WE",
        "TH",
        "FR"
    ]

    def __init__(self, root):

        self.root = root
        self.root.title("Tunniplaan")
        self.root.geometry("1400x900")

        self.links = saa_lingid()
        self.lesson_times = saa_tundide_ajad()

        self.selections = {}

        self.create_header()
        self.create_grid()

    def create_header(self):

        top = ttk.Frame(self.root)
        top.pack(fill="x", pady=10)

        ttk.Label(
            top,
            text="Vali klass:"
        ).pack(side="left", padx=10)

        self.class_box = ttk.Combobox(
            top,
            values=sorted(self.links.keys()),
            state="readonly",
            width=15
        )

        self.class_box.pack(side="left")
        self.class_box.bind(
            "<<ComboboxSelected>>",
            self.load_timetable
        )

        ttk.Button(
            top,
            text="Prindi valikud",
            command=self.print_choices
        ).pack(side="right", padx=10)
        ttk.Button(
            top,
            text="Upload to Calendar",
            command=self.export_to_calendar
        ).pack(side="right", padx=10)

    def create_grid(self):

        self.grid_frame = ttk.Frame(self.root)
        self.grid_frame.pack(fill="both", expand=True)

    def clear_grid(self):

        for widget in self.grid_frame.winfo_children():
            widget.destroy()

        self.selections.clear()

    def is_optional_lesson(self, options):

        optional_keywords = [
            "(v)",
            "Rootsi",
            "Praktiline kunst",
            "Keskkond ja tervis",
            "Rahvusarhiivi",
            "Segakoor",
            "lisakursus"
        ]

        return any(
            keyword.lower() in subject.lower()
            for keyword in optional_keywords
            for subject in options
        )

    def lesson_widget(self, lesson, row, col, day_index, lesson_index):

        if not lesson:
            return

        unique = list(dict.fromkeys(lesson))

        # Optional lesson (even if only one choice)
        if self.is_optional_lesson(unique):

            options = ["Puudub"] + unique

            selected = tk.StringVar(value="Puudub")

            box = ttk.Combobox(
                self.grid_frame,
                textvariable=selected,
                values=options,
                state="readonly"
            )

            box.grid(
                row=row,
                column=col,
                sticky="nsew",
                padx=2,
                pady=2
            )

            self.selections[(day_index, lesson_index)] = selected

        # Fixed lesson
        elif len(unique) == 1:

            ttk.Label(
                self.grid_frame,
                text=unique[0],
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

        # Multiple choices
        else:

            selected = tk.StringVar(value=unique[0])

            box = ttk.Combobox(
                self.grid_frame,
                textvariable=selected,
                values=unique,
                state="readonly"
            )

            box.grid(
                row=row,
                column=col,
                sticky="nsew",
                padx=2,
                pady=2
            )

            self.selections[(day_index, lesson_index)] = selected

    def load_timetable(self, event=None):

        self.clear_grid()

        class_name = self.class_box.get()

        timetable = saa_tunniplaan(
            self.links[class_name]
        )

        # Remove consultation lesson
        for day in timetable:
            if day:
                day.pop(0)

        # Corner label
        ttk.Label(
            self.grid_frame,
            text=""
        ).grid(row=0, column=0)

        # Day headers
        for col, day in enumerate(self.DAYS, start=1):

            ttk.Label(
                self.grid_frame,
                text=day,
                font=("Arial", 11, "bold")
            ).grid(
                row=0,
                column=col,
                padx=5,
                pady=5
            )


        for lesson_nr, time_data in enumerate(
                self.lesson_times,
                start=1):

            start_time, end_time = time_data

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

        for day_index, day in enumerate(timetable):

            for lesson_index, lesson in enumerate(day):

                self.lesson_widget(
                    lesson,
                    lesson_index + 1,
                    day_index + 1,
                    day_index,
                    lesson_index
                )

        for c in range(6):
            self.grid_frame.columnconfigure(
                c,
                weight=1
            )

    def get_final_timetable(self):

        class_name = self.class_box.get()

        timetable = saa_tunniplaan(
            self.links[class_name]
        )

        # Remove consultation lesson
        for day in timetable:
            if day:
                day.pop(0)

        final_timetable = []

        for day_index, day in enumerate(timetable):

            current_day = []

            for lesson_index, lesson in enumerate(day):

                unique = list(dict.fromkeys(lesson))

                if not unique:
                    current_day.append("")
                    continue

                # Optional lesson
                if self.is_optional_lesson(unique):

                    selected = self.selections[
                        (day_index, lesson_index)
                    ].get()

                    if selected == "Puudub":
                        current_day.append("")
                    else:
                        current_day.append(selected)

                # Fixed lesson
                elif len(unique) == 1:

                    current_day.append(unique[0])

                # Multiple non-optional choices
                else:

                    selected = self.selections[
                        (day_index, lesson_index)
                    ].get()

                    current_day.append(selected)

            final_timetable.append(current_day)
            print(final_timetable)

        return final_timetable

    def print_choices(self):

        timetable = self.get_final_timetable()

        print("\n=== VALITUD TUNNIPLAAN ===\n")

        for day_name, lessons in zip(self.DAYS, timetable):

            print(day_name)

            for lesson_nr, lesson in enumerate(
                    lessons,
                    start=1):

                if lesson:
                    print(
                        f"  {lesson_nr}. tund: {lesson}"
                    )

            print()
    def get_current_period_end(self):

        today = datetime.date.today()

        # determine school year
        if today.month >= 8:
            school_year = today.year
        else:
            school_year = today.year - 1

        period1_end = datetime.date(
            school_year,
            11,
            23
        )

        period2_end = datetime.date(
            school_year + 1,
            3,
            2
        )

        period3_end = datetime.date(
            school_year + 1,
            6,
            8
        )

        if today <= period1_end:
            return period1_end.strftime("%Y%m%d")

        if today <= period2_end:
            return period2_end.strftime("%Y%m%d")

        return period3_end.strftime("%Y%m%d")
    def export_to_calendar(self):

        timetable = self.get_final_timetable()

        events = []

        # Change to your school's actual end date
        until = self.get_current_period_end()

        # Group lessons with same name and time
        grouped = {}

        for day_index, day in enumerate(timetable):

            weekday = self.DAY_CODES[day_index]

            for lesson_index, subject in enumerate(day):

                if not subject:
                    continue

                start_time, end_time = self.lesson_times[lesson_index]

                key = (
                    subject,
                    start_time,
                    end_time
                )

                if key not in grouped:
                    grouped[key] = []

                grouped[key].append(weekday)

        # Create recurring events
        for (
            subject,
            start_time,
            end_time
        ), weekdays in grouped.items():

            append_events(
                events,
                subject,
                "",
                [start_time, end_time],
                ",".join(weekdays),
                until
            )

        upload_events(events)


root = tk.Tk()
app = TimetableUI(root)
root.mainloop()