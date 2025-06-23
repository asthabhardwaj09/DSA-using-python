# # arr=[3, 10, 4, 7, 20, 15]
# # K=3

def array_smallest(arr):
    k_smallest=arr[0] #a[1] not be there because suppose if the array will be array_smalles[1] it will show error
    for smallest in arr:
        if k_smallest>smallest:
            k_smallest=smallest
    print(k_smallest)


array_smallest([7, 10, 4, 3, 20, 15])


# def kth_smallest(arr, k):
#     used = [False] * len(arr)  # Track used elements

#     for _ in range(k):
#         min_val = float('inf')
#         min_index = -1

#         # Find the minimum unused element
#         for i in range(len(arr)):
#             if not used[i] and arr[i] < min_val:
#                 min_val = arr[i]
#                 min_index = i

#         used[min_index] = True  # Mark that as used

#     return min_val  # After k iterations, this is the kth smallest

# # Example usage
# arr = [7, 10, 4, 3, 20, 15]
# k = 3
# print("The", k, "th smallest element is:", kth_smallest(arr, k))



def kth_smallest(arr, k):
    for _ in range(k):
        smallest = float('inf') #to ensure any number in the array will be smaller, so we can correctly find the 
        index = -1

        # Find the smallest element in array
        for i in range(len(arr)):
            if arr[i] < smallest:
                smallest = arr[i]
                index = i

        arr[index] = float('inf')  # Mark it as used by setting to a very large number

    return smallest

arr = [7, 10, 4, 3, 20, 15]
k = 3
print(kth_smallest(arr, k))



# index = -1    => Start with "no index found yet"    
# index = i     => Save the position of smallest number
# arr[index] = inf => Remove that smallest number for next round
