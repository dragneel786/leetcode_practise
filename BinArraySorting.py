def sortBinaryArray (arr, n):
        # Your code here
        one_pos = 0
        for i in range(n):
            if(arr[i] == 1):
                break
            one_pos += 1
        
        for i in range(one_pos + 1, n):
            if(arr[i] == 0):
                arr[one_pos], arr[i] = 0, arr[one_pos]
                while(one_pos < n and arr[one_pos] != 1):
                    one_pos += 1
        
        print(arr)

sortBinaryArray([0,0,0,0], 4)