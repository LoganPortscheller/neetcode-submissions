class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_freq_table_to_list_of_strs = dict()

        for string in strs:
            # Building char frequency table for string
            char_freq_table = [0] * 26
            for char in string:
                char_freq_table[ord(char) - ord("a")] += 1

            char_freq_table_as_tuple = tuple(char_freq_table)

            char_freq_table_to_list_of_strs.setdefault(char_freq_table_as_tuple, []).append(string)

        return list(char_freq_table_to_list_of_strs.values())

            

            


                

            

            



            


        