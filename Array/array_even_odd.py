# You are given an array arr[]. Your task is to count the number of even and odd elements. Return first odd count then even count.

# Examples: 

# Input: arr = [2, 3, 4, 5, 6]
# Output: 2 3 
# Explanation: There are two odds[3, 5] and three even[2, 4, 6] present in the array.

# Input: arr = [22, 32, 42, 52, 62]
# Output: 0 5
# Explanation: All the elements are even.

def array_even(arr):
    countEven=0
    countOdd=0
    
    for num in arr:
        
        # print(num)

        if(num%2==0):
            print("even")
            countEven += 1
            
        else:
            print("odd")
            countOdd += 1
            
    print("total number of even",countEven)
    print("total number of odd",countOdd)
    
array_even([22, 32, 42, 52, 62])