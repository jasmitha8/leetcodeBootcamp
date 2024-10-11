class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        output = [1] * len(nums)
        
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]

        for j in range(len(nums) - 2, -1, -1):
            postfix[j] = postfix[j+1] * nums[j+1]

        for i in range(len(nums)):
            output[i] = prefix[i] * postfix[i]

        return output
    

class OptimizedSolution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        prefix, postfix = 1, 1

        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
        
        for j in range(len(nums) - 1, -1, -1):
            output[j] *= postfix
            postfix *= nums[j]

        return output
