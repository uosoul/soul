s = 'asdsadas'
def f1(s, t):
        dict1 = {}
        for i in s:
                if i not in dict1.keys():
                        dict1[i] = 0
                else:
                        dict1[i] +=1
        print(dict1)                

f1(s,s)

def f2(s, t):
        return sorted(s)==sorted(t)

def f3(s, t):
        set_tmp = set(s)
        if set_tmp == set(t):
                for i in set_tmp:
                        result = True and s.count(i) == t.count(i)
        else:
                result =False
        return (result)
import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)

