def BinarySearch(arr, key):
    size = len(arr)
    low = 0
    high = size - 1
    mid = int(low + (high - low) / 2)
    while low <= high:
        print(mid)
        if arr[mid] == key:
            return True
        else:
            if arr[mid] < key:
                low = mid + 1
            else:
                high = mid - 1
    return False


if __name__ == '__main__':
    print(BinarySearch(range(9), 4))
