class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        reversedString = s [::-1]
        answer = 0
        test = reversedString.strip()

        if len(test) == 1:
            return 1
        for c in test:
            if c.isspace():
                return answer
            else:
                answer = answer + 1
        return answer
