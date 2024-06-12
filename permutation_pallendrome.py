"""
Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false
Example 2:

Input: "aab"
Output: true
Example 3:

Input: "carerac"
Output: true
"""




class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = 0
        for ch in range(128):
            ct = 0
            for j in s:
                if j == chr(ch):
                    ct += 1
            count += ct % 2

        return count <= 1
