def removeElement(nums, val):
    while len(nums)> 0:
        if val in nums:
            nums.remove(val)
        else:
            break
    return nums


nums = [3,2,2,3]
val = 3
print(removeElement(nums, val))

nums = [0,1,2,2,3,0,4,2]
val = 2
print(removeElement(nums, val))