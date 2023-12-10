def generateParenthesis(n):
    ans = []
    def dfs (sub,depth):
        if depth == n:
            return
        dfs (sub+"(",depth+1)
        sub = sub[:-1]
        if sub[-1] == "(":
            dfs (sub+")",depth+1)
    dfs("",0)   
    return ans
generateParenthesis(n = 3)
