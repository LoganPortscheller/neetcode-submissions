class Solution:

    def encode(self, strs: List[str]) -> str:
        # If we use ' '.join(), this wouldn't work because there is no
        # limitation on the characters that can exist in the strings. Delimiters
        # can't be guaranteed to work

        # However, if we check for occurance of delimiters when we copy strings
        # into a list, we can escape them in a certain way. However, there's no guarantee
        # that is escape sequence doesn't occur in our intput strings, so using delimters
        # is not guaranteed to work

        # We could copy each character over one-by-one and then input whether a delimter occurs
        # on certain indexes (like even indexes)

        # We could append the string with information on where to place delimeters
        # For example, a character denoting where each delimter is, terminated by
        # a certain unused character

        # Strategy:
        # 1) Loop through and store length of strings O(strs.length)
        # 2) Append the terminating character (O(1))
        # 3) Append strings (O(1) amortized)
        # 4) Join list with an empty string O(total chars)

        encode_list = []
        for s in strs:
            encode_list.append(chr(len(s)))
        
        # Append length terminator
        # We know no string in strs is of length 200
        encode_list.append(chr(200))

        # Append all the strings in strs
        encode_list += strs

        encoded_str = "".join(encode_list)

        return encoded_str

    def decode(self, s: str) -> List[str]:
        # Read in string an split into length data list and strs_chars
        # Use data list and strs_chars to determine where to split each string
        str_lengths = []

        # Find first instance of string length terminator
        for i in range(len(s)):
            char = s[i]
            # If the character is the string length terminator, break
            if char == chr(200):
                break

            str_lengths.append(ord(char))

        # Point i to start of characters section of s
        i += 1
        strs = []
        for str_len in str_lengths:
            current_str = s[i : (i + str_len)]
            strs.append(current_str)

            # Point i to the first character of the next string
            i += str_len

        return strs


