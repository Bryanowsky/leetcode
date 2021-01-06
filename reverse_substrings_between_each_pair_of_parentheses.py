# You are given a string s that consists of lower case English letters and brackets.
#
# Reverse the strings in each pair of matching parentheses, starting from the innermost one.
#
# Your result should not contain any brackets.
#
#
#
# Example 1:
#
# Input: s = "(abcd)"
# Output: "dcba"
# Example 2:
#
# Input: s = "(u(love)i)"
# Output: "iloveu"
# Explanation: The substring "love" is reversed first, then the whole string is reversed.
# Example 3:
#
# Input: s = "(ed(et(oc))el)"
# Output: "leetcode"
# Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.
# Example 4:
#
# Input: s = "a(bcdefghijkl(mno)p)q"
# Output: "apmnolkjihgfedcbq"

# This solution works fine but it is a pretty complex


# class Solution:
#     def reverse_parentheses(self, s: str) -> str:
#         stack = []
#         index = 0
#         reverse_ = ''
#         s_ = list(s)
#         while '(' in s_ and ')' in s_:
#             if s_[index] != ')':
#                 stack.append(s_[index])
#                 index += 1
#             elif s_[index] == ')' and stack:
#                 s_.pop(index)
#                 suffix = s_[index:]
#                 print('stack', stack)
#                 reverse = stack.pop()
#                 while reverse != '(':
#                     reverse_ += reverse
#                     reverse = stack.pop()
#                 index = index - len(reverse_) - 1
#                 s_.pop(index)
#                 prefix = s_[:index]
#                 stack = []
#                 s_ = prefix + list(reverse_) + suffix
#                 index = 0
#                 print(reverse_, s_)
#                 reverse_ = ''
#         return ''.join(s_)



class Solution:
    def reverse_parentheses(self, s: str) -> str:
        stack = []
        index = 0
        reverse_ = ''
        s_ = list(s)
        while '(' in s_ and ')' in s_:
            if s_[index] != ')':
                stack.append(s_[index])
                index += 1
            elif s_[index] == ')' and stack:
                s_.pop(index)
                suffix = s_[index:]
                print('stack', stack)
                reverse = stack.pop()
                while reverse != '(':
                    reverse_ += reverse
                    reverse = stack.pop()
                index = index - len(reverse_) - 1
                s_.pop(index)
                prefix = s_[:index]
                stack = []
                s_ = prefix + list(reverse_) + suffix
                index = 0
                print(reverse_, s_)
                reverse_ = ''
        return ''.join(s_)

solution = Solution()
print(solution.reverse_parentheses('(abcd)'))
