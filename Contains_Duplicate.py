class Solution:
    def hasDuplicate(self, nums):
        hasDuplicate = False
        for i in range (0, len(nums)):
            for j in range (i+1, len(nums)):
                if nums[i] == nums[j]:
                    hasDuplicate = True
        return hasDuplicate

nums = [1,2,3,4]
print(Solution().hasDuplicate(nums))