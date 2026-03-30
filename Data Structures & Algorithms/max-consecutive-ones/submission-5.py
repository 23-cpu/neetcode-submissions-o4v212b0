class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cons = 0
        old_cons = 0
        max_val = 0 
        
        for el in nums:
            if el == 1:
                cons+=1
            elif el == 0:
                old_cons = cons
                cons = 0
                continue
            
            if cons > max_val:
                max_val = cons
        return max_val