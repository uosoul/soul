def isValid(s):
        dic{"{":"}",'[':']','(':')','?':'?'}
        stack = ['?'] # ?的意思是排除 第一个是右括号的情况！！
        for c in s:
                if c in dic:stack.append(c)
                elif dic[stack.pop()] != c: return False
        return len(stack) == 1










def getvalid(s):
        dict={'[':']','{': '}','(':')',  }

























