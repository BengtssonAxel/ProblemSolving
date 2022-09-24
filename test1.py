A = [-1,-3]

def solution(A):
    k = 1
    Dict = {}
    for x in A:
        if x >= 0:  
            Dict[x] = x
    i = True
    while i:
        if Dict.get(k) == None:
            print(k)
            i = False
        k += 1

solution(A)