import calculator
import customtkinter as ctk

def cli():
    target_hours = float(input("Input your goal for total amount of hours worked this week: "))
    worked_hours = float(input("Input how many hours you've already worked this week (not including today): "))
    clocked_in_time = input("Input what time you clocked in today (e.g. 9:02:17 AM): ")

    total_hours = calculator.get_total_hours(target_hours, worked_hours)
    clock_out_time_obj = calculator.get_clock_out_time(total_hours, clocked_in_time)
    time_left = calculator.get_time_left(clock_out_time_obj)
    clock_out_str = clock_out_time_obj.strftime('%I:%M:%S %p')

    print(f"To reach {target_hours} hours this week, you must work for another {time_left} and clock out at precisely {clock_out_str}.")

class TimeTrackerApp(ctk.CTK):
    def __init__(self):
        super().__init__()
        
        self.title("Weekly Time Calculator")
        self.geometry("400x300")

        self.target_entry = ctk.CTkEntry(self, placeholder_text="Target Hours")
        self.target_entry.pack(pady=10)

        self.worked_entry = ctk.CTkEntry(self, placeholder_text="Worked Hours")
        self.worked_entry.pack(pady=10)

        self.clocked_in_entry = ctk.CTkEntry(self, placeholder_text="Clock In Time")
        self.clocked_in_entry.pack(pady=10)

        self.calc_button = ctk.CTkButton(self, text='Calculate', command=self.run_calculator)
        self.calc_button.pack(pady=10)

    def run_calculator(self):
        targeted_hours = float(self.target_entry.get())
        worked_hours = float(self.worked_entry.get())
        clocked_in_time = self.clocked_in_entry.get()

        total_hours = calculator.get_total_hours(targeted_hours, worked_hours)
        clock_out_time_obj = calculator.get_clock_out_time(total_hours, clocked_in_time)
        time_left = calculator.get_time_left(clock_out_time_obj)
        clock_out_str = clock_out_time_obj.strftime('%I:%M:%S %p')


def main():
    # cli()
    app = TimeTrackerApp()
    app.mainloop()

if __name__ == "__main__":
    main()