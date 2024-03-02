class Solution:
    # https://leetcode.com/problems/contains-duplicate/
    def containsDuplicate(self, nums: list[int]) -> bool:
        values = set()
        for i,n in enumerate(nums):
            if n in values:
                return True
            else:
                values.add(n)
        return False

    # https://leetcode.com/problems/valid-anagram/
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq_dict_s = dict()
        freq_dict_t = dict()
        for i in range(len(s)):
            freq_dict_s[s[i]]=1+freq_dict_s.get(s[i],0)
            freq_dict_t[t[i]]=1+freq_dict_t.get(t[i],0)

        for char in freq_dict_s:
            if freq_dict_s[char] != freq_dict_t.get(char,0):
                return False
        return True

    # https://leetcode.com/problems/two-sum/
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_indices = dict()
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_indices:
                return [num_indices[complement], i]
            num_indices[num] = i

    # https://leetcode.com/problems/group-anagrams/
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_groups = dict()
        for i, word in enumerate(strs):
            sorted_word = tuple(sorted(word))
            if sorted_word not in anagram_groups:
                anagram_groups[sorted_word] = [i]
            else:
                anagram_groups[sorted_word].append(i)

        output_list = []
        for sorted_word in anagram_groups:
            group = []
            for i in anagram_groups[sorted_word]:
                group.append(strs[i])
            output_list.append(group)

        return output_list

    # https://leetcode.com/problems/top-k-frequent-elements/
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        numDict = dict()
        for n in nums:
            if n not in numDict.keys():
                numDict[n] = 1
            else:
                numDict[n]+=1
        keys = sorted(numDict,key=numDict.__getitem__,reverse=True)
        return keys[:k]

    # https://leetcode.com/problems/product-of-array-except-self/
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        out_list = []
        prefix_product_list = [1]
        suffix_product_list = [1]
        prod = 1
        for i in range(len(nums)-1):
            prod*=nums[i]
            prefix_product_list.append(prod)
        prod = 1
        for i in range(len(nums)-1,0,-1):
            prod*=nums[i]
            suffix_product_list.append(prod)

        suffix_product_list = suffix_product_list[::-1]

        for i in range(len(nums)):
            out_list.append(prefix_product_list[i]*suffix_product_list[i])

        return out_list

    # https://leetcode.com/problems/longest-consecutive-sequence/
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        max_length = 0

        for num in nums:
            if num - 1 not in num_set:
                current_num = num
                current_length = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1

                max_length = max(max_length, current_length)

        return max_length