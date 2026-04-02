def remove_adjacent_duplicates(s):
    '''
    Given a string remove all the adjacent duplicate characters and return the string
    '''
    
    i=0
    while i<len(s)-1:
        
        if s[i] == s[i+1]:
            if i == 0:
                s = s[2:len(s)]
            
            else:
                s = s[0:i]+s[i+2:len(s)]
                i -= 1
        else:
            i += 1
    
    return s