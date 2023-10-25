import datetime


def adjust_date(input_datetime, days, operation):

    # Check the type of operation and apply the corresponding adjustment.
    if operation:  # if True, add days.
        adjusted_date = input_datetime + datetime.timedelta(days=days)
    else:  # if False, subtract days.
        adjusted_date = input_datetime - datetime.timedelta(days=days)

    return adjusted_date


# Example of using the function:
date = datetime.datetime(2023, 10, 23, 12, 0)  # Date to be adjusted.
days_to_adjust = 5  # Number of days for the adjustment.
addition = True  # Boolean value for choosing addition or subtraction.

new_date = adjust_date(date, days_to_adjust, addition)
print("Adjusted date:", new_date)