# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
# Example 2:

# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s
# Example 3:

# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d
# Constraints:

# 1 <= word1.length, word2.length <= 100
# word1 and word2 consist of lowercase English letters.


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        rez = []

        len_word1 = len(word1)
        len_word2 = len(word2)

        if len_word1 == len_word2:
            c = 0
            for first in word1:
                c = c + 1
                rez.append(first)
                rez.insert(len(rez), word2[c-1])
                
        return str(rez)

Sol = Solution()
word1 = "abc"
word2 = "pqr"
print(Sol.mergeAlternately(word1, word2)) #"apbqcr"

Sol = Solution()
word1 = "ab"
word2 = "pqr"
print(Sol.mergeAlternately(word1, word2)) #"apbqcr"


