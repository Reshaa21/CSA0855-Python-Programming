def is_valid_number(s: str) -> bool:
    stripped_string = s.strip()

    # If the string is empty after stripping, it's not a valid number
    if not stripped_string:
        return False

    # Handle optional '+' or '-' signs at the beginning
    if stripped_string[0] in ('+', '-'):
        stripped_string = stripped_string[1:]

    try:
        # Try converting the stripped string to a float
        float(stripped_string)
        return True
    except ValueError:
        return False

# Test cases
print(is_valid_number("  +123  "))    # Output: True
print(is_valid_number(" -45.67"))     # Output: True
print(is_valid_number(" 123abc"))     # Output: False
print(is_valid_number("  +  "))       # Output: False
print(is_valid_number("   "))         # Output: False
