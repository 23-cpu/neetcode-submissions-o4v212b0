class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # resize
        ans = 2*len(nums)*[0]

        # move all items from the nums to the ans, and 
        # also move what is at first index, to the,
        # l(nums)+that index positon in the ans array
        
        for i in range(0,len(nums)):
            ans[i] = nums[i]
            ans[len(nums)+i] = nums[i]
        return ans




        