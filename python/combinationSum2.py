from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def findCombinations(temp, index, target):
            # print (temp, target, index)
            if target == 0:
                res.append(list(temp))
            if target <= 0:
                return
            prev = -1
            for i in range(index, len(candidates)):
                if candidates[i] == prev:
                    continue
                temp.append(candidates[i])
                findCombinations(temp, i+1, target - candidates[i])
                temp.remove(candidates[i])
                prev = candidates[i]
        findCombinations([], 0, target)
        return res

s = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8
print(s.combinationSum2(candidates, target))
candidates = [2, 3, 6, 7]
target = 7
print(s.combinationSum2(candidates, target))

candidates = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
              1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
target = 30
print(s.combinationSum2(candidates, target))


candidates = [2, 3, 5]
target = 8
print(s.combinationSum2(candidates, target))
candidates = [2]
target = 1
print(s.combinationSum2(candidates, target))
