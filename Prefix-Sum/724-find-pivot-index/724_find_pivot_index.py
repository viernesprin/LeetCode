<<<<<<< HEAD
class Solution(object):
    def pivotIndex(self, nums):
        total_sum = sum(nums)
        left_sum = 0
    
        for i, num in enumerate(nums):
            right_sum = total_sum - left_sum - num
        
            if left_sum == right_sum:
                return i
        
            left_sum += num
            
=======
class Solution(object):
    def pivotIndex(self, nums):
        total_sum = sum(nums)
        left_sum = 0
    
        for i, num in enumerate(nums):
            right_sum = total_sum - left_sum - num
        
            if left_sum == right_sum:
                return i
        
            left_sum += num
            
>>>>>>> 217cbfda8fc661c365c68536e588296e8150d6ea
        return -1