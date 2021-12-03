def preprocess(arr, N, left, right): 
        # initialize first left index as that index only 
        left[0] = 0
        lastIncr = 0
      
        for i in range(1,N): 
            # if current value is greater than previous, 
            # update last increasing 
            if (arr[i] > arr[i - 1]): 
                lastIncr = i 
            left[i] = lastIncr 
      
        # initialize last right index as that index only 
        right[N - 1] = N - 1
        firstDecr = N - 1
      
        i = N - 2
        while(i >= 0): 
            # if current value is greater than next, 
            # update first decreasing 
            if (arr[i] > arr[i + 1]): 
                firstDecr = i 
            right[i] = firstDecr 
            i -= 1
      
    # method returns true if arr[L..R] is in mountain form 
def isSubarrayMountainForm(arr, left, right, L, R): 
        
    # return true only if right at starting range is 
    # greater than left at ending range 
    return (right[L] >= left[R]) 

def processqueries(arr,n,m,q):
    result=[]
    left = [0 for i in range(n)] 
    right = [0 for i in range(n)] 
    preprocess(arr, n, left, right)
    for i in q:
        L,R=i
        if (isSubarrayMountainForm(arr, left, right, L, R)): 
            result.append("Yes")
        else:
            result.append("No")
    return result


processqueries([2,3,2,4,4,6,3,2],8, 2,[[0,2], [1,3]] )