def print_even_characters(myString : str):
    if not myString:
        raise ValueError("The string is empty")
    
    if len(myString) < 2:
        print(myString)
        raise Warning("The string has less than 2 characters")
    
    even_characters = myString[::2]
    return even_characters

print(print_even_characters("Hello, World!"))  # Output: "Hlo ol!"