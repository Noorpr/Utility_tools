def first_last_same(myList: list):
    if not myList:
        raise ValueError("The List is empty")
    if len(myList) < 2:
        raise Warning("The List has less than 2 elements")
    
    if myList[0] == myList[-1]:
        return True
    else:
        return False
    

numbers_x = [1, 2, 3, 4, 5, 1]
print(first_last_same(numbers_x)) # Output: True

numbers_y = [1, 2,3, 4, 5, 6]
print(first_last_same(numbers_y))  # Output: False