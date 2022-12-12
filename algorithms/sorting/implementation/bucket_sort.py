import random


def bucket_sort(arr):
    # Assuming arr only contains 0, 1 , 2 or 3
    counts = [0, 0, 0, 0]

    # Count the quantity of each val in arr
    for n in arr:
        counts[n] += 1

    # Fill each bucket in the original array
    i = 0
    for n in range(len(counts)):
        for j in range(counts[n]):
            arr[i] = n
            i += 1
    return arr


if __name__ == "__main__":
    data_list = random.choices(range(4), k=20)
    print("before sort:", data_list)
    bucket_sort(data_list)
    print("after sort:", data_list)