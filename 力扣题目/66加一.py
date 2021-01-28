class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:return [1]
        res = []
        while digits and digits[-1] == 9:
            digits.pop()
            res.append(0)
        if not digits:
            digits.append(1)
        else:
            digits[-1] +=1
        digits += res
        return digits

    
class Solution:
    def plusOne(self, digits):
        for i in range(len(digits)):
            if digits[~i] < 9:
                digits[~i] += 1
                return digits
            digits[~i] = 0
        return [1] + [0] * len(digits)
    

def plusOne(digits):
    num = 0
    for i in range(len(digits)):
    	num += digits[i] * pow(10, (len(digits)-1-i))
    return [int(i) for i in str(num+1)]


