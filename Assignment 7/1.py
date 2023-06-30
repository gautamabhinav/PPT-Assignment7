def isIsomorphic(s, t):
    if len(s) != len(t):
        return False
    
    char_map_s = {}
    char_map_t = {}
    
    for i in range(len(s)):
        char_s = s[i]
        char_t = t[i]
        
        if char_s in char_map_s:
            if char_map_s[char_s] != char_t:
                return False
        else:
            char_map_s[char_s] = char_t
        
        if char_t in char_map_t:
            if char_map_t[char_t] != char_s:
                return False
        else:
            char_map_t[char_t] = char_s
    
    return True

# Test case
s = "egg"
t = "add"
print(isIsomorphic(s, t))
