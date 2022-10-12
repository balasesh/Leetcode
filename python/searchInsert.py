def searchInsert(nums, target):
    position = -1
    for i in range(len(nums)):
        if (nums[i] == target) or (nums[i] > target):
            position = i
            break
    if position < 0 : 
        return len(nums)
    else:
        return position
nums = [1,3,5,6]
target = 5
print(searchInsert(nums, target))
nums = [1,3,5,6]
target = 2
print(searchInsert(nums, target))
nums = [1,3,5,6]
target = 7
print(searchInsert(nums, target))