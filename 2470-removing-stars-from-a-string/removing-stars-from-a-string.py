class Solution:
    def removeStars(self, s: str) -> str:
        final_stack = []
        for i in s:
            if i!= '*':
                final_stack.append(i)
            else:
                final_stack.pop()
        return "".join(final_stack)
