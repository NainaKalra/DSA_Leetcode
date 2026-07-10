class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        #dict to remember how many times a no came
        sum_map = {0: 1}
        
        for num in nums:
            #adding no to prefix sum
            current_sum += num
            
            #if (current_sum - k) was already there
            if (current_sum - k) in sum_map:
                #it means there was a subarray in bw whose sum was k 
                count += sum_map[current_sum - k]
                
            #adding
            sum_map[current_sum] = sum_map.get(current_sum, 0) + 1
            
        return count