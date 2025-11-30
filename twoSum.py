class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         
        hash = {}

        for i in range (len(nums)):
            hash[nums[i]] = i
        
        for i in range (len(nums)):
            diff = target - nums[i]
            print(diff)
            if (diff in hash):
                if ( i != hash.get(diff)): 
                    return [i,hash.get(diff)]
            
        return []

