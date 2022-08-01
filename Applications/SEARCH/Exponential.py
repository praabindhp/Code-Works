def binarySearch( n_arr, l, r, x):
	if r >= l:
		mid = l + ( r-l ) // 2

		if n_arr[mid] == x:
			return mid

		if n_arr[mid] > x:
			return binarySearch(n_arr, l,
								mid - 1, x)

		return binarySearch(n_arr, mid + 1, r, x)
		
	return -1

def exponentialSearch(n_arr, n, x):

	if n_arr[0] == x:
		return 0
		
	i = 1
	while i < n and n_arr[i] <= x:
		i = i * 2

	return binarySearch( n_arr, i // 2,
						min(i, n-1), x)
	
n = int(input("Enter Number Of Elements : "))

arr = input().split()
n_arr = []
for i in arr:
    n_arr.append(int(i))
    
x = int(input("Enter The Element To Be Searched : "))
result = exponentialSearch(n_arr, n, x)
if result == -1:
	print ("Element Not Found")
else:
	print ("Element Present At Index : {0}".format(result))