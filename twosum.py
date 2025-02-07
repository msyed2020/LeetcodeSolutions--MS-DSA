# 1. Two Sum

def twoSum(arr, target):
    h = {}
    for i, j in enumerate(arr):
        val = target - j
        if val in h:
            return [h[val], i]
        else:
            h[j] = i
    return

print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))
print(twoSum([4,5,6,7], 11))