def longest(s):

    pos_dict = []
    for n in range(0, len(s)):
        if s[n] == '1':
            pos_dict.append(n)    

    longest_s = 0
    
    for inx in pos_dict:
        i = inx  + 1
        unos = '1'     
        while(i < len(s)):
            if s[i] == '1':                
                unos += '1'
                i += 1
            else:
                longest_s = max(len(unos), longest_s)               
                break
                
    return longest_s * '1'

print(longest('10110110011110'))


def longest_ones(s):

  lon_sequence = 0
  

  cur_sequence = 0
  

  for ch in s:

    if ch == '1':
      cur_sequence += 1

    else:

      if cur_sequence > lon_sequence:
        lon_sequence = cur_sequence
      cur_sequence = 0

  return lon_sequence

print(longest_ones("11011101"))


