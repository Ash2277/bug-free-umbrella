# more time less space
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        lst = [0]*(max(nums)+1)
        for i in nums:
            lst[i] = lst[i]+1

        return lst.index(max(lst))

# more space less time


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        i = nums[0]
        a = []
        b = []
        b.append(i)
        a.append(nums.count(i))
        for j in nums:
            if not j == i:
                i = j
                a.append(nums.count(i))
                b.append(i)
        c = max(a)
        d = a.index(c)
        return b[d]
