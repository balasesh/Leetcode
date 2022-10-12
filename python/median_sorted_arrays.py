class Solution:

	# Method to find median
	def Median(self, A, B):
	
		# Assumption both A and B cannot be empty
		n = len(A)
		m = len(B)
		if (n > m):
			return self.Median(B, A) # Swapping to make A smaller

		start = 0
		end = n
		realmidinmergedarray = (n + m + 1) // 2

		while (start <= end):
			mid = (start + end) // 2
			leftAsize = mid
			leftBsize = realmidinmergedarray - mid
			
			# checking overflow of indices
			leftA = A[leftAsize - 1] if (leftAsize > 0) else float('-inf')
			leftB = B[leftBsize - 1] if (leftBsize > 0) else float('-inf')
			rightA = A[leftAsize] if (leftAsize < n) else float('inf')
			rightB = B[leftBsize] if (leftBsize < m) else float('inf')

			# if correct partition is done
			if leftA <= rightB and leftB <= rightA:
				if ((m + n) % 2 == 0):
					return (max(leftA, leftB) + min(rightA, rightB)) / 2.0
				return max(leftA, leftB)*1.0

			elif (leftA > rightB):
				end = mid - 1
			else:
				start = mid + 1

# Driver code
ans = Solution()
arr1 = [-5, 3, 6, 12, 15]
arr2 = [-12, -10, -6, -3, 4, 10]
print("Median of the two arrays is {}".format(ans.Median(arr1, arr2)))

# This code is contributed by Arpan


nums1 = [1, 3]
nums2 = [2]
print('Median : 2.0 Answer: ' + str(ans.Median(nums1, nums2)))
nums1 = [1, 2]
nums2 = [3, 4]
print('Median : 2.5 Answer: ' + str(ans.Median(nums1, nums2)))
nums1 = [2, 3, 5, 8]
nums2 = [10, 12, 14, 16, 18, 20]
print('Median : 11.0 Answer: ' + str(ans.Median(nums1, nums2)))


# Let’s take an example to understand this
# Input :arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10},
#            brr[] = { 11, 12, 13, 14, 15, 16, 17, 18, 19 }

# Recursive call 1:
# smaller array[] = 1 2 3 4 5 6 7 8 9 10, mid = 5
# larger array[] = 11 12 13 14 15 16 17 18 19 , mid = 15

# 5 < 15
# Discard first half of the first array and second half of the second array

# Recursive call 2:
# smaller array[] = 11 12 13 14 15, mid = 13
# larger array[] = 5 6 7 8 9 10, mid = 7

# 7 < 13
# Discard first half of the second array and second half of the first array

# Recursive call 3:
# smaller array[] = 11 12 13 , mid = 12
# larger array[] = 7 8 9 10 , mid = 8

# 8 < 12
# Discard first half of the second array and second half of the first array

# Recursive call 4:
# smaller array[] = 11 12
# larger array[] = 8 9 10

# Size of the smaller array is 2 and the size of the larger array is odd
# so, the median will be the median of max( 11, 8), 9, min( 10, 12)
# that is 9, 10, 11, so the median is 10.

# Output:10.000000
