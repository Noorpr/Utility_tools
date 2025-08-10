def remove_first_characters(myString : str, n : int):
    if not myString:
        raise ValueError("The string is empty")
    if n < 0 or n >= len(myString):
        raise IndexError("n is out of bounds")
    
    return myString[n:]

print(remove_first_characters("Hello, World!", 7))  # Output: "World!"