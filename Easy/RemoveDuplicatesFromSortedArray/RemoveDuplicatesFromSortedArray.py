class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        if n < 2:
            return n
        
        i, j = 0, 1
        
        while j < n:
            if nums[i] != nums[j]:
                i += 1
            
            nums[i] = nums[j]
            j += 1
        
        return i+1
