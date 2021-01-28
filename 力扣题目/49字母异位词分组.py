def groupAnagrams(strs):
        dic = {}
        for s in strs:
                keys = ''.join(sorted(s))
                if keys not in dic:
                        dic[keys] = [s]
                else:
                        dic.[keys].append(s)
        return dic

def groupAnagrams(self,strs):
        dic = {}
        for item in sorted(strs):
                sortedItem =''.join(sorted(item))
                dic[sortedItem] = dic.get(sortedItem, [ ]) + [item]
        return dic.values()
# 这样就不用使用if else语句 get【返回值，预设值】
