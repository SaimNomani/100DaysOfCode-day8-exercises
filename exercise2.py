# You need to write a function that checks whether if the number passed into it is a prime number or not.
#
# e.g. 2 is a prime number because it's only divisible by 1 and 2.
#
# But 4 is not a prime number because you can divide it by 1, 2 or 4.
# Example Input 1
# 73
# Example Output 1
# It's a prime number.
# Example Input 2
# 75
# Example Output 2
# It's not a prime number.

number = int(input("enter number: "))


def is_prime_checker(num):
    is_prime = True
    for n in range(2, num):
        if num % n == 0:
            is_prime = False
            break
    if is_prime:
        print("prime number")
    else:
        print("not a prime number")


is_prime_checker(num=number)
