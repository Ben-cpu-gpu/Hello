# def is_palindrome(s):
#     return s == s[::-1]

# s1 = "level"
# s2 = "cool"
# s3 = "Madam"
# s4 = "Guys"

# print(f"is {s1} a palindrome? {is_palindrome(s1)}")
# print(f"is {s2} a palindrome? {is_palindrome(s2)}")
# print(f"is {s3} a palindrome? {is_palindrome(s3)}")
# print(f"is {s4} a palindrome? {is_palindrome(s4)}")

def is_even (n):
    return n % 2 == 0

def  sum_lower (n):
    s = 0
    while  n >= 0:
        if is_even(n):
            s += n
        s += n - 1
        return s
print (sum_lower(7))
