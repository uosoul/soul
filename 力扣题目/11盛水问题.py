#我写的，时间复杂度过高。

def maxArea(self, height):# -> int:: List[int]
        area = []
        for i in range(len(height)+1):
                for k in range(i+1,len(height)+1):
                        area.append((k-i)*min(height[i],height[k]))
        return max(area)

def maxArea(self, height ): #-> int:List[int]
        i, j =0, len(height)-1
        water = 0
        while i<j:
                water = max(water,(j-i)*min(height[i],height[j]))
        if height[i] < height[j]:
                i +=1
        else:
                j -= 1
        return water


#第二次写
lst=[1,8,6,2,5,4,8,3,7]
def f1(list1):
        max1=0
        for i in range(len(list1)-1):
                for j in range(i+1,len(list1)):
                        max1 = max(max1,(j-i)*min(list1[i],list1[j]))
        return max1
print(f1(lst))

def f2(list1):
        max1 = 0
        l, r = 0, len(list1)-1
        while l<r:
                max1 = max(max1,(r-l)*min(list1[l],list1[r]))
                if list1[l]<list1[r]:
                        l +=1
                else:
                        r -=1
        return max1
print(f2(lst))

























