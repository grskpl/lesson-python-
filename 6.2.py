def format_seconds(seconds):
    if seconds < 0 or seconds >= 8640000:
        return "Некоректне введене число"

    days, remainder = divmod(seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    if days == 1:
        day_str = "день"
    elif 2 <= days <= 4:
        day_str = "дні"
    else:
        day_str = "днів"

    time_str = f"{hours:02}:{minutes:02}:{seconds:02}"

    return f"{days} {day_str}, {time_str}"

print(format_seconds(0))         # 0 днів, 00:00:00
print(format_seconds(224930))    # 2 дні, 14:28:50
print(format_seconds(466289))    # 5 днів, 09:31:29
print(format_seconds(950400))    # 11 днів, 00:00:00
print(format_seconds(1209600))   # 14 днів, 00:00:00
print(format_seconds(1900800))   # 22 дні, 00:00:00
print(format_seconds(8639999))   # 99 днів, 23:59:59
print(format_seconds(22493))     # 0 днів, 06:14:53
print(format_seconds(7948799))   # 91 день, 23:59:59
