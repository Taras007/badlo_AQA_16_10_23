import random

# Creating a list of 100 random numbers from 1 to 10.
random_numbers = [random.randint(1, 10) for _ in range(100)]

# Counting the occurrence of each element in the list using dictionary comprehension.
count_elements = {i: random_numbers.count(i) for i in set(random_numbers)}

# Outputting the results.
print("List of random numbers:", random_numbers)
print("Count of each element in the list:", count_elements)