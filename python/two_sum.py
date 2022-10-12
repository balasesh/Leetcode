def twoSum(nums, target):
    index_map = {}
    result = []
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in index_map:
            result.append(index_map.get(diff))
            result.append(i)
        else:
            index_map[nums[i]] = i
    return result

nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))
nums = [3,2,4]
target = 6
print(twoSum(nums, target))
nums = [3,3]
target = 6
print(twoSum(nums, target))