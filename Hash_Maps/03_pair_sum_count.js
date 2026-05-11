// ============================================================
// PAIR SUM COUNT
// Difficulty: Easy / Medium
// Pattern: Hash Map / Frequency Map
// ============================================================
//
// Given an array of integers and a target value, return the
// number of unique pairs (i, j) where i < j and
// nums[i] + nums[j] === target.
//
// A "unique pair" means you cannot reuse the same index twice,
// but identical values at different indices are allowed.
//
// Examples:
//   countPairs([1, 2, 3, 4, 3], 6)  => 2
//     Pairs: (2,4) and (3,3)
//
//   countPairs([1, 1, 1, 1], 2)     => 6
//     All combinations of two 1s: C(4,2) = 6
//
//   countPairs([5, 5, 5], 10)       => 3
//     (5@0,5@1), (5@0,5@2), (5@1,5@2)
//
//   countPairs([1, 2, 3], 10)       => 0
//     No valid pairs
//
// Constraints:
//   - 2 <= nums.length <= 100,000
//   - -10,000 <= nums[i] <= 10,000
//   - -20,000 <= target <= 20,000
// ============================================================

function countPairs(nums, target) {
  // YOUR CODE HERE

}

// ============================================================
// TEST RUNNER — do not edit below this line
// ============================================================

let passed = 0;
let failed = 0;

function test(description, nums, target, expected) {
  const result = countPairs(nums, target);
  const pass = result === expected;
  if (pass) {
    console.log(`  ✅ PASS — ${description}`);
    passed++;
  } else {
    console.log(`  ❌ FAIL — ${description}`);
    console.log(`       nums:     [${nums.join(", ")}]`);
    console.log(`       target:   ${target}`);
    console.log(`       Expected: ${expected}`);
    console.log(`       Got:      ${result}`);
    failed++;
  }
}

console.log("\n🔢 Pair Sum Count Tests\n");

test('Two distinct pairs',             [1, 2, 3, 4, 3],    6,   2);
test('Four identical values',          [1, 1, 1, 1],       2,   6);
test('Three identical values',         [5, 5, 5],          10,  3);
test('No valid pairs',                 [1, 2, 3],          10,  0);
test('Negative numbers',               [-1, -2, 3, 4, -3], 1,   2);
test('Target zero with negatives',     [-3, 3, -2, 2, 0, 0], 0, 3);
test('Single pair only',               [1, 9, 2, 8],       10,  2);
test('All elements the same, no pair', [3, 3, 3],          7,   0);
test('Large array, one valid pair',    [1, 2, 4, 5, 6],    3,   1);
test('Mixed signs, target negative',   [-5, -5, 2, 3],     -10, 1);
test('Two elements, valid pair',       [4, 6],             10,  1);
test('Two elements, invalid pair',     [4, 6],             9,   0);

console.log(`\n${passed} passed, ${failed} failed\n`);
