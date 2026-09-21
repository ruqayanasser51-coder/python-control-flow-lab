# Exercise 1: Vowel or Consonant

def check_letter():
    letter = input("Enter a letter: ")

    if len(letter) != 1 or not letter.isalpha():
        print("Please enter a single letter.")
    elif letter.lower() in "aeiou":
        print(f"The letter {letter} is a vowel.")
    else:
        print(f"The letter {letter} is a consonant.")


# Call the function
check_letter()


# Exercise 2: Old enough to vote?

def check_voting_eligibility():
    try:
        age = int(input("Please enter your age: "))

        if age < 0:
            print("Please enter a valid age.")
            return

        voting_age = 18

        if age >= voting_age:
            print("You are eligible to vote.")
        else:
            print("You are not eligible to vote.")

    except ValueError:
        print("Please enter a valid number.")


# Call the function
check_voting_eligibility()


# Exercise 3: Calculate Dog Years

def calculate_dog_years():
    age = int(input("Input a dog's age: "))

    if age <= 2:
        dog_years = age * 10
    else:
        dog_years = 20 + (age - 2) * 7

    print(f"The dog's age in dog years is {dog_years}.")


# Call the function
calculate_dog_years()


# Exercise 4: Weather Advice

def weather_advice():
    cold = input("Is it cold? (yes/no): ").lower()
    raining = input("Is it raining? (yes/no): ").lower()

    if cold == "yes" and raining == "yes":
        print("Wear a waterproof coat.")
    elif cold == "yes" and raining == "no":
        print("Wear a warm coat.")
    elif cold == "no" and raining == "yes":
        print("Carry an umbrella.")
    else:
        print("Wear light clothing.")


# Call the function
weather_advice()


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
        "Jan": 31,
        "Feb": 29,
        "Mar": 31,
        "Apr": 30,
        "May": 31,
        "Jun": 30,
        "Jul": 31,
        "Aug": 31,
        "Sep": 30,
        "Oct": 31,
        "Nov": 30,
        "Dec": 31
    }

    if day < 1 or day > days_in_month[month]:
        print("Invalid day.")
        return

    if (
        (month == "Dec" and day >= 21)
        or month in ["Jan", "Feb"]
        or (month == "Mar" and day <= 19)
    ):
        season = "Winter"

    elif (
        (month == "Mar" and day >= 20)
        or month in ["Apr", "May"]
        or (month == "Jun" and day <= 20)
    ):
        season = "Spring"

    elif (
        (month == "Jun" and day >= 21)
        or month in ["Jul", "Aug"]
        or (month == "Sep" and day <= 21)
    ):
        season = "Summer"

    else:
        season = "Fall"

    print(f"{month} {day} is in {season}.")


# Call the function
determine_season()


# Exercise 6: Number Guessing Game

def guess_number():
    target_number = 42

    for attempt in range(1, 6):
        try:
            guess = int(input("Guess a number between 1 and 100: "))

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            if guess == target_number:
                print("Congratulations, you guessed correctly!")
                return

            if attempt == 5:
                print("Last chance!")

            if guess < target_number and not guess == target_number:
                print("Guess is too low.")
            elif guess > target_number or not guess < target_number:
                print("Guess is too high.")

        except ValueError:
            print("Please enter a valid number.")

    print("Sorry, you failed to guess the number in five attempts.")


# Call the function
guess_number()