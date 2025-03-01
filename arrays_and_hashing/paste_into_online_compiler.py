import sys
from typing import List
class Solution:
    # https://leetcode.com/problems/contains-duplicate/
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Given an integer array nums, return true if any value appears at least twice in the array,
        and return false if every element is distinct.

        Args:
            nums (List[int]): The list of numbers to search in.

        Returns:
            bool: True if any element appears at least twice, False otherwise.
        """
        pass
    
    # https://leetcode.com/problems/valid-anagram/
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Given two strings s and t, return true if t is an anagram of s, and false otherwise.

        An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
        typically using all the original letters exactly once.

        Args:
            s (str): The original string.
            t (str): The potential anagram.

        Returns:
            bool: True if t is an anagram of s, False otherwise.
        """
        
        pass

    # https://leetcode.com/problems/two-sum/
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers, find two elements that add up to a given target sum.

        Args:
            nums (List[int]): The list of numbers to search in.
            target (int): The target sum that the two elements should add up to.

        Returns:
            List[int]: A list of two indices of the elements that add up to the target sum.
        """
        pass

    # https://leetcode.com/problems/group-anagrams/
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Given a list of strings, group the anagrams together and return the grouped strings.

        Args:
            strs (List[str]): The list of strings to group.

        Returns:
            List[List[str]]: A list of lists, where each sublist contains strings which are anagrams of each other.
        """
        pass

    # https://leetcode.com/problems/top-k-frequent-elements/
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Given a non-empty list of integers, return the k most frequent elements.

        Args:
            nums (List[int]): The list of integers.
            k (int): The number of top frequent elements to return.

        Returns:
            List[int]: A list of the k most frequent elements in descending order of frequency.
        """

        pass

    # https://leetcode.com/problems/product-of-array-except-self/
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Given an array of n integers where n > 1, return an array output such that output[i] is equal to the product of all the numbers in the input array except nums[i].

        Args:
            nums (List[int]): The list of numbers to compute the product of all elements except the current element.

        Returns:
            List[int]: A list of the product of all elements except the current element.
        """
        pass

    # https://leetcode.com/problems/longest-consecutive-sequence/
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Given an unsorted list of integers, return the length of the longest consecutive elements sequence.

        Args:
            nums (List[int]): The list of numbers to find the longest consecutive sequence in.

        Returns:
            int: The length of the longest consecutive elements sequence.
        """
        pass

def main():
    solution = Solution()
    
    test_cases = [
        # (solution.containsDuplicate, [[1, 2, 3, 1], [1, 2, 3, 4], [111, 33, 4, 3, 2, 4, 2]], [True, False, True]),
        # (solution.isAnagram, [("anagram", "nagaram"), ("rat", "car")], [True, False]),
        # (solution.twoSum, [([2, 7, 11, 15], 9), ([3, 2, 4], 6), ([3, 3], 6)], [[0, 1], [1, 2], [0, 1]]),
        # (solution.groupAnagrams, [["eat", "tea", "tan", "ate", "nat", "bat"], [""], ["a"]], [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
        # (solution.topKFrequent, [([1, 1, 1, 2, 2, 3], 2), ([1], 1)], [[1, 2], [1]]),
        # (solution.productExceptSelf, [[1,2,3,4], [-1, 1, 0, -3, 3]], [[24,12,8,6], [0,0,9,0,0]]),
        # (solution.longestConsecutive, [[100,4,200,1,3,2], [0,3,7,2,5,8,4,6,0,1]], [4, 9])
    ]
    
    for func, inputs, expected in test_cases:
        for inp, exp in zip(inputs, expected):
            result = func(*inp) if isinstance(inp, tuple) else func(inp)
            print(f"{func.__name__}({inp}) = {result}, expected: {exp}")
            assert result == exp, f"Test failed for {func.__name__}({inp})"
    
if __name__ == "__main__":
    main()
