def reverseWords(s):
    words = s.split()  # Split the sentence into words
    reversed_words = [word[::-1] for word in words]  # Reverse each word
    return ' '.join(reversed_words)  # Join the reversed words with whitespace

# Test case
s = "Let's take LeetCode contest"
print(reverseWords(s))
