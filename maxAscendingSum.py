# 1800. Maximum Ascending Subarray Sum

def maxAscendingSum(self, nums: list[int]) -> int:
    curr = res = nums[0]
    for i in range(1, len(nums)):
        curr = curr + nums[i] if nums[i] > nums[i-1] else nums[i]
        res = max(res, curr)
    return res

print(maxAscendingSum([10,20,30,5,10,50]))
print(maxAscendingSum([10,20,30,40,50]))
print(maxAscendingSum([12,17,15,13,10,11,12]))