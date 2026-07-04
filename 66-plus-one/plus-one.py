class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
#starting from the last index
        for i in range(n-1,-1,-1):
            if digits[i]<9:
                digits[i]+=1
                return digits
            #if the number is 9, it will become zero and 1 carry will forward
            digits[i]=0
        #concatenating 1 
        return [1]+digits
