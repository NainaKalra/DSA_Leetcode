class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
    
        for i in range(len(s) - 2):
            a = s[i]
            b = s[i + 1]
            c = s[i + 2]
        
            if a != b and b != c and a != c:
                count += 1
            
        return count