def go_stair(n):
        if n<=3:
                return n
        f1,f2, f3 = 1,2,3
        for i in range(4,n+1):
                f1, f2, = f2, f3
                f3 = f1+f2
        return f3
print(go_stair(6))
                
#答案
def climbStairs(n):
        if (n<=2): return n
        f1, f2, f3 = 1, 2, 3
        for i in range(3,n+1):
                f3 = f1+ f2
                f1 = f2
                f2 = f3
        return f3
                        
