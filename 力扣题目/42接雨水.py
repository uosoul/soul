class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        for i in range(len(height)):
            max_left, max_right = 0,0
            # 寻找 max_left
            for j in range(0,i):
                max_left = max(max_left,height[j])
            # 寻找 max_right
            for j in range(i,len(height)):
                max_right = max(max_right,height[j])
            if min(max_left,max_right) > height[i]:
                ans += min(max_left,max_right) - height[i]
        
        return ans

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        org_height = height[:]
        h_index = height.index(max(height))
        for i in range(h_index):
            if height[i] > height[i+1]:
                height[i+1] = height[i]
        for j in range(len(height)-1, h_index, -1):
            if height[j] > height[j-1]:
                height[j-1] =height[j]
        rain =sum(height) - sum(org_height)
        return rain



class Solution:
    def trap(self, height: List[int]) -> int:
        # 边界条件
        if not height: return 0
        n = len(height)

        left,right = 0, n - 1  # 分别位于输入数组的两端
        maxleft,maxright = height[0],height[n - 1]
        ans = 0

        while left < right:
            maxleft = max(height[left],maxleft)
            maxright = max(height[right],maxright)
            if maxleft < maxright:
                ans += maxleft - height[left]
                left += 1
            else:
                ans += maxright - height[right]
                right -= 1
        eun

