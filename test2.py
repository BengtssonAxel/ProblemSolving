N = 191
K = 4

def solution(N, K):
    myList = [int(i) for i in str(N)]
    while K != 0:
        if myList[0] != 9:
            myList[0] += 1
        elif myList[1] != 9:
            myList[1] += 1
        elif myList[2] != 9:
            myList[2] += 1
        else:
            print(int(''.join(str(x) for x in myList)))
            return int(''.join(str(x) for x in myList))
        K -= 1
    print(int(''.join(str(x) for x in myList)))
    return int(''.join(str(x) for x in myList))
solution(N,K)