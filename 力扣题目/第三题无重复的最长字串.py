"""给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度"""
string = "pwwkew"
def Shortest_str(s):
        li = [0]
        n = 0
        str1 = s
        while n < len(str1):
            s = str1[n:]
            print(s)
            m = ''
            for i in s:
                if i not in m:
                    m +=i
                else:
                    li.append(len(m))
                    m = i
            li.append(len(m))
            n +=1
        return max(li)
print(Shortest_str(string))
#这种方法时间复杂度太高




#另一种
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        if len(s) == 1:
            return 1

        def find_left(s, i):
            tmp_str = s[i]
            j = i - 1
            while j >= 0 and s[j] not in tmp_str:
                tmp_str += s[j]
                j -= 1
            return len(tmp_str)
        length = 0
        for i in range(0, len(s)):
            length = max(length, find_left(s, i))
        return length

























