def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


arr = [9,8,7,6,5,4,3,8,]
sorted_arr = bubble_sort(arr)
print("Sorted array is:", sorted_arr)

    