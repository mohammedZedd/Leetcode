class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        R = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0

        for i in range(len(s) - 1):
            if R[s[i]] < R[s[i + 1]]:
                total -= R[s[i]]
            else:
                total += R[s[i]]
        
        total += R[s[-1]]  
        return total
