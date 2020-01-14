def binarySearch(listData, value):
    low = 0
    high = len(listData) - 1

    while (low <= high):
        mid = round((high + low) / 2)

        if(listData[mid] == value):
            return mid
        elif(listData[mid] < value):
            low = mid + 1
        else:
            high = mid - 1

    return -1


test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15

binarySearch(test_list, test_val2)
