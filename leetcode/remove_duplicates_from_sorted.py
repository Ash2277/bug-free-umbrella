class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 1; prev = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[prev]:
                nums[idx] = nums[i]
                prev=idx
                idx += 1
        return idx