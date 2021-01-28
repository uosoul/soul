# 我写的
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:return 0
        # 滑动窗口的方法
        tmp = []
        res = []
        # s = ' '
        for i in s:
            if i not in tmp:
                tmp += i,   
            else:
                res.append(''.join(tmp))
                while tmp and i in tmp:
                    tmp.pop(0)
                tmp += i
        res.append(''.join(tmp))
        return len(sorted(res,key=lambda n: len(n))[-1])

## 答案方法
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_len = start = 0
        for index,value in enumerate(s):
            if value in used and start <= used[value] :# 关键点
                start = used[value]+1

            else:
                max_len = max(max_len,index-start+1)
            used[value]=index
        return max_len







