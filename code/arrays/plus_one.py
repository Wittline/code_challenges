#input = [9, 9, 9]
#output = [1,0,0,0]

#input = [1, 2, 3]
#output = [1,2,4]

def plus_one(numbers):
    
    carry = 1
    for i in range(len(numbers) - 1, -1 , -1):

        numbers[i] += carry
        carry = 0

        if numbers[i] > 9:
            numbers[i] = 0
            carry = 1
        
        return numbers