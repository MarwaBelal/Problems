#Problem4 -  Convert Number
'''
Convert number from base a to base b
Your program will take number in base a then convert it to base b
Input

Enter number
>> 234
Enter Number base
>> 6
Convert it to base
>> 8
Output
136
'''
def value(c):
    if c >= '0' and c <= '9':
        return ord(c) - ord('0')
    else:
        return ord(c) - ord('A') + 10;
		
def ToDecimal(str, base1):
    llen = len(str)
    power = 1 
    num = 0  
    for i in range(llen - 1, -1, -1):
        if value(str[i]) >= base1:
            print('Invalid Number.')
            return -1
        num += value(str[i]) * power
        power = power * base1
    return num

no1 = str(input("Enter Number "))
base1 = int(input("Enter Number base "))
base2= int(input("Convert it to base "))
dec = ToDecimal(no1,base1)

def ToAnyBase(dec, base2):
    if base2 < 2:
        return False
    remainders = []
    while dec > 0:
        remainders.append(str(dec % base2))
        dec //= base2
    remainders.reverse()
    return ''.join(remainders)

x= ToAnyBase(dec, base2)
print (x)