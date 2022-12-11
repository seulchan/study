import random


def selection_sort(data):

    for stand in range(len(data) - 1):
        lowest = stand
        for index in range(stand+1, len(data)):
            if data[lowest] > data[index]:
                lowest = index
        data[lowest], data[stand] = data[stand], data[lowest]
    return data


if __name__ == "__main__":
    data_list = random.sample(range(100), 50)
    print("before sort:", data_list)
    selection_sort(data_list)
    print("after sort:", data_list)
