def partition(s) :
    answ = []
    for x in range (1,len(s)):
        for y in range (0,x):
            revers = s [y:x]
            reversed = revers[::-1]
            if revers == reversed:
                answ.append(revers)
    return answ
        
        
        
print (partition("aab"))