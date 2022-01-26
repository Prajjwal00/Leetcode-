class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        result = [1]*N
        
        curr = 1
        for i in range(N):
            if i != 0:
                result[i]*=curr
            curr*=nums[i]
        
        curr = 1
        for i in range(N-1,-1,-1):
            if i != N-1:
                result[i]*=curr
            curr*=nums[i]
        
        return result
             
