def find_occurance(string, substring):
    if not string or not substring:
        raise ValueError("String or substring cannot be empty")
    if len(substring) > len(string):
        return 0
    
    count = 0
    string_words = string.split()

    for word in string_words:
        if substring in word:
            count += word.count(substring)

    if count > 0:
        return substring + " occurs " + str(count) + " times"
    else:
        return substring + " does not occur in the string"
    

str_word = "Emma is good developer. Emma is a writer"
substr_word = "Emma"

print(find_occurance(str_word, substr_word))  # Output: "Emma occurs 2 times"