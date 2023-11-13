import datetime

def calculate_age(birth_datetime):
    current_datetime = datetime.datetime.now()
    age = current_datetime - birth_datetime  # The time difference representing age.

    # Returning both datetime and timestamp.
    return age, age.total_seconds()

# Example of using the function:
birth_date = datetime.datetime(1990, 11, 4, 6, 0)  # Date of birth.

age, age_timestamp = calculate_age(birth_date)
print("Your age in days:", age)
print("Your age in seconds:", age_timestamp)