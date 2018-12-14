#Problem1 - Median
'''Given: A positive integer and an array A[1..n] of integers a positive number k≤n
Return: The k-th smallest element of A
Sample Input
11
2 36 5 21 8 13 11 20 5 4 1
8
Sample Output
13'''

number_array=list()
number = input("Enter the length of the array: ")
print('Enter the elements')
for i in range(int(number)):
    n=input("number :")
    number_array.append(int(n))
k = int(input("Enter k: "))
    
def kSmallest(array, k):
	# Sort the given array
	array.sort()
	print ("The kth smallest element is: ", array[k-1])
kSmallest(number_array, k)