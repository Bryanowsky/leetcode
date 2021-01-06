class Solution:
    def compress_string(self, chars: [str]) -> int:
        init_char = ''
        counter_char = 1
        index = 0
        while index < len(chars):
            if init_char == '':
                init_char = chars[index]
            else:
                if chars[index] == init_char:
                    counter_char += 1
                    chars.pop(index-1)
                    index -= 1
                else:
                    if counter_char > 1:
                        chars.insert(index, list(str(counter_char)))
                        index += 1
                    init_char = chars[index]
                    counter_char = 1
            index += 1
        if counter_char > 1:
            chars.insert(index, list(str(counter_char)))
            index += 1
        print(chars)
        return len(chars)


solution = Solution()
print(solution.compress_string(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
# print(solution.compress_string(["a", "a", "b", "b", "c", "c", "c"]))
# print(solution.compress_string(["a", "a", "a", "a"]))
