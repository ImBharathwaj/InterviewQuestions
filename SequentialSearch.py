def SequentialSearch(arr, value):
    size = len(arr)
    i = 0
    while i < size:
        if value == arr[i]:
            return True
        i += 1
    return False

if __name__ == '__main__':
    print(SequentialSearch([1,2,32,4,5,6,7,7,8],8))
