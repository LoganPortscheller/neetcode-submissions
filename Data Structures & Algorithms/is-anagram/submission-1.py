class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if type(s) != str or type(t) != str:
            return None

        if len(s) != len(t):
            return False

        s_char_freq = dict()

        for s_char in s:
            if s_char in s_char_freq:
                s_char_freq[s_char] += 1
            else:
                s_char_freq[s_char] = 1

        for t_char in t:
            if t_char in s_char_freq and s_char_freq[t_char] > 0:
                s_char_freq[t_char] -= 1
            else:
                return False
        
        return True

        