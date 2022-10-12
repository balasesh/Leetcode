def removeDuplicates(nums):
    nums = list(set(nums))
    print(nums)
    print(len(list(set(nums))))
    return len(list(set(nums)))

nums = [1,1,2]
removeDuplicates(nums)
nums = [0,0,1,1,1,2,2,3,3,4]
removeDuplicates(nums)
