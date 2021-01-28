#第一种暴力求解法

lst1 = [-1,0,1,2,-1,-4]
def three_sum(lst):
        sum1 = []
        for i in range(len(lst)-2):
                for j in range(i+1,len(lst)-1):
                        for k in range(j+1,len(lst)):
                                if lst[i]+lst[j]+lst[k] == 0:
                                        sum1.append([lst[i], lst[j], lst[k]])
        return sum1
print(three_sum(lst1))


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        lst = []

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l , r = i+1,len(nums)-1
            while l < r:
                s = nums[i] + nums[l]+nums[r]
                if s < 0:
                    l+=1
                elif s>0:
                    r-=1
                else:
                    lst.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l] == nums[l+1]:
                        l +=1
                    while l<r and nums[r] == nums[r-1]:
                        r -=1
                    l +=1; r -=1
        return lst
        





















