import time
import timeit

st = time.process_time()

def reverseArray(arr, start, end):
    i = start
    j = end
    while i < j:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i += 1
        j -= 1

def rotateArray(arr, k):
    n = len(arr)
    reverseArray(arr, 0, k - 1)
    reverseArray(arr, k, n - 1)
    reverseArray(arr, 0, n - 1)

et = time.process_time()

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    rotateArray(arr, 4)
    print(arr)
    elapsed_time = et - st
    print('Elapsed time of rotation is : %.8f' % elapsed_time, 'seconds')
    result = timeit.timeit(stmt='reverseArray()', globals=globals(), number=0)
    print('Elapsed time is : %.8f'%result)
