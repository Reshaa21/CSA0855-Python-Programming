def is_valid_number(s: str) -> bool:
    # Remove leading and trailing spaces
    s = s.strip()

    # If the string is empty after stripping, it's not valid
    if not s:
        return False

    # Check for an optional sign at the start
    if s[0] in ['+', '-']:
        s = s[1:]

    # If there's nothing left after removing the sign, it's invalid
    if not s:
        return False

    # Variables to track if a dot or 'e' has been encountered
    has_dot = False
    has_e = False

    for i, char in enumerate(s):
        if char.isdigit():
            continue  # Digits are always valid
        elif char == '.':
            # A dot is valid only if it hasn't appeared yet and 'e' hasn't been encountered
            if has_dot or has_e:
                return False
            has_dot = True
        elif char in ['e', 'E']:
            # 'e' is valid only if it hasn't appeared yet and is not the first/last character
            if has_e or i == 0 or i == len(s) - 1:
                return False
            has_e = True
            # Allow a sign after 'e' (e.g., 2e+10)
            if i + 1 < len(s) and s[i + 1] in ['+', '-']:
                i += 1  # Skip the sign after 'e'
        else:
            # Any other character is invalid
            return False

    return True

# Test inputs
test_inputs = [
    "0", "e", " ", ".", "%", "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10",
    "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789", "abc", "1a", "1e",
    "e3", "99e2.5", "--6", "-+3", "95a54e53"
]

# Test the function with all inputs
for user_input in test_inputs:
    if is_valid_number(user_input):
        print(f"'{user_input}' is a valid number.")
    else:
        print(f"'{user_input}' is not a valid number.")
