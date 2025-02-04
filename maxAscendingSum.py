# 1800. Maximum Ascending Subarray Sum

def maxAscendingSum(self, nums: list[int]) -> int:
    curr = res = nums[0]
    for i in range(1, len(nums)):
        curr = curr + nums[i] if nums[i] > nums[i-1] else nums[i]
        res = max(res, curr)
    return res