class Solution(object):
    def rotate(self, nums, k):
        
        n = len(nums)
        k %= n  # Handle cases where k >= n
    
        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
    
        # 1. Reverse the entire array
        reverse(0, n - 1)
        # 2. Reverse the first k elements
        reverse(0, k - 1)
        # 3. Reverse the remaining n - k elements
        reverse(k, n - 1)

        return nums
       
