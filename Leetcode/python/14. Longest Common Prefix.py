class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = strs[0]
        k = ""

        counter = 0
        while counter < len(i):
            for j in strs[1:] :
                if not j.startswith(i[:counter+1]):
                    return k
            counter += 1
            k = i[:counter] 
        return k

