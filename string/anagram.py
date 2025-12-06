# 🧠 Problem: Check if Two Strings Are Anagrams
# 🔹 Problem Statement:
# Write a function that takes two strings as input and returns True if they are anagrams of each other.
# Two strings are anagrams if they contain the same characters with the same frequency, ignoring spaces and case.
#
# Example:
# are_anagrams("Listen", "Silent")     # → True
# are_anagrams("Hello", "Bello")       # → False
# are_anagrams("Dormitory", "Dirty room")  # → True
# are_anagrams("python", "java")       # → False
#
# Constraints:
# - Time Complexity: O(n)
# - Space Complexity: O(1) if we assume a fixed alphabet
# - Handle spaces and case-insensitivity

# ✅ Approach:
# 1. Normalize the strings: remove spaces and convert to lowercase.
# 2. Quickly return False if lengths differ.
# 3. Count character frequencies for the first string.
# 4. Decrease counts while iterating through the second string.
# 5. If a character is missing or overused, return False.
# 6. Otherwise, return True.


def _are_anagrams(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    if len(s1) != len(s2):
        return False
    
    counts = {}
    for char in s1:
        counts[char] = counts.get(char, 0) + 1

    for char in s2:
        if char not in counts or counts[char] == 0:
            return False
        counts[char] -= 1

    return True
        

# ✅ Test cases
if __name__ == "__main__":
    test_cases = [
        ("Listen", "Silent"),
        ("Hello", "Bello"),
        ("Dormitory", "Dirty room"),
        ("python", "java")
    ]

    for s1, s2 in test_cases:
        result = _are_anagrams(s1, s2)
        print(f"are_anagrams('{s1}', '{s2}') → {result}")