def start_from_center(s, left, right):
    
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    
    # son geçerli substring
    return s[left+1:right]


def longest_palindromic_substring(s):
    """
    Returns the longest palindromic substring (length >= 2).
    If multiple exist, returns the first one.
    """
    longest = ""

    for i in range(len(s)):
        
        p1 = start_from_center(s, i, i)
        p2 = start_from_center(s, i, i+1)
        
        if len(p1) > len(longest):
            longest = p1
        
        if len(p2) > len(longest):
            longest = p2

    if len(longest) < 2:
        return ""

    return longest