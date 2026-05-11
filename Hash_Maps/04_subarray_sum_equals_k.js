// ============================================================
// SUBARRAY SUM EQUALS K
// Difficulty: Medium
// Pattern: Hash Map / Frequency Map
// ============================================================
//
// Given an array of integers (which may include negatives and
// zeros) and an integer k, return the total number of
// contiguous subarrays whose elements sum to exactly k.
//
// A subarray is a contiguous portion of the array.
// The same element can appear in multiple valid subarrays.
//
// Examples:
//   subarrayCount([2, 1, 3, -1, 2], 3)  => 3
//     [2,1], [3], [1,3,-1]
//
//   subarrayCount([1, 1, 1], 2)          => 2
//     [1,1] starting at index 0 and index 1
//
//   subarrayCount([1, -1, 1], 1)         => 3
//     [1], [-1,1,1] — wait, check manually:
//     [1] at idx 0, [1,-1,1] sums to 1, [1] at idx 2
//
//   subarrayCount([3], 3)                => 1
//
// Hint: Think about prefix sums. If you track how many times
// each prefix sum has occurred, you can determine in O(1)
// whether adding the current element completes a valid subarray.
//
// Constraints:
//   - 1 <= nums.length <= 50,000
//   - -1,000 <= nums[i] <= 1,000
//   - -1,000,000 <= k <= 1,000,000
// ============================================================

function subarrayCount(nums, k) {
  // YOUR CODE HERE

}

// ============================================================
// TEST RUNNER — do not edit below this line
// ============================================================

let passed = 0;
let failed = 0;

function test(description, nums, k, expected) {
  const result = subarrayCount(nums, k);
  const pass = result === expected;
  if (pass) {
    console.log(`  ✅ PASS — ${description}`);
    passed++;
  } else {
    console.log(`  ❌ FAIL — ${description}`);
    console.log(`       nums:     [${nums.join(", ")}]`);
    console.log(`       k:        ${k}`);
    console.log(`       Expected: ${expected}`);
    console.log(`       Got:      ${result}`);
    failed++;
  }
}

console.log("\n➕ Subarray Sum Equals K Tests\n");

test('Three valid subarrays',                [2, 1, 3, -1, 2],    3,  3);
test('Classic overlapping subarrays',        [1, 1, 1],           2,  2);
test('Includes negatives',                   [1, -1, 1],          1,  3);
test('Single element matches',               [3],                 3,  1);
test('Single element no match',              [3],                 4,  0);
test('Zero elements sum to k',               [0, 0, 0],           0,  6);
test('Negative k',                           [1, -2, 3, -1],      -1, 1);
test('Entire array is one valid subarray',   [1, 2, 3],           6,  1);
test('No valid subarrays',                   [1, 2, 3],           9,  0);
test('Repeated element equals k',            [5, 5, 5],           5,  3);
test('Negative values in subarray',          [-1, -1, 1, 1, 0],   0,  4);
test('k=0 with mixed positives/negatives',   [3, -3, 3, -3],      0,  4);

console.log(`\n${passed} passed, ${failed} failed\n`);
