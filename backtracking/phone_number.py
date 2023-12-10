def backtrack (digits):
        ans = []
        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(sub,depth):
            if len(sub)>=len(digits):
                ans.append(sub)
            if depth >= len(digits):
                return
            for e in phone_map[digits[depth]]:
                backtrack (sub+e,depth+1)
                backtrack (sub[:-1],depth+1)

        backtrack('', 0)
        return ans
        
              
                
    
    
    
    
    
print(backtrack(digits = "237"))