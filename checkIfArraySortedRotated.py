def check(self, nums: list[int]) -> bool:
        count, n = 0, len(nums)
        for i in range(n):
            if nums[i] > nums[(i+1) % n]:
                count += 1
                if count > 1: return False
        return True

print(check([3,4,5,1,2]))
print(check([2,1,3,4]))
print(check([1,2,3]))
print(check([1,2,3,4,5]))
print(check([3,3,3]))