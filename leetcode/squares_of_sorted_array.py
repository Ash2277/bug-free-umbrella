class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        lst = []
        for i in nums:
            lst.append(i*i)
        lst.sort()
        return lst
