#solution 1 : O(n2)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]



#solution 2 : o(n) 
class Solution2(object):
    def twoSum(self, nums, target):
        seen = {}
        for i , num in enumerate(nums):
            complement = target - num 
            if complement in seen :
                return [seen[complement],i]
            seen[num]=i