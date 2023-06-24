import random

# Example1:
# Ask the user for two integer n and m where m>n.
# Create a list x of size n. Populate the list with n random integers in the range 1through m.

input("Enter the following numbers where m > n")
n1 = int(input("Enter first number (n): "))
n2 = int(input("Enter second number (m): "))


def random_integer(n, m):
    x = list(range(n))
    for j in range(3):
        for i in range(len(x)):
            # print(i)
            r = random.randrange(1, m)
            x[i] = r
        print(x)


# Example 2:
# Modify the answer to the problem above so that all of the integers in list x are unique.
def random_unique_integer(n, m):
    x = list(range(n))
    for j in range(3):
        for i in range(len(x)):
            # print(i)
            r = random.randrange(1, m)
            if r not in x:
                x[i] = r
            else:
                while r in x:
                    r = random.randrange(1, m)
                x[i] = r
        print(x)


random_unique_integer(n1, n2)
