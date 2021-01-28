class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        c = counts.most_common(1)  # 输出次数最多的形式为 （a, 10次） 
        return c[0][0]


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(),key=lambda k:counts.get(k))



# 中位数一定是多数元素
def majorityElement(nums)
        nums.sort()
        return nums[len(nums)//2]
