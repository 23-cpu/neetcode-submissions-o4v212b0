class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightmax = -1
        for i in range(len(arr)-1, -1,-1):
            oldie = arr[i]
            arr[i] = rightmax
            rightmax = max(oldie,rightmax)
        return arr
        