def divisible_by_number(numbers, divisor):
    if not numbers:
        raise ValueError("The list of numbers are empty")
    if divisor == 0:
        raise ValueError("Divisor cannot be zero")
    
    divisible_numbers = []

    for number in numbers:
        if number % divisor == 0:
            divisible_numbers.append(number)

    if not divisible_numbers:
        print("No numbers are divisible by ", divisor)
    
    return divisible_numbers


numbers = [5, 4, 10, 15, 20, 25, 27, 38, 44, 50, 55]

print(divisible_by_number(numbers, 5))  # Output: [5, 10, 15, 20, 25, 50, 55]
