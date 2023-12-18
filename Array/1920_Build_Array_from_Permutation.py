nums = [5, 4, 0, 1, 2, 3]

class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        return [nums[i] for i in nums]


ans = Solution()
print(ans.buildArray(nums))