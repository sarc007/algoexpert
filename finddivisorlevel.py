"""
Divisior problem asked by exceptionally Find the divsors levels for a given number, for example 8-->4-->2, so for 8
the divisors are 4 and 2 (2 is prime) Find the divsors levels for a given number, for example 63-->7,
so for 63 the divisors are 9 and 7 (and 7 is prime)
[divisor levels: number] --> 1 : 0, 2 : 0, 3 : 0, 4 : 1, 8 : 2, 12 : 2, 24 : 3, 48 : 4, 63 : 2, 9 : 1, 128 : 6, 96 : 5
6666 : 3, 128476 : 2, 32119 : 0
"""

number_list = [1, 2, 3, 4, 8, 12, 24, 48, 63, 9, 101, 128, 96, 6666, 128476, 32119]
# number_list = [48, 101]
plist = []
def is_prime(num):
    # primelist = [0]
    if num > 1:
        # Iterate from 2 to n / 2
        for i in range(2, int(num / 2)+1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                plist.append(0)
                is_prime(num / i)
                break

                # print(num, "is not a prime number")
                # if (i % 2) == 0 and i >= (num/i):
                #     is_prime(())
                # elif ((num/i) % 2) == 0 and (num/i) >= i:
                #     is_prime(i)
                # elif (i % 2) == 0 and ((num/i) % 2) > 0:
                #     is_prime(i)
                # elif (i % 2) > 0 and ((num/i) % 2) == 0:
                #     is_prime(num/i)
                # else:
                #     is_prime(i)


        # else:
        #     primelist.append(1)
    return 0


for number in number_list:
    # number = int(number_str)
    # if number % 2 == 0:
    #     print(str(number) + ' : ' + str(len(is_prime(number)) - 2))
    # else:
    #     print(str(number) + ' : ' + str(len(is_prime(number)) - 1))
    is_prime(number)
    print(str(number) + ' : ' + str(len(plist)))
    plist = []
# def check_num(num):
#     if num > 1:
#         # Iterate from 2 to n / 2
#         i = int(num / 2) + 1
#         while i > 1:
#
#             # If num is divisible by any number between
#             # 2 and n / 2, it is not prime
#             if (num % i) == 0:
#                 # print(num, "is not a prime number")
#                 divisorlist.append(i)
#                 check_num()
#             i = i - 1
#         else:
#             return result
#
#     else:
#         return result
# print(check_num(number))
# print(divisorlist)
