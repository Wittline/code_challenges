def split_quote(st):
    
    i = 0
    result = []
    st = st + ' '
    n = len(st) - 1

    while i < n:        
        if st[i] == "'":            
            j = i
            while True:                
                if j == i and st[j] == "'":
                    j +=1
                elif j > i and st[j] ==  "'":
                    break
                else:
                    j +=1
            result.append(st[i:j+1].strip())            
            i = j + 1
        elif st[i] == " ":
            j = i
            while True:                
                if j == i and st[j] == " ":
                    j +=1
                elif j > i and st[j] ==  " ":
                    break
                else:
                    j +=1
            result.append(st[i:j+1].strip())
            i = j + 1          
        else:
            i += 1
    return result

