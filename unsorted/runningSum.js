/**
 * @copyright https://leetcode.com/problems/running-sum-of-1d-array/
 * @param {number[]} nums
 * @return {number[]}
 */
const reducer = (array) => array.reduce((accum, currVal) => accum + currVal);
export default function runningSum(nums) {
  let results = Array(nums.length);
  for (let i = 0; i < nums.length; i++) {
    results[i] = reducer(nums.slice(0, i + 1));
  }
  return results;
}
