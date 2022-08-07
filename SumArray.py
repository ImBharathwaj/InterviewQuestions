def SumArray(arr):
    size = len(arr)
    total = 0
    index = 0
    while index < size:
        total += arr[index]
        index+=1
    return total

if __name__ == '__main__':
    print(SumArray([1,2,3,5,5,6,7,87]))
