class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        # Prend le premier mot comme référence
        for i in range(len(strs[0])):
            char = strs[0][i]
            for word in strs[1:]:
                # Vérifie si l'index dépasse ou si le caractère diffère
                if i >= len(word) or word[i] != char:
                    return strs[0][:i]
        
        return strs[0]
