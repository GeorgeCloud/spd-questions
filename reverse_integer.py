class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            # escape early due to edge case
            return 0
        elif x > 0:
            # safe to reverse string with built-in slice method
            cand = int(str(x)[::-1])
            # ensure candidate is not out of bound
            if -2**31 <= cand <= 2**31 - 1:
                return cand
            else:
                # if out of bound return 0
                return 0
        else:
            # return negative number into positive then reverse then turn number back to negative
            cand = -int(str(-x)[::-1])
            # ensure candidate is not out of bound
            if -2**31 <= cand <= 2**31 - 1:
                return cand
            else:
                # if out of bound return 0
                return 0

            
