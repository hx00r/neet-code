class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        resMap = {}
        # x = target - cur
        for idx, number in enumerate(nums):
            res = target - number
            if res in resMap:
                return [resMap[res], idx]
            resMap[number] = idx
            