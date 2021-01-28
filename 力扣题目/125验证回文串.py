class Solution:
    import re
    def isPalindrome(self, s: str) -> bool:
        if s == '':
            return True
        s = s.lower()
        regx = re.compile(r'[0-9a-zA-Z]')
        s1 = ''.join(re.findall(regx,s))
        if s1==s1[::-1]:
            return True
        else:
            return False

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(re.findall(r'[A-Za-z0-9]+', s.lower()))
        if s == s[::-1]:
            return True
        return False


#isalnum()判断是数字或者字母为True

def isPalindrome(self, s):
    l, r = 0, len(s-1)
    while l<r:
        while l<r and not s[l].isalnum():
            l +=1
        while l<r and not s[r].isalnum():
            r -=1
        if s[l].lower() != s[r].lower():
            return False
        l +=1; r -=1
    return True


#第二次
str1='param _as sds'
import re
def f1(str):
    regex = r'[a-z0-9A-Z]*'
    s1 = ''.join(re.findall(regex,str.lower()))
    if s1 == s1[::-1]:
        return True
    return False

#print(f1(str1))


class Solution:
    def isPalindrome(self, s):
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l <r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l +=1; r -= 1
        return True





























