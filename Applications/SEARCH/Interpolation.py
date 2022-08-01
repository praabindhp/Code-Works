def interpolationSearch(arr, lo, hi, x):

	if (lo <= hi and x >= arr[lo] and x <= arr[hi]):

		pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) *
					(x - arr[lo]))

		if arr[pos] == x:
			return pos

		if arr[pos] < x:
			return interpolationSearch(arr, pos + 1,
									hi, x)

		if arr[pos] > x:
			return interpolationSearch(arr, lo,
									pos - 1, x)
	return -1

n = int(input("Enter Number Of Elements : "))

n_arr = input().split()
arr = []
for i in n_arr:
    arr.append(int(i))

x = int(input("Enter The Element To Be Searched : "))
index = interpolationSearch(arr, 0, n - 1, x)

if index != -1:
	print ("Element Present At Index : {0}".format(index))
else:
	print ("Element Not Found")