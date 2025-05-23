"""
# Time Complexity :
- O(n), where n is the number of houses

# Space Complexity :
- O(1), using two variables instead of a full dp array

# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        prev1, prev2 = 0, 0

        for num in nums:
            temp = prev1
            prev1 = max(prev2 + num, prev1)
            prev2 = temp

        return prev1

