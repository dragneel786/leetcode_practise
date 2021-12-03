
def sortedSquares(nums):
    idx = -1
    n = len(nums) 
    first_idx = 0
    last_idx = n - 1
    res = [0 for _ in range(n)]
    i = n - 1
    while(first_idx <= last_idx):
        if (abs(nums[first_idx]) > abs(nums[last_idx])):
            res[i] = (nums[first_idx] ** 2)
            first_idx += 1
        else:
            res[i] = (nums[last_idx] ** 2)
            last_idx -= 1

        i -= 1
            
    return res



print(sortedSquares([-8, -1, 0, 1, 2, 3]))