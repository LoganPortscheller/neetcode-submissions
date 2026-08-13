class Solution:
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     # Sort the nums array (O(n log n))
    #     # Itterate through array backwards, until you find the kth most frequent element (O(n))
    #     # Overall: O(n log n)

    #     # Use histogram to count the number of occurances of the integers in nums
    #     num_frequency_dict = {}
    #     for num in nums:
    #         if num in num_frequency_dict:
    #             num_frequency_dict[num] = num_frequency_dict[num] + 1
    #         else:
    #             num_frequency_dict[num] = 1

    #     # Generate a list of the frequencies
    #     frequency_list = []
    #     for frequency in num_frequency_dict.values():
    #         frequency_list.append(frequency)

    #     sort(frequency_list, reverse=False)
    #     frequency_rank = 1
    #     prev_frequency = 0
    #     for i in range(len(frequency_list)):

    # 1) Count frequency of each integer in nums in dict
    # 2) Loop through key-value pairs in dict and assigning the 
    #    my_list[freq] = my_List_of_vals_with_this_freq
    # 3) Itterate through the list from -1000 to 1000 until we find the 
    #    kth most frequent integer (and return this list)
            
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequency of each integer in nums
        num_to_frequency = {}
        for num in nums:
            if num in num_to_frequency:
                num_to_frequency[num] = num_to_frequency[num] + 1
            else:
                num_to_frequency[num] = 1

        # freq_list[i] = list of integers in num that occur i times
        freq_list = [[]]
        # for i in range(len(num_to_frequency) + 1):
        #     freq_list.append([])

        for num, frequency in num_to_frequency.items():
            if frequency > (len(freq_list) - 1):
                for a in range(len(freq_list), frequency + 1):
                    freq_list.append([])
            
            freq_list[frequency].append(num)

        # Return the list of top k frequencies
        topKNums = []

        for j in range(len(freq_list) - 1, 0, -1):
            topKNums += freq_list[j]

            if (len(topKNums) >= k):
                return topKNums