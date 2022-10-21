class Solution(object):
    def search(self, nums, target):
        x = 0
        while x != len(nums):
            for i in nums:
                x += 1
                if i == target:
                    return x - 1
        return -1