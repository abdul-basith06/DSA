# 🧠 Problem: Longest Substring Without Repeating Characters
# 🔹 Problem Statement:
# Given a string s, find the length of the longest substring that contains no repeating characters.
#
# Example:
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with a length of 3.
#
# Constraints:
# - Use the sliding window technique.
# - Time complexity should be O(n).
###

# ✅ Approach:
# - Use two pointers (`left` and `right`) to create a sliding window.
# - Use a set (`seen`) to store the unique characters currently in the window.
# - Iterate through the string using `right`:
#     - If `s[right]` is already in the set, it means we have a duplicate:
#         - Remove characters from the left side until the duplicate is gone.
#         - Increment `left` pointer accordingly.
#     - Add `s[right]` to the set.
#     - Update `max_len` as the size of the current window (`right - left + 1`).
# - This ensures we always maintain a window of unique characters.
# - Time Complexity: O(n), Space Complexity: O(n)


def longest_substring(s):
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        # If duplicate found, shrink the window from the left
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        # Add the current character to the set
        seen.add(s[right])

        # Update maximum window length
        max_len = max(max_len, right - left + 1)

    return max_len


if __name__ == "__main__":
    s = "abcabcbb"
    res = longest_substring(s)
    print(f"The length of the longest substring without repeating characters in '{s}' is: {res}")
