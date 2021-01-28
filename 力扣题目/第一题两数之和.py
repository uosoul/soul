"""给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个整数，
并返回他们的数组下标。你可以假设每种输入只会对应一个答案。
但是，数组中同一个元素不能使用两遍。"""

#第1种方法，暴力的解法，时间复杂度
def find_target(lst,target):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]+lst[j] == target:
                return [i, j]
    return [-1, -1]




#第2种 哈希表
class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        keys = { }
        for i, v in enumerate(nums):
            if target-v in keys:
                return [keys[target-v], i]
            else:
                keys[v] = i
        return None


lst = [1,2,3,5]
target = 5
#哈希表
def twosums(lst,target):
    if len(lst)<=1:
        return None
    dict1 = { }
    for i,j in enumerate(lst):
        if str(target-j) in dict1:          
            return [dict1[str(target-j)],  i]
        else:
            dict1[str(j)] = i
    return None
            
print(twosums(lst,target))       















































