class Solution:
    def maxSubArray(self, nums):
        # Initialize with the first element
        global_max = nums[0]
        current_max = nums[0]

        # Iterate from the second element onwards
        for i in range(1, len(nums)):
            # Either start fresh from the current element or add it to the existing subarray
            current_max = max(nums[i], current_max + nums[i])
            # Update our running maximum
            global_max = max(global_max, current_max)

        return global_max
