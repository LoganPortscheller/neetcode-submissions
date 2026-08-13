class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Each char in s maped to number of time it occurs in s
        s_char_histogram = dict()

        # Populate histogram
        for s_char in s:
            if s_char in s_char_histogram:
                s_char_histogram[s_char] += 1
            else:
                s_char_histogram[s_char] = 1

        print(s_char_histogram)

        # Decrement histogram for every character that occurs in t
        for t_char in t:
            # t_char never occurs in s_char
            if t_char not in s_char_histogram:
                return False
            
            # t_char occurs in s -> decremement value by 1
            s_char_histogram[t_char] -= 1

            # t_char occurs more in t than in s
            if s_char_histogram[t_char] < 0:
                return False

        print(s_char_histogram)

        # Check that all values in histogram are 0
        for val in s_char_histogram.values():
            if val != 0:
                return False
        return True


        