import random


def insertion_sort(data):
    for index in range(len(data) - 1):
        for index2 in range(index + 1, 0, -1):
            if data[index2] < data[index2 - 1]:
                data[index2], data[index2 - 1] = data[index2 - 1], data[index2]
            else:
                break
    return data


if __name__ == "__main__":
    data_list = random.sample(range(100), 50)
    print("before sort:", data_list)
    insertion_sort(data_list)
    print("after sort:", data_list)
