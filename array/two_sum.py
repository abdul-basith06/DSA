# 🧠 Problem: Two Sum
# 🔹 Problem Statement
# Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
###
# 🔸 Example:
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
# Explanation: nums[0] + nums[1] == 2 + 7 == 9
###
# ✅ Approach (Hash Map - O(n) Time, O(n) Space):
# - Use a dictionary (hash map) to store numbers and their indices as we iterate.
# - For each number, compute its complement: `target - num`.
# - If the complement is already in the map, return its index and current index.
# - Else, store the number with its index in the map.
# - This avoids nested loops and ensures linear time.

def two_sum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in lookup:
            return (lookup[diff], i)
        lookup[num] = i
    return []

if __name__ == "__main__":
    nums = [2, 7, 11, 92]
    target = 99
    result = two_sum(nums, target)
    print(f"Input: nums = {nums}, target = {target}")
    print(f"Output: {result}")