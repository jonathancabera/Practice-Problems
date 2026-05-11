# ============================================================
# FIRST UNIQUE CHARACTER
# Difficulty: Easy
# Pattern: Hash Map / Frequency Map
# ============================================================
#
# Given a string of lowercase letters, return the index of the
# first character that appears exactly once in the string.
# If no such character exists, return -1.
#
# Examples:
#   first_unique_char("abacabad")  => 6   ('d' at index 6)
#   first_unique_char("aabbcc")    => -1  (all repeat)
#   first_unique_char("z")         => 0   (single char is unique)
#
# Constraints:
#   - 1 <= len(s) <= 10,000
#   - s consists of lowercase English letters only
# ============================================================

def first_unique_char(s: str) -> int:
    # YOUR CODE HERE
    pass


# ============================================================
# TEST RUNNER — do not edit below this line
# ============================================================

passed = 0
failed = 0

def test(description, input_val, expected):
    global passed, failed
    result = first_unique_char(input_val)
    if result == expected:
        print(f"  ✅ PASS — {description}")
        passed += 1
    else:
        print(f"  ❌ FAIL — {description}")
        print(f"       Input:    \"{input_val}\"")
        print(f"       Expected: {expected}")
        print(f"       Got:      {result}")
        failed += 1

print("\n🔤 First Unique Character Tests\n")

test('Unique char at end',              "abacabad",  6)
test('No unique chars',                 "aabbcc",    -1)
test('Single character string',         "z",         0)
test('All unique — returns first',      "abcde",     0)
test('Unique char at start',            "abba",      -1)
test('Unique char in the middle',       "aabcca",    3)
test('Two unique chars — first wins',   "xxyzz",     2)
test('Long repeated prefix',            "aaaaaab",   6)
test('Repeated pairs, one odd one out', "ccddeeaf",  6)
test('Single repeated char',            "aaaa",      -1)

print(f"\n{passed} passed, {failed} failed\n")
