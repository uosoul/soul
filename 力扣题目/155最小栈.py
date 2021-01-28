class minstack:
        def __init__(self):
                self.lst = []
        def push(self,x):
                self.lst.append(x)
        def pop(self):
                self.lst.pop()
        def top(self):
                return self.lst[-1]
        def getMin(self):
                return min(self.lst)
#取最小元素的时候 时间复杂度太高了！
a = minstack()
                
class MinStack:
        def __init__(self):
                self.stack = []
                self.min_stack = [math.inf]

        def push(self,x: int)->None:
                self.stack.append(x)
                self.min_stack.append(min(x,self.min_stack[-1]))

        def pop(self)->None:
                self.stack.pop()
                self.min_stack.pop()

        def top(self)->int:
                return self.stack[-1]
        def getMin(self) ->int:
                return self.min_stack[-1]

#国外的,有点长，不过不需要建立两个表，用元组的形式存储 每一次添加元素的时候的最小值
class Minstack:
        def __init__():
                self.q = []
        def push(self,x):
                curMin = self.getMin()
                if curMin ==None or x <curMin:
                        curMin = x
                self.q.append((x,curMin));
        def pop(self):
                self.q.pop()

        def top(self):
                if len(self.q)==0:
                        return None
                else:
                        return self.q[len(self.q)-1][0]
        def getMin(self):
                if len(self.q)==0:
                        return None
                else:
                        return self.q[len(self.q)-1][1]  #(元素，最小值)
                



























