def check(s):
    return s == s[::-1]

s = input("Enter a string: ")

if check(s):
    print("Palindrome")
else:
    print("Not a palindrome")