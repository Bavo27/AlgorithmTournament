randomList = [5, 2, 9, 1, 5, 6]
def bavoSort(arr):
    for i in range(len(arr)):
        for j in range(i - 1, -1, -1):
            curr = arr[j]
            if arr[j] > arr[j+1]:
                arr[j] = arr[j+1]
                arr[j+1] = curr
    return arr
sortedList = bavoSort(randomList)
print("Sorted array is:", sortedList)