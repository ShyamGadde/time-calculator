def add_time(start, duration, start_day=""):
    am_pm = start[-2:]

    st_hrs, st_mins = map(int, start.split()[0].split(':'))
    mins_elapsed = None

    if am_pm == "AM":
        if st_hrs == 12:
            mins_elapsed = st_mins
        else:
            mins_elapsed = st_hrs * 60 + st_mins
    else:
        if st_hrs == 12:
            mins_elapsed = st_hrs * 60 + st_smins
        else:
            mins_elapsed = (12 + st_hrs) * 60 + st_mins

    dur_hrs, dur_mins = map(int, duration.split()[0].split(':'))
    add_mins = dur_hrs * 60 + dur_mins

    add_days, new_mins = divmod(mins_elapsed + add_mins, 1440)

    hrs, mins = divmod(new_mins, 60)
    mins = f"{mins}".zfill(2)
    new_time = None

    if not hrs:
        new_time = f"12:{mins} AM"
    elif hrs < 12:
        new_time = f"{hrs}:{mins} AM"
    elif hrs == 12:
        new_time = f"12:{mins} PM"
    else:
        hrs %= 12
        new_time = f"{hrs}:{mins} PM"

    days = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
    if start_day:
        new_time += f", {days[([day for day in days if days[day] == start_day.title()][0] + add_days) % 7]}"

    if add_days == 1:
        new_time += " (next day)"
    elif add_days > 1:
        new_time += f" ({add_days} days later)"
    
    return new_time

# print(add_time("11:06 PM", "01:02"))
print(add_time("11:59 PM", "24:05"))
