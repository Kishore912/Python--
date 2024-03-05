def palindrome(word):
    word=word.lower()
    print("palindrome" if word == word[::-1] else "not a palindrome")
palindrome(input())    