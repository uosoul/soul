def FB(n):
        F,S = 1,1
        if n <=2:
                return 1
        for i in range(n-2):
                sum1 = F+S
                print(F,S,sum1)
                F,S = S,sum1
                
        return sum1

def F(n):
        if n==1 or n==2:
                return 1
        return F(n-1)+F(n-2)
print(F(3),F(4),F(5))
        
