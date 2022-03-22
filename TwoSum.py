def twoSum(numbers, target):
    first = 0
    n = len(numbers)
    last = n - 1
    while(first < last):
        temp = numbers[first] + numbers[last]
        if (temp == target):
            return [first + 1, last + 1]
        
        elif(temp < target):
            last += 1
        
        else:
            first += 1
    
print(twoSum([2, 7, 11, 45], 9))
