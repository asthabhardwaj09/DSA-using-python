# def arr_min_max(arr):
#     print(min(arr), max(arr))

# arr_min_max([3, 2, 1, 56, 10000, 167])

# def arr_min_max(arr):
#     min_val=arr[0]
#     max_val=arr[0]
#     for i in arr:
#         if i<min_val:
#             min_val = i
#         elif i>max_val:
#             max_val = i
#         else:
#             pass
#     print (min_val, max_val)
    
    
    
# arr_min_max([3, 2, 1, 56, 10000, 167])


def arr_min_max(arr):
    min_val = arr[0]
    max_val = arr[0]
    for i in arr:
        if i < min_val:
            min_val = i
        elif i > max_val:
            max_val = i
    return min_val, max_val

# -------- Main --------
n = int(input())                          # First line: size of array
arr = list(map(int, input().split()))    # Second line: space-separated integers

min_val, max_val = arr_min_max(arr)
print(min_val, max_val)

