# Input: arr[] = [0, 1, 2, 0, 1, 2]
# Output: [0, 0, 1, 1, 2, 2]
#only use 0 , 1 , 2

# Use _ when you don’t need the variable (just a good habit).

# Use i, j, etc. if you're going to use the value.

# def accending_arr(arr):
#     arrs=arr[0]
#     temp=''
#     for i in arr:
#         if arr[i]<=arrs:
#             arrs=arr[i]
#             temp=arrs
#         else:
#             pass
#     return temp


# print(accending_arr([0, 1, 2, 0, 1, 2]))

# above 👆 code is wrong. Down 👇 code is correct using the sam e logic

# def accending_arr(arr):
#     result = []                      # To store sorted result

#     # Step 1: First add all 0s
#     for i in arr:
#         if i == 0:
#             result.append(i)

#     # Step 2: Then add all 1s
#     for i in arr:
#         if i == 1:
#             result.append(i)

#     # Step 3: Finally add all 2s
#     for i in arr:
#         if i == 2:
#             result.append(i)

#     return result

# print(accending_arr([0, 1, 2, 0, 1, 2]))


#---------------------------------------------------------------------------------

def accneding_arr(arr):
    result = []
    for i in arr:
        if i == 0:
            result.append(i)
    for i in arr:
        if i==1:
            result.append(i)
    for i in arr:
        if i==2:
            result.append(i)
    return result

print(accneding_arr([0,0,1,1,0,2,1,0,1,0,1,2,1,0,1,2]))


def accending_arr(arr):
    
    count0 = count1 = count2 = 0

    for i in arr:
        if i == 0:
            count0 += 1
        elif i == 1:
            count1 += 1
        elif i == 2:
            count2 += 1

    sorted_arr = []

    for _ in range(count0):
        sorted_arr.append(0)   

    for _ in range(count1):
        sorted_arr.append(1)   

    for _ in range(count2):
        sorted_arr.append(2)  

    return sorted_arr

print(accending_arr([0,0,1,1,0,2,1,0,1,0,1,2,1,0,1,2]))
