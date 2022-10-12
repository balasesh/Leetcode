def searchRange(nums, target):
    result = [-1,-1]
    for i in range(len(nums)):
        if nums[i] == target and result[0] == -1:
            result[0] = i
        if nums[-(i+1)] == target and result[1] == -1:
            result [1] = len(nums) - (i+1)
        if result[0] > -1 and result[1] > -1:
            break
    return result
    
nums = [5,7,7,8,8,10]
target = 8
print(searchRange(nums, target))
nums = [5,7,7,8,8,10]
target = 10
print(searchRange(nums, target))
nums = []
target = 0
print(searchRange(nums, target))