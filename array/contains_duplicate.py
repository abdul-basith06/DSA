# 🧠 Problem: Contains Duplicate
# 🔹 Problem Statement:
# Given an integer array nums, return true if any value appears more than once
# in the array, otherwise return false.
#
# Example 1:
# Input: nums = [1, 2, 3, 3]
# Output: true
#
# Example 2:
# Input: nums = [1, 2, 3, 4]
# Output: false
#
# Constraints:
# - Solve efficiently
# - Aim for optimal time complexity
###

# ✅ Approach:
# - Think about how to track elements you've already seen
# - Compare current element with previously seen elements
# - If a duplicate is found → return True
# - If loop completes → return False
# - Optimize using appropriate data structures


def contains_duplicate(nums):
    seen = set()
    for i in nums:
        if i in seen:
            return True
        else:
            seen.add(i)
    return False
        

if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    result = contains_duplicate(nums)
    print(f"Does the array contain duplicates? {result}")