class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
            if not intervals:
                return []
            
        # Step 1: Saare intervals ko unke shuruat ke time (start time) ke hisab se sort kar do
            intervals.sort(key=lambda x: x[0])
        
            merged = [intervals[0]]  # Pehle interval ko answer list me daal do
        
            for current in intervals[1:]:
            # merged list ka ekdum aakhiri wala interval uthao
                last_merged = merged[-1]
            
            # Agar aaj wale interval ka start time, piche wale ke end time se chota ya barabar hai
                if current[0] <= last_merged[1]:
                # Toh dono ko jod do (end time badha do jo bhi dono me se bada ho)
                    last_merged[1] = max(last_merged[1], current[1])
                else:
                # Agar nahi takra rahe, toh naya interval chupchap answer me jod do
                    merged.append(current)
                
            return merged