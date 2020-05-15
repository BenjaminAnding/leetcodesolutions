class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        answer = []
        for i in range(len(nums)):
            remainder = target - nums[i]
            nums[i]=None
            if remainder in nums:
                answer.append(i)
                answer.append(nums.index(remainder))
                break
        return answer
