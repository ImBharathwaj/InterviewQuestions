def sentinelLinearSearch(arr, key):
    n = len(arr)
    last = arr[n - 1]
    arr[n - 1] = key
    i = 0
    while arr[i] != key:
        i += 1
    arr[n - 1] = last
    
    if ((i < n-1) or (arr[n-1] == key)):
        print(i)
    else:
        print("Element not present")

if __name__ == '__main__':
    arr = [5,7,4,10,12,14]
    key = 12
    sentinelLinearSearch(arr, key)