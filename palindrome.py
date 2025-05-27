class Solution1(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_str = str(x)
        n = len(x_str)
        
        for i in range(n//2):
            if x_str[i] != x_str[n-1-i]:
                return False
        
        return True




class Solution2(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        digits = []
        n = x

        # Étape 1 : extraire les chiffres (de droite à gauche)
        for i in range(10):  # un entier 32 bits a au max 10 chiffres
            if n == 0 and i > 0:
                break
            digits.append(n % 10)
            n //= 10

        # Étape 2 : comparer symétriquement les chiffres
        length = len(digits)
        for i in range(length // 2):
            if digits[i] != digits[length - 1 - i]:
                return False

        return True
