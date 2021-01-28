def largestRectangleArea(heights: List[int]) -> int:
        res = 0
        n = len(heights)
        for i in range(n):
                left_i = i
                right_i =i
                while left_i >=0 and height[left_i]>=height[i]:
                        left_i -=1
                while right_i >=0 and height[right_i]>=height[i]:
                        right_i +=1
                res =max(res,(right_i-left_i -1)*height[i])
        return res        


def largestRectangleArea(heights: List[int]) -> isnt:
        res = 0
        lst1 = [(-1,-1)]

        for i, j in enumerate(heights):
                while j < lst1[-1][1]:#末尾的最后一个元素
                        a = lst1.pop() #a[1]是高度
                        res = max(res, a[1]*(i - lst1[-1][0] -1 ))
                lst1.append((i, j)) #记录下表和值

        while len(lst1) != 1 :# 如果stack有剩余的话，右边界一定是len(height)  
                b = lst1.pop()
                res = max(res, b[1]*(len(heights) - lst1[-1][0] -1))
        return res





















        
