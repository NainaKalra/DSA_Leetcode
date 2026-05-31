class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        current_whites = blocks[:k].count('W')
        min_whites = current_whites
    
        for i in range(k, len(blocks)):
            if blocks[i] == 'W':
                current_whites += 1
            if blocks[i - k] == 'W':
                current_whites -= 1
            
            min_whites = min(min_whites, current_whites)
        
        return min_whites