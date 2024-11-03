class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if s == goal:
            return True

        if len(s) != len(goal):
            return False
        
        ans = False

        for index in range(1, len(goal)):
            if s[index:] + s[:index] == goal:
                ans = True
                break

        return ans