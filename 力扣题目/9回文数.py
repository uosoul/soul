def isPalindrom(x):
    if x<0:return False
    p,res =x,0
    while p:
        res = res*10+p%10
        p = int(p/10)
