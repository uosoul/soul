class Solution: # 两层遍历
    def letterCombinations(self, digits: str) -> List[str]:
        # chr(97)->'a'  ord('a')->97   2->97-99  3->100-102
        self.res = []
        self.m = {
        '2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'
        }
        for digit in digits:
            self.add_alp(digit)
        return self.res

    def add_alp(self, num):
            if len(self.res) == 0:
                self.res = [i for i in self.m[num]]
            else:
                tmps= [i for i in self.m[num]] 
                level = []
                for i in self.res:
                    for j in tmps:
                        level.append(i+j)
                self.res=level





class Solution(object):
    m = {
        '2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'
        }
    def dfs(self,i,digits,ans,tmp):
        if i == len(digits):
            ans.append(''.join(tmp))
            return

        for ch in self.m[digits[i]]:
            tmp.append(ch)
            self.dfs(i+1,digits,ans,tmp)
            tmp.pop()

        def letterCombinations(self,digits):
            if not digits:return []
            ans = []
            tmp = []
            self.dfs(0,digits,ans,tmp)
            return ans










            
    
