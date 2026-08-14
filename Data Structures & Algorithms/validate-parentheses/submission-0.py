class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        bracket = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        for i in s:
            if i in '([{':
                stack.append(i)

            else:
                if not stack or stack[-1] != bracket[i]:
                    return False

                stack.pop()

        return len(stack) == 0