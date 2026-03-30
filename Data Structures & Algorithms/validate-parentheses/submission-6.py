class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map_el = {']':'[',
                  ')':'(',
                  '}':'{' 
        } 
    
        for el in s:
            if el in map_el:
                if stack and stack[-1] == map_el[el]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(el) 
    
        if not stack:
            return True
        else:
            return False
