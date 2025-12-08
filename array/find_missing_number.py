# Problem: Find the Missing Number
# Problem Statement
# Given an array nums containing n distinct integers in the range [0, n],
# return the only number in the range that is missing from the array.

# Example:
# Input: nums = [3, 0, 1]
# Output: 2

# Input: nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
# Output: 8

# Approach (Math / Gauss Formula - O(n) Time, O(1) Space):
# - The sum of numbers from 0 to n is exactly: n * (n + 1) // 2
# - Calculate the expected sum using the formula.
# - Calculate the actual sum of the given array.
# - Return the difference → that’s the missing number!
# - Super fast and uses constant extra space.


def find_missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


# Test
if __name__ == "__main__":
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    result = find_missing_number(nums)
    print(f"Input:  nums = {nums}")
    print(f"Output: {result}")
