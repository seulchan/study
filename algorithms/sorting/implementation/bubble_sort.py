import random


def bubble_sort(data):
    for index in range(len(data)-1):
        swap = False
        for index2 in range(len(data)-index-1):
            if data[index2] > data[index2 + 1]:
                data[index2], data[index2 + 1] = data[index2 + 1], data[index2]
                swap = True

        if swap == False:
            break


if __name__ == "__main__":
    data_list = random.sample(range(100), 50)
    print("before sort:", data_list)
    bubble_sort(data_list)
    print("after sort:", data_list)