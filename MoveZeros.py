def moveZeroes(nums):

    pointer_0 = -1
    for i in range(len(nums)):
        if(nums[i] == 0):
            pointer_0 = i
            break
    
    if(pointer_0 < 0):
       return

    pointer_other = pointer_0 + 1
    
    while(pointer_other < len(nums)):
        if(nums[pointer_other] != 0):
            nums[pointer_0], nums[pointer_other] = nums[pointer_other], nums[pointer_0]
            while(nums[pointer_0] != 0):
                pointer_0 += 1
        pointer_other += 1
    
    print(nums)

moveZeroes([0,1,0,3,12])

