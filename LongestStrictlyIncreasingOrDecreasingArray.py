def longestMonotonicSubarray(self, nums: list[int]) -> int:
        n, ans, inc, dec=len(nums), 0, 1, 1
        if n==1: return 1
        for i in range(1, n):
            if nums[i]>nums[i-1]:
                inc+=1
                dec=1
            elif nums[i]<nums[i-1]:
                inc=1
                dec+=1
            else:
                inc=dec=1
            ans=max(ans, dec, inc)
        return ans

print(longestMonotonicSubarray([1,4,3,3,2]))
print(longestMonotonicSubarray([3,3,3,3]))
print(longestMonotonicSubarray([3,2,1]))
print(longestMonotonicSubarray([1,1,1,1]))
print(longestMonotonicSubarray([2,2,2,2]))