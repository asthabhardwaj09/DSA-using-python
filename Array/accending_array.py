# Bubble sort is used here 👇

# def sort_array(arr):
#     n = len(arr)
#     for i in range(n):
#         print (i)
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 # Swap
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr
# print(sort_array([1, 23, 45, 0, 1, 2, 78]))


def sort_array(arr):
    n = len(arr)

    for i in range(n):              # Loop through each element
        for j in range(n):          # Compare with every other element
            if arr[i] < arr[j]:     # If left value is smaller, swap
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

    return arr
print(sort_array([1, 23, 45, 0, 1, 2, 78]))



