#Valid Parentheses
def areBracketsBalanced(s):
        stack = []

        dict_brackets = {
            "(":")", 
            "{":"}", 
            "[":"]"                     
        }

        for c in s:
            
            if c in dict_brackets:            
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    if dict_brackets[stack.pop()] != c:
                        return False                
            
        return not stack
 
 
# Driver Code
if __name__ == "__main__":
    expr = "{()}[]"
 
    # Function call
    if areBracketsBalanced(expr):
        print("Balanced")
    else:
        print("Not Balanced")