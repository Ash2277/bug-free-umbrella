class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force method
        # l=[]
        # for i in range(0,len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if i!=j:
        #             a=nums[i]+nums[j]
        #             if a==target:
        #                 l=[j,i]
        # return l

        # mapping
        li = []
        c = 0
        for i in range(0, len(nums)):
            li = [nums[i], i]
        for j in range(0, len(nums)):
            b = target-nums[j]
            if(b in nums):
                c = nums.index(b)
                if c != j:
                    return [c, j]
        return -1
