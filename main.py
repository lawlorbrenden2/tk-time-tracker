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

class TimeTrackerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Weekly Time Calculator")
        self.geometry("650x250")

        self.help_window = None

        self.top_bar = ctk.CTkFrame(self, fg_color="transparent")
        self.top_bar.pack(fill="x", padx=10, pady=5)

        self.help_button = ctk.CTkButton(
            self.top_bar, 
            text="?", 
            width=30, 
            fg_color="#8A2BE2",
            hover_color="#6A1CB3",
            command=self.open_help
        )
        self.help_button.pack(side="right")

        self.input_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.input_frame.pack(pady=20)

        self.target_entry = ctk.CTkEntry(self.input_frame, placeholder_text="Target Hours")
        self.target_entry.pack(side="left", padx=12)

        self.worked_entry = ctk.CTkEntry(self.input_frame, placeholder_text="Worked Hours")
        self.worked_entry.pack(side="left", padx=12)

        self.clocked_in_entry = ctk.CTkEntry(self.input_frame, placeholder_text="Clock In Time")
        self.clocked_in_entry.pack(side="left", padx=12)

        self.calc_button = ctk.CTkButton(
            self, 
            text="Calculate", 
            fg_color="#8A2BE2", 
            hover_color="#6A1CB3", 
            command=self.run_calculator
        )
        self.calc_button.pack(pady=10)

        self.result_label = ctk.CTkLabel(self, text="Enter your times and click Calculate.", wraplength=650)
        self.result_label.pack(pady=10)

    def run_calculator(self):
        try:
            target_hours = float(self.target_entry.get())
            worked_hours = float(self.worked_entry.get())
            clocked_in_time = self.clocked_in_entry.get()

            total_hours = calculator.get_total_hours(target_hours, worked_hours)
            clock_out_time_obj = calculator.get_clock_out_time(total_hours, clocked_in_time)
            time_left = calculator.get_time_left(clock_out_time_obj)
            clock_out_str = clock_out_time_obj.strftime('%I:%M:%S %p')

            result_text = f"To reach {target_hours} hours this week, you must work for another {time_left} and clock out at precisely {clock_out_str}."
            self.result_label.configure(text=result_text)
        except ValueError:
            self.result_label.configure(text="Error: Please check your inputs and try again. Ensure your time is formatted like 09:00:00 AM.")

    def open_help(self):
        if self.help_window is None or not self.help_window.winfo_exists():
            self.help_window = ctk.CTkToplevel(self)
            self.help_window.title("Formatting Help")
            self.help_window.geometry("300x200")
 
            self.help_window.attributes("-topmost", True)

            help_text = (
                "Input Formatting Guide:\n\n"
                "Target Hours: Decimal (e.g., 40 or 40.5)\n"
                "Worked Hours: Decimal (e.g., 32.345)\n"
                "Clock In Time: HH:MM:SS AM/PM\n"
                "(e.g., 09:00:00 AM)"
            )

            help_label = ctk.CTkLabel(self.help_window, text=help_text, justify="left")
            help_label.pack(padx=20, pady=30)
        else:
            self.help_window.focus()
def main():
    # cli()
    app = TimeTrackerApp()
    app.mainloop()

if __name__ == "__main__":
    main()