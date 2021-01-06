class Solution:
    def count_and_say(self, n: int) -> str:
        if n == 1:
            return '1'
        else:
            return self.generate_string(n, '')

    def generate_string(self, n: int, result: str) -> str:
        if n == 0:
            return result
        else:
            if result == '':
                return self.generate_string(n-1, '1')
            else:
                new_line = ''
                init_char = ''
                counter_char = 0
                for i in range(len(result)):
                    if i == 0:
                        init_char = result[0]
                        counter_char = 1
                    else:
                        if result[i] == init_char:
                            counter_char += 1
                        else:
                            new_line += str(counter_char) + str(init_char)
                            init_char = result[i]
                            counter_char = 1
                new_line += str(counter_char) + str(init_char)
                return self.generate_string(n-1, new_line)


solution = Solution()
print(solution.count_and_say(6))
