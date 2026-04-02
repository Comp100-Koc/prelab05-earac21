def add_binary(a, b):
    a = a[2:]
    b = b[2:]
    
    i = len(a) - 1
    j = len(b) - 1
    carry = 0
    result = ""
    
    while i >= 0 or j >= 0 or carry:
        
        bit_a = 1 if i >= 0 and a[i] == '1' else 0
        bit_b = 1 if j >= 0 and b[j] == '1' else 0
        
        total = bit_a + bit_b + carry
        
        result = str(total % 2) + result
        carry = total // 2
        
        i -= 1
        j -= 1
    
    result=remove_zeros(result)
    
    return "0b" + result

def remove_zeros(s):
    k = 0
    while k < len(s) and s[k] == '0':
        k += 1
    
    s = s[k:]
    
    if s == "":
        return "0"
    
    return s