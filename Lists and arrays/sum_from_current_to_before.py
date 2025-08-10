def sum_from_current_to_before(myList : list, index : int):
    if not myList:
        raise ValueError("The list is empty")
    
    if len(myList) < 2 and index < 0:
        return myList[0]
    else:
        if index < 0 or index >= len(myList):
            raise IndexError("Index out of bounds")
    
    total = 0
    for i in range(index, -1, -1):
        total += myList[i]
    return total

# Bonus function to calculate cumulative sum
def cumulative_sum(myList : list):
    if not myList:
        raise ValueError("The list is empty")
    cumulative_list = []

    for i in range(len(myList)):
        cumulative_list.append(sum_from_current_to_before(myList, i))

    return cumulative_list

myList = [1, 2, 3, 4, 5]
print(sum_from_current_to_before(myList, 3))  # Output: 10 (4 + 3 + 2 + 1)

