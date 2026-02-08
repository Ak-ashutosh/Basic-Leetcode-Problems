class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

      #Write code here
        res = {}

        for i, j in enumerate(nums):
            diff = target - j

            if diff in res:
                return [res[diff], i]

            res[j] = i
