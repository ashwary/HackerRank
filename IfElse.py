# Given an integer, , perform the following conditional actions:
#
# If N is odd, print Weird
# If N is even and in the inclusive range of 2  to 5, print Not Weird
# If N is even and in the inclusive range of  to , print Weird
# If N is even and greater than , print Not Weird

N = int(input().strip())

if N%2 != 0 or 5<N<21:
    print("WEIRD")
else:
    print("NOT WEIRD")

