import collections

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)


ans = Solution()
print(ans.majorityElement([2, 2, 1, 1, 1, 2, 2]))