i_array = [-11,2, 0, 3, 4, 5, 6, 7, 8, 9, 10, 11]


# This function is using another alternate way to check for prime numbers
# Please note that , it's not the most efficient way to check for primes. Please read the comments for more information
def prime_check(prime):
    prime_result = dict()
    # Note that the python interpreter skips the rest of the code when one of the conditional statements becomes true
    for p in range(len(prime)):
        current_number = prime[p]
        if current_number == 1:
            prime_result[current_number] = "not prime"
            continue
        # from 2 to current number, when we divide and have remainder 0, that means the number has other factors
        # which is not 1, or itself
        if current_number == 2:
            prime_result[current_number] = "prime"
            continue

        # if it is 0 or negative numbers we won't count it as an applicable integers for the problem in hand
        if current_number < 1:
            prime_result[current_number] = "N/A"
            continue

        if current_number == 0:
            prime_result[current_number] = "N/A"
            continue
        # prime number principle: to find numbers of prime factors for an integer we should check 2 to
        # square root of that number: current**0.5
        # However be advised that range(start,stop,step) function does not except a floating number as its argument.
        # Furthermore, since current**0.5 is a floating number we need to use integer wrapper class int() to cast the
        # floating number in to integer: hence the for loop will be adjusted as such:
        # for x in range(2,int(current_number**0.5))
        # However since the range(start,end) is designed to exclude the end point to accurately implement the principle
        # we could add 1 to it.
        # example : current_number = 9 , square_root(9)= 3, adding 1 to square root: 3+1=4 ====> 4 is end point for
        # range function. So instead of checking from 2 to 9 , we will check 2 to 3 which is much smaller range,
        # hence making the code much more efficient by avoiding unnecessary iterations.
        for x in range(2, current_number+1):
            if current_number % x == 0:
                prime_result[current_number] = "not prime"
                # important break-statement
                # Example 4 is not prime: factors=1,2,4; if we don't break out of the loop
                # we will have 4 / 5,4/6 and so on..... which eventually makes our code
                # to branch off to the else statement for prime , and the result will inaccurately
                # conclude that 4 is prime
                # break statement breaks the current iteration of the inner loop
                break
            else:
                prime_result[current_number] = "prime"
    print("Prime Check(No Square Root Principle): ",prime_result)


def prime_check_principle(array):
    primes = {}
    for i in array:
        if i < 0:
            primes[i]="N/A-Complex Number"

            # crucial use of "continue"
            # Basically, when interpreter encounter "continue", it will skip anything underneath it and GOES to the next
            # iteration
            continue

        if i == 1:
            primes[i] = "N/A-1 is not prime"
        if i==2:
            primes[i] = "prime"

        for j in range(2, int(round(i ** 0.5))+1):
            if i % j == 0:
                primes[i] = "not prime"
                break
            else:
                primes[i] = "prime"
    return primes




prime_check(i_array)

out_put = prime_check_principle(i_array)
print("Prime_Check_Principle: ",out_put)