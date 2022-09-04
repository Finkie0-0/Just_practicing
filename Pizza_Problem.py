"""Checks if the given, positive number, is in fact a palindrome"""

def palindrome(N):
    x = list(str(N))
    if (x[:] == x[::-1]):
        return True
    else:
        return False

"""Reverses the given positive integer"""

def reverse_int(N):
    r = str(N)
    x = r[::-1]
    return int(x)


def palindrome_generator():
    recieve = int(input("Enter a positive integer. "))
    if (palindrome(recieve) == True):
        print(recieve, " is a palindrome!")
    else:
        print("Generating a palindrome...")
        while palindrome(recieve) == False:
            reverse_int(recieve) + recieve











