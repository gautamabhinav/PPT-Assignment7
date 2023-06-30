def reverseStr(s, k):
    chars = list(s)  # Convert the string to a list of characters
    for i in range(0, len(chars), 2 * k):
        # Reverse the first k characters within each 2k group
        chars[i:i+k] = chars[i:i+k][::-1]
    return ''.join(chars)  # Convert the list of characters back to a string

# Test case
s = "abcdefg"
k = 2
print(reverseStr(s, k))
