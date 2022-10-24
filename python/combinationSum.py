def combinationSum(candidates, target):
    combinations = []
    temp = []

    candidates = sorted(list(set(candidates)))
    findNumbers(combinations, candidates, temp, target, 0)
    return combinations


def findNumbers(ans, candidates, temp, target, index):
    if (target == 0):
        ans.append(list(temp))
        return

    for i in range(index, len(candidates)):
        if (target - candidates[i]) >= 0:
            temp.append(candidates[i])
            findNumbers(ans, candidates, temp, target-candidates[i], i)
            temp.remove(candidates[i])


candidates = [2, 3, 6, 7]
target = 7
print(combinationSum(candidates, target))
# candidates = [2, 3, 5]
# target = 8
# print(combinationSum(candidates, target))
# candidates = [2]
# target = 1
# print(combinationSum(candidates, target))
