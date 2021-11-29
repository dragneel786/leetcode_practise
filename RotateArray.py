def rotate(nums, k):
    n = len(nums)
    if(k == n):
        return nums
    
    k = n - k
    for i in range(k // 2):
        nums[i], nums[k - i - 1] = nums[k - i - 1], nums[i]
    
    for i in range(k, (n + k) // 2):
        nums[i], nums[(n + k) - i - 1] = nums[(n + k) - i - 1], nums[i]
        
    for i in range(n // 2):
        nums[i], nums[n - i - 1] = nums[n - i - 1], nums[i]
    
    print(nums)
rotate([-1, 100, 3, 99], 2)