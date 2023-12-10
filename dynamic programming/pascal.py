def generate(numRows):
    answ = [[1]]*numRows
    for i in range(1,len(answ)):
        for e in range(1,len(answ[i-1])):
            answ[i]= answ[i]+[answ[i-1][e]+answ[i-1][e-1]]
        answ[i] = answ[i]+[1]
    return answ    

print(generate(numRows = 50))   