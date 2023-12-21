# x = int(input("What's x? "))

# if x % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

# This is a longer version of this function
# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False

# This is the shorter version
def is_even(n):
    return True if n% 2 == 0 else False

# Even simpler
def is_even(n):
    return n % 2 == 0
main()