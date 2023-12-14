is_number = lambda s: s.replace('.', '', 1).isdigit()

print(is_number("123.45"))  # Output: True
print(is_number("abc123"))  # Output: False