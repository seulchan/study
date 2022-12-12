import random


def insertion_sort(data):
    for index in range(len(data) - 1):
        for index2 in range(index + 1, 0, -1):
            if data[index2] < data[index2 - 1]:
                data[index2], data[index2 - 1] = data[index2 - 1], data[index2]
            else:
                break


def insertion_sort_v2(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[j + 1] < arr[j]:
            # arr[j] and arr[j + 1] are out of order so swap them
            arr[j + 1], arr[j] = arr[j], arr[j + 1]
            j -= 1
    return arr


if __name__ == "__main__":
    data_list = random.sample(range(100), 50)
    print("before sort:", data_list)
    insertion_sort_v2(data_list)
    print("after sort:", data_list)
