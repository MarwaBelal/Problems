#Problem3 - Find Armstrong Number in an Interval
'''
A positive integer is called an Armstrong number of order n if
abcd... = an + bn + cn + dn + ...
For example,
153 = 1*1*1 + 5*5*5 + 3*3*3 // 153 is an Armstrong number.
Your program will take start and end interval as input then print all Armstrong number in
this interval
Input
>> 100 2000
Output
153
370
371
407
1634'''

lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

for num in range(lower, upper + 1):
    NumberOfDigits= len(str(num))
    sum = 0
    # find the sum of the cube of each digit
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** NumberOfDigits
        temp //= 10
    if num == sum:
        print(num)
