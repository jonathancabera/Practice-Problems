# ============================================================
# PAIR SUM COUNT
# Difficulty: Easy / Medium
# Pattern: Hash Map / Frequency Map
# ============================================================
#
# Given a list of integers and a target value, return the
# number of unique pairs (i, j) where i < j and
# nums[i] + nums[j] == target.
#
# A "unique pair" means you cannot reuse the same index twice,
# but identical values at different indices are allowed.
#
# Examples:
#   count_pairs([1, 2, 3, 4, 3], 6)  => 2
#     Pairs: (2,4) and (3,3)
#
#   count_pairs([1, 1, 1, 1], 2)     => 6
#     All combinations of two 1s: C(4,2) = 6
#
#   count_pairs([5, 5, 5], 10)       => 3
#     (5@0,5@1), (5@0,5@2), (5@1,5@2)
#
#   count_pairs([1, 2, 3], 10)       => 0
#     No valid pairs
#
# Constraints:
#   - 2 <= len(nums) <= 100,000
#   - -10,000 <= nums[i] <= 10,000
#   - -20,000 <= target <= 20,000
# ============================================================

from typing import List

def count_pairs(nums: List[int], target: int) -> int:
    # YOUR CODE HERE
    pass


# ============================================================
# TEST RUNNER — do not edit below this line
# ============================================================

passed = 0
failed = 0

def test(description, nums, target, expected):
    global passed, failed
    result = count_pairs(nums, target)
    if result == expected:
        print(f"  ✅ PASS — {description}")
        passed += 1
    else:
        print(f"  ❌ FAIL — {description}")
        print(f"       nums:     {nums}")
        print(f"       target:   {target}")
        print(f"       Expected: {expected}")
        print(f"       Got:      {result}")
        failed += 1

print("\n🔢 Pair Sum Count Tests\n")

test('Two distinct pairs',              [1, 2, 3, 4, 3],      6,   2)
test('Four identical values',           [1, 1, 1, 1],         2,   6)
test('Three identical values',          [5, 5, 5],            10,  3)
test('No valid pairs',                  [1, 2, 3],            10,  0)
test('Negative numbers',                [-1, -2, 3, 4, -3],   1,   2)
test('Target zero with negatives',      [-3, 3, -2, 2, 0, 0], 0,   3)
test('Single pair only',                [1, 9, 2, 8],         10,  2)
test('All elements the same, no pair',  [3, 3, 3],            7,   0)
test('Large array, one valid pair',     [1, 2, 4, 5, 6],      3,   1)
test('Mixed signs, target negative',    [-5, -5, 2, 3],       -10, 1)
test('Two elements, valid pair',        [4, 6],               10,  1)
test('Two elements, invalid pair',      [4, 6],               9,   0)

print(f"\n{passed} passed, {failed} failed\n")
