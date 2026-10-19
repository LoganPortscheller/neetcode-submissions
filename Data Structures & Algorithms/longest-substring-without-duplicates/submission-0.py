class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_longest_substr = 0
        chars_in_substr = set()
        l = 0
        r = 0

        while r < len(s):
            # Runs until substring s[l, r] (inclusive) doesn't repeat any chars
            while s[r] in chars_in_substr:
                chars_in_substr.remove(s[l])
                l += 1

            # At this point, s[l, r] is the longest valid substring ending at
            # index r
            len_longest_substr = max(len_longest_substr, r - l + 1)
            chars_in_substr.add(s[r])

            r += 1

        return len_longest_substr

    
        