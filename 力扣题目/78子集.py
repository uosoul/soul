def subsets(self, nums: List[int]) -> List[List[int]]:
        results = [[]]

        for num in nums:
                newsets = [ ]
                for re in results:
                        new_re = re + [num]
                        newsets.append(new_re)
                results.extend(newsets)
                        

def subsets(nums):
	res =[]
	for i in range(len(nums)+1):
		for tmp in itertools.combinations(nums,i):
			res.append(tmp)
	return res

        
