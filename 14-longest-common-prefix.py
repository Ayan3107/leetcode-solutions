class Solution:
    def longestCommonPrefix(self, strs):
        prefix =""

        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix =prefix[:-1]

                if prefix =="":
                    return""

        return prefix        