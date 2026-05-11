# ============================================================
# MOST FREQUENT WORDS
# Difficulty: Easy
# Pattern: Hash Map / Frequency Map
# ============================================================
#
# Given a list of lowercase words and a number k, return the
# k most frequently occurring words, sorted by frequency
# (highest first). Break ties alphabetically (a before b).
#
# Examples:
#   top_k_words(["the","cat","sat","the","cat","the"], 2)
#     => ["the", "cat"]
#
#   top_k_words(["one","two","one","two","three"], 3)
#     => ["one", "two", "three"]
#
#   top_k_words(["apple","banana","apple","banana"], 1)
#     => ["apple"]       (tie broken alphabetically)
#
# Constraints:
#   - 1 <= len(words) <= 10,000
#   - 1 <= k <= number of unique words
#   - All words are lowercase letters only
# ============================================================

from typing import List

def top_k_words(words: List[str], k: int) -> List[str]:
    # YOUR CODE HERE
    pass


# ============================================================
# TEST RUNNER — do not edit below this line
# ============================================================

passed = 0
failed = 0

def test(description, words, k, expected):
    global passed, failed
    result = top_k_words(words, k)
    if result == expected:
        print(f"  ✅ PASS — {description}")
        passed += 1
    else:
        print(f"  ❌ FAIL — {description}")
        print(f"       Words:    {words}")
        print(f"       k:        {k}")
        print(f"       Expected: {expected}")
        print(f"       Got:      {result}")
        failed += 1

print("\n📊 Most Frequent Words Tests\n")

test('Basic case, clear winner',
  ["the","cat","sat","the","cat","the"], 2,
  ["the", "cat"]
)
test('Three-way result, k=3',
  ["one","two","one","two","three"], 3,
  ["one", "two", "three"]
)
test('Tie broken alphabetically',
  ["apple","banana","apple","banana"], 1,
  ["apple"]
)
test('All words appear once — alphabetical order',
  ["zebra","mango","apple"], 2,
  ["apple", "mango"]
)
test('k equals total unique words',
  ["hi","hi","bye"], 2,
  ["hi", "bye"]
)
test('Single word repeated',
  ["go","go","go"], 1,
  ["go"]
)
test('Mixed frequencies, pick top 1',
  ["a","b","b","c","c","c"], 1,
  ["c"]
)
test('Mixed frequencies, pick top 2',
  ["a","b","b","c","c","c"], 2,
  ["c", "b"]
)
test('All same frequency — fully alphabetical',
  ["dog","cat","ant"], 3,
  ["ant","cat","dog"]
)
test('k=1 with clear winner',
  ["x","x","x","y","y","z"], 1,
  ["x"]
)

print(f"\n{passed} passed, {failed} failed\n")
