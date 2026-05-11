# ============================================================
# GROUP ANAGRAM SENTENCES
# Difficulty: Medium
# Pattern: Hash Map / Frequency Map
# ============================================================
#
# You are given a list of sentences (each a single string of
# lowercase words separated by spaces). Group the sentences
# together if they are "word anagrams" of each other — meaning
# they contain exactly the same words with the same frequencies,
# just possibly in a different order.
#
# Return a list of groups. Within each group, sentences must
# appear in the same order they appeared in the input. The
# groups themselves must be sorted by the index of their
# first sentence in the input (i.e. the group whose first
# sentence appeared earliest comes first).
#
# Examples:
#   Input: [
#     "the cat sat",
#     "hello world",
#     "sat the cat",
#     "world hello",
#     "cat sat the"
#   ]
#   Output: [
#     ["the cat sat", "sat the cat", "cat sat the"],
#     ["hello world", "world hello"]
#   ]
#
#   Input: ["go home", "go go", "home go", "stop"]
#   Output: [
#     ["go home", "home go"],
#     ["go go"],
#     ["stop"]
#   ]
#
# Note: "go home" and "home go" are word-anagrams (same words,
# different order). "go go" has two "go"s — different frequency,
# so it is its own group.
#
# Constraints:
#   - 1 <= len(sentences) <= 10,000
#   - Each sentence contains 1–10 words
#   - All characters are lowercase letters or spaces
#   - No leading, trailing, or double spaces
# ============================================================

from typing import List

def group_anagram_sentences(sentences: List[str]) -> List[List[str]]:
    # YOUR CODE HERE
    pass


# ============================================================
# TEST RUNNER — do not edit below this line
# ============================================================

passed = 0
failed = 0

def test(description, sentences, expected):
    global passed, failed
    result = group_anagram_sentences(sentences)
    if result == expected:
        print(f"  ✅ PASS — {description}")
        passed += 1
    else:
        print(f"  ❌ FAIL — {description}")
        print(f"       Input:    {sentences}")
        print(f"       Expected: {expected}")
        print(f"       Got:      {result}")
        failed += 1

print("\n🗂️  Group Anagram Sentences Tests\n")

test('Three-way and two-way group',
  ["the cat sat", "hello world", "sat the cat", "world hello", "cat sat the"],
  [["the cat sat", "sat the cat", "cat sat the"], ["hello world", "world hello"]]
)
test('Frequency matters — go go is its own group',
  ["go home", "go go", "home go", "stop"],
  [["go home", "home go"], ["go go"], ["stop"]]
)
test('All sentences are unique groups',
  ["one two", "three four", "five six"],
  [["one two"], ["three four"], ["five six"]]
)
test('All sentences are one group',
  ["a b c", "b c a", "c a b"],
  [["a b c", "b c a", "c a b"]]
)
test('Single word sentences',
  ["cat", "dog", "cat", "dog", "fish"],
  [["cat", "cat"], ["dog", "dog"], ["fish"]]
)
test('Single sentence input',
  ["hello world"],
  [["hello world"]]
)
test('Order within group preserved',
  ["z y x", "a b c", "y z x", "c a b"],
  [["z y x", "y z x"], ["a b c", "c a b"]]
)
test('Repeated word changes group',
  ["a a b", "a b a", "a b b"],
  [["a a b", "a b a"], ["a b b"]]
)

print(f"\n{passed} passed, {failed} failed\n")
