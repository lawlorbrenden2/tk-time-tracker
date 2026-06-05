from datetime import datetime, timedelta

# Calculate total hours to work today
def get_total_hours(target_hours, worked_hours):
    total_hours = target_hours - worked_hours
    total_hours = timedelta(hours=total_hours)
    return total_hours

# Calculate the exact time to clock out
def get_clock_out_time(total_hours, clocked_in_time_input):
    clocked_in_time_obj = datetime.strptime(clocked_in_time_input, '%I:%M:%S %p')
    now = datetime.now()
    clocked_in_time_obj = clocked_in_time_obj.replace(year=now.year, month=now.month, day=now.day)
    clock_out_time_obj = clocked_in_time_obj + total_hours

    return clock_out_time_obj

# Calculate how much time you have left to work
def get_time_left(clock_out_time_obj):
    now = datetime.now()
    time_left = clock_out_time_obj - now

    # Format the output
    total_seconds = time_left.total_seconds()
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    time_left_formatted = f"{hours} hours and {minutes} minutes"

    return time_left_formatted