import time

# Storing starting time of the program
st = time.process_time()
def rotate(a, k):
    while k > 0:
        last = a[-1]
        for i in reversed(range((len(a) - 1))):
            a[i + 1] = a[i]
        a[0] = last
        last = a[-1]
        k -= 1

# Storing ending time of the function
et = time.process_time()

if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    rotate(a,4)
    print(a)
    # Calculating elapsed time of the program
    # To calculate with millisecond multiply with 1000
    # To calculate with minute divide it by 60
    # Calculating in seconds
    elapsed_time = et - st
    print('Elapsed time of rotation is : %.9f' % elapsed_time, 'secs')
