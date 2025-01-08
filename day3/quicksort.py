def quick_sort_inplace(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort_inplace(arr, low, pi - 1)
        quick_sort_inplace(arr, pi + 1, high)


def partition(arr, low, high):
    pivot = arr[high]  
    i = low - 1  

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


arr = [50, 30, 40, 20, 10]
print("Original list:", arr)
quick_sort_inplace(arr, 0, len(arr) - 1)
print("Sorted list:", arr)
