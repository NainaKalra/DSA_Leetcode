class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        first_word = strs[0]

        for i in range(len(first_word)):
            char = first_word[i]
            for j in range(1,len(strs)):
                #if word is short or char doesn't matches
                if i == len(strs[j]) or strs[j][i]!= char:
                    return first_word[:i]
        return first_word