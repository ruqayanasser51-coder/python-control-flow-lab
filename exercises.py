# Exercise 5: What's the Season?

def determine_season():
    month = input("Enter the month of the year: ").strip().title()
    day_input = input("Enter the day of the month: ").strip()

    valid_months = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ]

    if month not in valid_months:
        print("Invalid month.")
        return

    try:
        day = int(day_input)
    except ValueError:
        print("Invalid day.")
        return

    days_in_month = {
        "Jan": 31, "Feb": 29, "Mar": 31, "Apr": 30,
        "May": 31, "Jun": 30, "Jul": 31, "Aug": 31,
        "Sep": 30, "Oct": 31, "Nov": 30, "Dec": 31
    }

    if day < 1 or day > days_in_month[month]:
        print("Invalid day.")
        return

    if (month == "Dec" and day >= 21) or month in ["Jan", "Feb"] or (month == "Mar" and day <= 19):
        season = "Winter"
    elif (month == "Mar" and day >= 20) or month in ["Apr", "May"] or (month == "Jun" and day <= 20):
        season = "Spring"
    elif (month == "Jun" and day >= 21) or month in ["Jul", "Aug"] or (month == "Sep" and day <= 21):
        season = "Summer"
    else:
        season = "Fall"

    print(f"{month} {day} is in {season}.")


# Call the function
determine_season() 