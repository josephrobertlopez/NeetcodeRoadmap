import pytest
from .arrays_and_hashing import Solution  # Adjust the import as necessary


@pytest.mark.parametrize("nums, output_bool", [
    ([1, 2, 3, 1], True),
    ([1, 2, 3, 4], False),
    ([111, 33, 4, 3, 2, 4, 2], True),
])
def test_containsDuplicate(nums, output_bool):
    assert Solution().containsDuplicate(nums) == output_bool


@pytest.mark.parametrize("s,t,output_bool", [
    ("anagram", "nagaram", True),
    ("rat", "car", False)
])
def test_isAnagram(s, t, output_bool):
    assert Solution().isAnagram(s, t) == output_bool


@pytest.mark.parametrize("nums, target, out_vals", [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1])
])
def test_twoSums(nums, target, out_vals):
    assert Solution().twoSum(nums, target) == out_vals


@pytest.mark.parametrize("strs, out_strs", [
    (["eat", "tea", "tan", "ate", "nat", "bat"], [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
    ([""], [[""]]),
    (["a"], [["a"]])
])
def test_groupAnagrams(strs, out_strs):
    def set_of_frozen_sets(data: list[list[str]]) -> set:
        out_set = set()
        for inner_list in data:
            frozen_inner = frozenset(inner_list)
            out_set.add(frozen_inner)
        return out_set

    assert set_of_frozen_sets(Solution().groupAnagrams(strs)) == set_of_frozen_sets(out_strs)


@pytest.mark.parametrize("nums, k, highest_freq", [
    ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
    ([1], 1, [1]),
])
def test_topKFrequent(nums, k, highest_freq):
    assert set(Solution().topKFrequent(nums, k)) == set(highest_freq)

@pytest.mark.parametrize("nums, out_list",[
    ([1,2,3,4],[24,12,8,6]),
    ([-1, 1, 0, -3, 3],[0,0,9,0,0]),
])
def test_productExceptSelf(nums, out_list):
    assert Solution().productExceptSelf(nums)==out_list

@pytest.mark.parametrize("nums, longestConsecutive", [
    ([100,4,200,1,3,2], 4),
    ([0,3,7,2,5,8,4,6,0,1], 9),
])
def test_longestConsecutive(nums, longestConsecutive):
    assert Solution().longestConsecutive(nums) == longestConsecutive