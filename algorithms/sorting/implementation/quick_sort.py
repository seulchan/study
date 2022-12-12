import random


# Implementation of QuickSort
def quick_sort(arr, s, e):
    if e - s + 1 <= 1:
        return

    pivot = arr[e]
    left = s  # pointer for left side

    # Partition: elements smaller than pivot on left side
    for i in range(s, e):
        if arr[i] < pivot:
            tmp = arr[left]
            arr[left] = arr[i]
            arr[i] = tmp
            left += 1

    # Move pivot in-between left & right sides
    arr[e] = arr[left]
    arr[left] = pivot

    # Quick sort left side
    quick_sort(arr, s, left - 1)

    # Quick sort right side
    quick_sort(arr, left + 1, e)

    return arr


if __name__ == "__main__":
    data_list = random.sample(range(100), 50)
    print("before sort:", data_list)
    quick_sort(data_list, 0, len(data_list) - 1)
    print("after sort:", data_list)
