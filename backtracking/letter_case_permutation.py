def permutation(S):
    answer = []
    def dfs (depth, sub):
        if len(sub)==len(S):
            answer.append(sub)
        else:
            if S[depth].isalpha():
                dfs(depth+1,sub+S[depth].swapcase())
            dfs(depth+1,sub+S[depth])
  
    dfs(0,"")    
    return answer

print(permutation("a1b1"))