#Problem2 - Find Factors of Number
'''Write a program that get factors of a number and display it.
Input
>> 20
Output

The factors of 20 are:
1
2
4
5
10
20'''

def FindFactors(x):
   # This function takes a number and prints the factors
   x = int(input("Enter The Number you want its factors: "))
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)
num = 20
FindFactors(num)