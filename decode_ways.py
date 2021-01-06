# Your previous Plain Text content is preserved below:
#
# Lets say we map the 'A' to 'Z' as 1 to 26 as shown below
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#
# Given a numerical string, output number of ways that the numerical string can be interpreted.
#
# Example 1:
# ---------
# Input: "12"
# Output: 2
# Explanation: It could be interpreted as "AB" (1 2) or "L" (12).
#
# Example 2:
# ----------
# Input: "226"
# Output: 3
# Explanation: It could be interpreted as as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
#
# Example 3:
# ----------
# Input: "23232323"
# Output: 16
#
# Example 4:
# ----------
# Input: "12212112"
# Output: 34
#

# import string
#
# indexes = range(1, 27)
# CHARS_DICT = {index: string.ascii_uppercase[index-1] for index in indexes}
#
#
# def generate_combinations(input_string: str, index: int, result_string: str, combinations: []):
#     if index == 0 and input_string[index] == '0':
#         return []
#
#     if index == len(input_string):
#         combinations.append(result_string)
#
#     possible_combination = 0
#
#     for j in range(index, len(input_string)):
#         if input_string[j-1] == '0' and j > index:
#             continue
#
#         possible_combination = (possible_combination * 10) + int(input_string[j])
#
#         if 1 <= possible_combination <= 26:
#             print('entering', result_string, possible_combination)
#             generate_combinations(input_string, j+1, result_string + CHARS_DICT.get(possible_combination, '0'),
#                                   combinations)
#
#     return combinations
#
#
# print(generate_combinations('1029', 0, '', []))


def generate_combinations(input_string: str) -> int:
    if len(input_string) < 1:
        return 1

    possible_combinations = [0] * (len(input_string) + 1)

    possible_combinations[0] = 1
    possible_combinations[1] = 0 if input_string[0] == '0' else 1

    for i in range(2, len(input_string) + 1):
        if 1 <= int(input_string[i-1]) <= 10:
            possible_combinations[i] += possible_combinations[i-1]
        if 10 <= int(input_string[i-2:i]) <= 26:
            possible_combinations[i] += possible_combinations[i-2]
    return possible_combinations[-1]


print(generate_combinations(''))


