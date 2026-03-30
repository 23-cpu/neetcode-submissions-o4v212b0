class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = 0
        
        for r in range(0,len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                l = l+1
        return l
        