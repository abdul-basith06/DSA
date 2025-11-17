# 🧠 Problem: Longest Palindromic Substring
# 🔹 Problem Statement:
# Given a string s, return the longest palindromic substring in s.
#
# Example:
# Input: "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
#
# Constraints:
# - Use the expand-around-center technique.
# - Time Complexity: O(n²)
# - Space Complexity: O(1)
###

# ✅ Approach:
# - Treat each index as the center of two palindromes:
#       1. Odd-length (center at i)
#       2. Even-length (center between i and i+1)
# - Expand outward while characters match.
# - Track the longest palindrome found.
# - Time Complexity: O(n²), Space Complexity: O(1)


def expand(s, left, right):
    # Expand outward while valid and matching
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    # Return the palindrome found
    return s[left + 1:right]


def longest_palindrome(s):
    longest = ""

    for i in range(len(s)):
        # Odd-length palindrome
        odd = expand(s, i, i)

        # Even-length palindrome
        even = expand(s, i, i + 1)

        # Pick the longer one
        longest = max(longest, odd, even, key=len)

    return longest


if __name__ == "__main__":
    s = "babad"
    result = longest_palindrome(s)
    print(f"The longest palindromic substring of '{s}' is: {result}")
