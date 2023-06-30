def addStrings(num1, num2):
    result = []
    carry = 0
    i = len(num1) - 1
    j = len(num2) - 1
    
    while i >= 0 or j >= 0 or carry > 0:
        digit1 = int(num1[i]) if i >= 0 else 0
        digit2 = int(num2[j]) if j >= 0 else 0
        
        curr_sum = digit1 + digit2 + carry
        carry = curr_sum // 10
        digit = curr_sum % 10
        
        result.append(str(digit))
        
        i -= 1
        j -= 1
    
    result.reverse()
    return ''.join(result)

# Test case
num1 = "11"
num2 = "123"
print(addStrings(num1, num2))
