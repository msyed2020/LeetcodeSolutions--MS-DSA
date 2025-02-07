def isArraySpecial(nums: list[int]) -> bool:
    if len(nums) == 1:
        return True
    for i in range(len(nums)-1):
        if (nums[i] % 2 == 0 and nums[i + 1] % 2 == 0) or (nums[i] % 2 == 1 and nums[i + 1] % 2 == 1):
            return False
    return True

print(isArraySpecial([1]))
print(isArraySpecial([2,1,4]))
print(isArraySpecial([4,3,1,6]))
print(isArraySpecial([1,2,3,4,5]))