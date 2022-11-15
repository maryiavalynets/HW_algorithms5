# 1. Selection Sort algorithm in descending order

def selectionSort(array, size):

    for s in range(size):
        max_idx = s
        for i in range(s + 1, size):
            if array[i] > array[max_idx]:
                max_idx = i
        (array[s], array[max_idx]) = (array[max_idx], array[s])

data = [7, 2, 1, 6]
size = len(data)
selectionSort(data, size)
print(data)

#2. Bubble Sort algorithm in descending order

def bubblesort(elements):

    swapped = False

    for n in range(len(elements)-1, 0, -1):
        for i in range(n):
            if elements[i] < elements[i + 1]:
                swapped = True
                elements[i], elements[i + 1] = elements[i + 1], elements[i]
        if not swapped:
            return

elements = [39, 12, 18, 85, 72, 10, 2, 18]
bubblesort(elements)
print(elements)

#3. Insertion Sort algorithm in descending order

def insertionsort(arr):

    for step in range(1, len(arr)):
        key = arr[step]
        j = step - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key

arr = [15, 50, -27, -4, 10 ]
insertionsort(arr)
print(arr)

#4. Merge Sort algorithm in descending order

def mergesort(lst, reverse=False):

    if len(lst) < 2:
        return lst

    middle = len(lst) // 2
    left = mergesort(lst[:middle], reverse)
    right = mergesort(lst[middle:], reverse)

    i, j, k = 0, 0, 0

    if reverse:
        while i < len(left) and j < len(right):
            if left[i] >= right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1

    else:
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1

    return lst

lst = [2, 4, 1, 3, 8, 5]
print(mergesort(lst, True))