# ✅ 🧩 Problem: Find the Maximum Subarray Sum

# 🔹 Problem Statement:
# You are given an integer array nums.
# Your task is to find the maximum sum of any continuous subarray within the array.
# This is known as the Maximum Subarray Problem, solved using Kadane’s Algorithm.
# Return the maximum possible sum.

# ✅ Approach:
# - Initialize curr_sum as 0 and max_sum as the first element.
# - Iterate through the list of numbers:
#     - Add the current number to curr_sum.
#     - If curr_sum becomes greater than max_sum, update max_sum.
#     - If curr_sum becomes negative, reset curr_sum to 0.
# - This ensures we always track the best possible continuous subarray.
# - Time Complexity: O(n)
# - Space Complexity: O(1)


def _max_sub_array(nums):
    max_sum = nums[0]
    curr_sum = 0
   
    for x in nums:
        curr_sum += x
        
        if curr_sum > max_sum:
            max_sum = curr_sum
            
        if curr_sum < 0:
            curr_sum = 0
           
    return max_sum
    
        
if __name__== "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_sum = _max_sub_array(nums)
    print("The max valued sub array is: ",max_sum)
