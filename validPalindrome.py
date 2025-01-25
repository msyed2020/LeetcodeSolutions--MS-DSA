def validPalindrome(word: str):
    return word == word[::-1]

print(validPalindrome("nitin"))