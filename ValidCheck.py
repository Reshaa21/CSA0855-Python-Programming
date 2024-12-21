def is_valid_string(s: str) -> bool:
    stripped_string = s.strip()
    return bool(stripped_string)
print(is_valid_string("   "))         
print(is_valid_string("Hello"))       
print(is_valid_string("   Hello   ")) 
print(is_valid_string(""))            
