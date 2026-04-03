class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        numdup = 0
        for el in nums:
            if el not in dic:
                dic[el] = 1
            else:
                dic[el]+=1
    
        for value in dic.values():
            if value > numdup:
                numdup = value
            
        if numdup > 1:
            return True
        else:
            return False 
    





