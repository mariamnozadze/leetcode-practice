#  You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.

# Return the score of s.

 

# Example 1:

# Input: s = "hello"

# Output: 13

# Explanation:

# The ASCII values of the characters in s are: 'h' = 104, 'e' = 101, 'l' = 108, 'o' = 111. So, the score of s would be |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13.

# Example 2:

# Input: s = "zaz"

# Output: 50

# Explanation:

# The ASCII values of the characters in s are: 'z' = 122, 'a' = 97. So, the score of s would be |122 - 97| + |97 - 122| = 25 + 25 = 50.

 

# Constraints:

# 2 <= s.length <= 100
# s consists only of lowercase English letters.
 
 
class Solution(object):
    def scoreOfString(self, s):
        arr=[ord(i) for i in s]

        left, right = 0, 1
        result = 0

        while left < len(arr) - 1:
            current_score = abs(arr[left] - arr[right])
            result += current_score

            left += 1
            right += 1
        return result
        

# -- solution 2
class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0
        for i in range(len(s) - 1):
            total += abs(ord(s[i]) - ord(s[i + 1]))
        return total
    
    
    
# -- solution 3 in JAVASCRIPT
# var scoreOfString = function(s) {
#     let score = 0;
#     for (let i = 1; i < s.length; i++) {
#      score += Math.abs(s.charCodeAt(i - 1) - s.charCodeAt(i));
#     }
#     return score;
# };