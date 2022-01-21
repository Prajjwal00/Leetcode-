#Longest substring without a repeating charecter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict1={}
        start=0
        max_len=0
        for i in range(0,len(s)):
            if s[i] in dict1:
                start=max(start,dict1[s[i]]+1)
            max_len=max(max_len,i-start+1)
            dict1[s[i]]=i
        return max_len
