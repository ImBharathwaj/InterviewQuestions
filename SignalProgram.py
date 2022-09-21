#SIGNALS PROGRAM 

def read_integer(msg):
    a = input(msg)
    if(a.isdigit()):
        return int(a)
    else:
        print('Invalid.')
        return read_integer(msg)

def read_char(msg):
    a = input(msg)
    a = a.lower()
    if(a == "y" or a == "n"):
        return a
    else:
        print('Invalid.')
        return read_integer(msg)

# Getting input from the User
NoOfSignal = read_integer("Enter the number of signals : ")
Sametime = read_char("Does the signals have same time difference(y or n): ")
TimeToSig = []
if Sametime == "y":
    SigToDest = read_integer("Enter time difference between each signals including last signal to destination :")
    for i in range(NoOfSignal+1):
        TimeToSig.append(SigToDest)
else:
    
    for i in range(NoOfSignal):
        TimeToSig.append(int(input("Enter time to signal :")))
    SigToDest = read_integer("Enter time to reach destination from signal :")
TwoWay = read_char("Does all signals are two ways (y or n):")
paths = []
if TwoWay == "y":
    for i in range(NoOfSignal+1):
        paths.append(2)
else:
    for i in range(NoOfSignal):
        paths.append(read_integer("Enter number of paths at signal (2-4) :"))
signal = read_integer("Enter the signal time : ")

#genarating the ways
way = [int(x) for x in range(0,signal+1)]
two , three , four = 2*signal,3*signal,4*signal
for i in range(len(paths)):
    if paths[i] == 2:
        a = two
    elif paths[i] == 3:
        a = three
    else:
        paths[i] = four

    for i in range(NoOfSignal):
        for i in range(len(way)):
            res = way[i]+ a
            way.append(res)
    way = list(set(way))

def issafe(way,key):
    for i in range(len(way)):
        if key == way[i]:
           return int(0)
        if key < way[i]:
            a = way[i]-key
            break
    return a

res = 0
for i in range(NoOfSignal):
   res = res + TimeToSig[i] + abs((issafe(way,TimeToSig[i])))
reachDes = res + SigToDest
print("It takes {} seconds to reach destination".format(reachDes))
