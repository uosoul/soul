def moveZero(nums):
        zero = 0
        for i in range(len(nums)):
                if nums[i] != 0:
                        nums[i],nums[zero] = nums[zero],nums[i]
                        zero +=1
        print(nums)


	
nums=[0,2,0,5,0,4,0,1,0,5,0]
moveZero(nums)

#第二次
def f2(nums):
        for i in range(len(nums)):
                if nums[i]==0:
                        nums.append(0)
                        nums.remove(0)#默认从前面删除零
        return nums
print(f2(nums))   #时间复杂度太高了  不建议

def f3(nums):
        m = 0
        for i in range(len(nums)):
                if nums[i] !=0:
                        nums[i],nums[m] = nums[0],nums[i]
                        m +=1
        return nums
print(f3(nums))
                        
                        
                























