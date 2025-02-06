def validPalindrome(word: str):
    return word == word[::-1]

def validPalindrome2(word: str):
    word = ''.join(c.lower() for c in word if c.isalnum())
    l = 0
    r = len(word) - 1
    while l <= r:
        if word[l] != word[r]:
            return False
        else:
            l += 1
            r -= 1
    return True

print(validPalindrome("nitin"))
print(validPalindrome2("nitin"))

print(validPalindrome("racecar"))
print(validPalindrome2("racecar"))