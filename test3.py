D = [2, 5, 9, 2, 1, 4]
X = 4

def solution(D, X):
    daysToComplete = 1
    i = 0
    max = -1
    min = -1
    streak = False

    for x in D:
        if i == len(D) - 1:
            daysToComplete +=1
            return(daysToComplete)
        if not streak: 
            if min < 0:
                D[i] = min
            if max < 0:
                D[i] = max
            
        if streak:
            if D[i] < min and abs(D[i] - min) <= X:
                min = D[i]
            if D[i] > max and abs(D[i] - max) <= X:
                max = D[i]
        if abs(D[i] - D[i+1]) > X or (abs(D[i] - min)) or abs(D[i] - max) > X:
            daysToComplete += 1
            streak = False 
            max = -1
            min - -1    
        streak = True
        i += 1
    return(daysToComplete)
      
print(solution(D, X))

#i  / i+1 == +/- --> x. 
# 3
# x 1, 6.