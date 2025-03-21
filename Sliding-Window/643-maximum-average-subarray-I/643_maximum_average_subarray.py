class Solution(object):
    def findMaxAverage(self, nums, k):
        max_sum = float(sum(nums[:k]))
        curr_sum = max_sum
        
        for i in range(k, len(nums)):
            curr_sum += nums[i] - nums[i-k] 
            max_sum = max(max_sum, curr_sum)
        
        return max_sum / k