class Solution:
    def isValid(self, s: str) -> bool:
        open_ = []
        parentheses = []
        brackets = []
        curly = []
        for item in s:
            if item == '(':
                parentheses.append(item)
                open_.append(item)
            elif item == '[':
                brackets.append(item)
                open_.append(item)
            elif item == '{':
                curly.append(item)
                open_.append(item)
            elif item == ')':
                if parentheses and open_.pop() == '(':
                    parentheses.pop()
                else:
                    return False
            elif item == ']':
                if brackets and open_.pop() == '[':
                    brackets.pop()
                else:
                    return False
            elif item == '}':
                if curly and open_.pop() == '{':
                    curly.pop()
                else:
                    return False
        if parentheses or brackets or curly:
            return False
        return True
