from pathlib import Path

def PalindromeChecker(word:str):
    word = word.strip()
    chars = []
    for character in word:
        chars.append(character)
    chars.reverse()
    Palindrome = ''.join(chars)

    if Palindrome == word:
        print(f'{word} is palindrome\n')
    else:
        print(f"{word} is not a palindrome\n")

filepath = Path('palindrome.txt')

fh = open(filepath,'r')



for word in fh:
    PalindromeChecker(word)


