class Solution(object):
    def isPalindrome(self, x:int):
        """
        :type x: int
        :rtype: bool
        """
        # if x < 0:
        #     return False
        # return x == int("".join(list(reversed(list(str(x))))))
        num_str = str(x)
        reverse_str = num_str[::-1]

        if num_str == reverse_str:
            return True
        return False

print("palindrome: ",Solution().isPalindrome(10))