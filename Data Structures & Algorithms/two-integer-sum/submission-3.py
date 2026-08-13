class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        int_to_idx_dict = dict()
        
        for i in range(len(nums)):
            needed_operand = target - nums[i]

            if needed_operand in int_to_idx_dict:
                return [int_to_idx_dict[needed_operand][0], i]
            
            if nums[i] in int_to_idx_dict:
                int_to_idx_dict[nums[i]].append(i)
            else:
                int_to_idx_dict[nums[i]] = [i]
        
        # for i in range(len(nums)):
        #     needed_operand = target - nums[i]

        #     if (needed_operand == nums[i]):
        #         continue

        #     if needed_operand in num_exists_in_list:
        #         other_idx = num_exists_in_list[needed_operand]

        #         if i < other_idx:
        #             return [i, other_idx]
        #         else:
        #             return [other_idx, i]
        